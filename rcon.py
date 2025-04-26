"""
Minecraft-Twitch Integration Bot
-------------------------------
A bot that integrates Twitch chat voting with Minecraft server commands through RCON.
Features:
- Twitch chat voting system
- Real-time overlay for vote display
- Automated event execution
- WebSocket-based overlay communication

Made with love: @ivthered
"""

import mcrcon
import threading
import time
import random
import sys
import os
from queue import Queue
from twitchio.ext import commands
import requests
import webbrowser
import http.server
import socketserver
import asyncio
import websockets
import json
from colorama import init
from utils.colors import Colors
init()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from events import get_events

# API Configuration
RCON_CONFIG = {
    "host": "",
    "password": "",
    "port": 000
}

TWITCH_CONFIG = {
    "channel": "",
    "bot_username": "",
    "client_id": "",
    "client_secret": "",
    "redirect_uri": "http://localhost:8080",
    "whitelist": ["user1", "trusted_user1", "trusted_user2"]
}

# Global Variables
VOTING_DURATION_DEFAULT = 300  # 5 minutes
WEBSOCKET_PORT = 8765
OAUTH_PORT = 8080
COMMAND_DELAY = 0.1
PERIODIC_UPDATE = 5
MAX_EVENTS_HISTORY = 10  # Limit event history
CLEANUP_INTERVAL = 60  # Cleanup every 60 seconds

# Command Constants
EXECUTE_FORMAT = "execute at {player} run {command}"  # Bedrock execute format
DEFAULT_PLAYER = "playername"  # Default target player

# RCON Constants
RCON_RECONNECT_DELAY = 5  # Seconds between reconnection attempts
RCON_MAX_RETRIES = 2      # Maximum reconnection attempts before failing

# Additional Global Variables
PLAYER_NAMES = [
    "playername", "Player2", "Player3", "Player4", 
    "Player5", "Player6", "Player7", "Player8", "Player9", "Player10"
]
ACTIVE_PLAYERS = 1  # Set this to how many players you want (up to 10)

class VotingSystem(commands.Bot):
    """Main bot class handling Twitch chat integration and Minecraft RCON commands."""

    # Command templates updated for Bedrock
    CMD_TEMPLATES = {
        "execute": EXECUTE_FORMAT,
        "effect": "effect @a {} {} {} true",
        "say": "say {}",
        "playsound": "playsound {} @a",
        "weather": "weather {}"
    }

    # Get events from the separate module
    MINECRAFT_EVENTS = get_events(DEFAULT_PLAYER)

    def __init__(self, rcon_config, twitch_config, debug=False):
        """
        Initialize the bot with RCON and Twitch configurations.
        
        Args:
            rcon_config (dict): RCON connection settings
            twitch_config (dict): Twitch authentication settings
            debug (bool): Enable debug mode
        """
        # Set event loop
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        
        # OAuth initialization
        self.oauth_token = self.get_oauth_token(twitch_config)
        self.twitch_config = twitch_config  # Store for token refresh
        
        # Bot initialization
        super().__init__(
            token=self.oauth_token,
            prefix="!",
            initial_channels=[twitch_config["channel"]]
        )

        # Core attributes
        self.votes = {}  # Track votes by user
        self.vote_counts = {1: 0, 2: 0, 3: 0}  # Track vote counts
        self.rcon_queue = Queue()
        self.voting_duration = VOTING_DURATION_DEFAULT  # 5 minutes default
        self.current_vote = None
        self.voting_timer = None  # Change from thread to timer handle
        self.auto_vote = True
        
        # WebSocket/Overlay attributes
        self.overlay_clients = set()
        self.overlay_server_task = None
        self.overlay_server_running = False
        self.current_overlay_state = None
        
        # Configuration
        self.whitelist = [name.lower() for name in twitch_config.get("whitelist", [])]
        self.EVENT_DURATIONS = {event["name"]: event["duration"] for event in self.MINECRAFT_EVENTS}

        # Initialize RCON connection
        self._init_rcon(rcon_config)
        
        # Start command processor
        self.processor_thread = threading.Thread(
            target=self.process_commands,
            daemon=True,
        )
        self.processor_thread.start()

        # Add cleanup task attributes
        self.cleanup_task = None
        self.events_history = []
        
        # Start cleanup task
        self.cleanup_task = self.loop.create_task(self.periodic_cleanup())

        # Add server status checker
        self.status_task = self.loop.create_task(self.check_server_status())

        # Add player management
        self.player_count = min(ACTIVE_PLAYERS, len(PLAYER_NAMES))
        self.active_players = PLAYER_NAMES[:self.player_count]

    def _init_rcon(self, config):
        """Initialize RCON connection with retry logic."""
        self.rcon = None
        self.rcon_config = config
        self.rcon_connected = False
        self._connect_rcon()

    def _connect_rcon(self):
        """Attempt to connect to RCON with retries."""
        retries = 0
        while retries < RCON_MAX_RETRIES and not self.rcon_connected:
            try:
                self.rcon = mcrcon.MCRcon(
                    self.rcon_config["host"],
                    self.rcon_config["password"],
                    self.rcon_config["port"]
                )
                self.rcon.connect()
                self.rcon_connected = True
                print(f"{Colors.RCON}[RCON] Successfully connected to Minecraft server")
                # Test connection
                response = self.rcon.command("list")
                print(f"{Colors.RCON}[RCON] Server response: {response}")
            except Exception as e:
                retries += 1
                print(f"{Colors.RCON}[RCON] Connection attempt {retries} failed: {str(e)}")
                if retries < RCON_MAX_RETRIES:
                    print(f"{Colors.RCON}[RCON] Retrying in {RCON_RECONNECT_DELAY} seconds...")
                    time.sleep(RCON_RECONNECT_DELAY)
                else:
                    print(f"{Colors.RCON}[RCON] Maximum retries reached. Could not connect to server.")
                    raise

    def get_oauth_token(self, config):
        """Get OAuth token for Twitch authentication."""
        print(f"{Colors.OAUTH}[OAUTH] Starting OAuth flow...")
        auth_url = (
            f"https://id.twitch.tv/oauth2/authorize"
            f"?client_id={config['client_id']}"
            f"&redirect_uri={config['redirect_uri']}"
            f"&response_type=code"
            f"&scope=chat:read chat:edit"
        )
        print(f"{Colors.OAUTH}[OAUTH] Open this URL in your browser: {auth_url}")
        webbrowser.open(auth_url)

        # Start a local server to capture the authorization code
        code = self.start_local_server()
        print(f"{Colors.OAUTH}[OAUTH] Authorization code received: {code}")

        token_url = "https://id.twitch.tv/oauth2/token"
        payload = {
            "client_id": config["client_id"],
            "client_secret": config["client_secret"],
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": config["redirect_uri"],
        }
        response = requests.post(token_url, data=payload)
        if response.status_code == 200:
            token_data = response.json()
            print(f"{Colors.OAUTH}[OAUTH] Access token obtained successfully!")
            return token_data["access_token"]
        else:
            print(f"{Colors.ERROR}[OAUTH ERROR] Failed to obtain token: {response.json()}")
            raise Exception("OAuth token retrieval failed")

    def start_local_server(self):
        class OAuthHandler(http.server.BaseHTTPRequestHandler):
            authorization_code = None

            def do_GET(self):
                try:
                    # Parse the authorization code from the URL
                    if "code" in self.path:
                        query = self.path.split("?")[1]
                        params = dict(qc.split("=") for qc in query.split("&"))
                        OAuthHandler.authorization_code = params.get("code")
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(b"Authorization successful! You can close this window.")
                    else:
                        self.send_response(400)
                        self.end_headers()
                        self.wfile.write(b"Missing authorization code.")
                except ConnectionAbortedError:
                    print("[OAUTH] Connection aborted by the client.")
                except Exception as e:
                    print(f"[OAUTH ERROR] {e}")

        # Start the server in a separate thread
        with socketserver.TCPServer(("localhost", OAUTH_PORT), OAuthHandler) as httpd:
            print(f"[OAUTH] Waiting for authorization code on http://localhost:{OAUTH_PORT}...")
            server_thread = threading.Thread(target=httpd.serve_forever)
            server_thread.daemon = True
            server_thread.start()

            # Wait until the authorization code is received
            while OAuthHandler.authorization_code is None:
                time.sleep(1)

            httpd.shutdown()
            return OAuthHandler.authorization_code

    async def event_ready(self):
        print(f"{Colors.TWITCH}[TWITCH] Bot is ready! Logged in as {self.nick}")
        print(f"{Colors.TWITCH}[TWITCH] OAuth Token: {self.oauth_token}")

    async def event_message(self, message):
        if message.echo:
            return
        print(f"[CHAT] {message.author.name}: {message.content}")
        await self.handle_commands(message)

    def process_commands(self):
        """Enhanced command processor with reconnection logic."""
        print("[PROCESSOR] Command processor started")
        while True:
            if not self.rcon_queue.empty():
                cmd = self.rcon_queue.get()
                try:
                    if not self.rcon_connected:
                        print("[RCON] Connection lost, attempting to reconnect...")
                        self._connect_rcon()
                    
                    response = self.rcon.command(cmd)
                    print(f"[RCON] Executed: {cmd} | Response: {response}")
                    
                except (ConnectionRefusedError, ConnectionResetError, TimeoutError) as e:
                    print(f"[RCON] Connection error: {str(e)}")
                    self.rcon_connected = False
                    # Put the command back in queue
                    self.rcon_queue.put(cmd)
                    # Wait before retry
                    time.sleep(RCON_RECONNECT_DELAY)
                except Exception as e:
                    print(f"[RCON] Command failed: {str(e)}")
            time.sleep(COMMAND_DELAY)

    @commands.command(name="vote")
    async def vote(self, ctx, option: int):
        """Handle user votes with vote changing capability."""
        if not self.current_vote:
            await ctx.send("No active voting session. Please wait for the next vote!")
            return

        if option not in [1, 2, 3]:
            await ctx.send("Invalid vote! Please vote for 1, 2, or 3.")
            return

        user = ctx.author.name
        if user in self.votes:
            # If user voted before, subtract their old vote
            old_vote = self.votes[user]
            self.vote_counts[old_vote] -= 1

        # Record the user's new vote
        self.votes[user] = option
        self.vote_counts[option] += 1
        await ctx.send(f"{user} voted for option {option}!")
        print(f"{Colors.VOTE}[VOTING] {user} voted for option {option}")

        # Update the overlay state with vote counts
        try:
            percentages = self.calculate_vote_percentages()
            self.current_overlay_state = {
                "type": "update_vote",
                "options": [event["name"] for event in self.current_vote],
                "votes": list(self.vote_counts.values()),
                "percentages": percentages,
                "duration": self.voting_duration  # Add duration to help overlay sync
            }
            await self.update_overlay(self.current_overlay_state)
        except Exception as e:
            print(f"[ERROR] Failed to update overlay: {str(e)}")

    def calculate_vote_percentages(self):
        """Calculate the percentage of votes for each option."""
        total_votes = sum(self.vote_counts.values())
        if total_votes == 0:
            return [0, 0, 0]  # Return 0% for all options if no votes
        return [round((self.vote_counts[i] / total_votes) * 100, 2) for i in range(1, 4)]

    def start_voting(self, auto=True, voting_time=None):
        """Start a new voting session."""
        try:
            # Cancel any existing timer
            if self.voting_timer:
                self.voting_timer.cancel()
                self.voting_timer = None
            
            self.auto_vote = auto
            if voting_time:
                self.voting_duration = voting_time

            # Reset voting state with full event configs
            available_events = self.MINECRAFT_EVENTS
            self.current_vote = random.sample(available_events, 3)
            self.votes = {}
            self.vote_counts = {1: 0, 2: 0, 3: 0}

            # Update overlay state first
            self.current_overlay_state = {
                "type": "start_vote",
                "options": [event["name"] for event in self.current_vote],
                "votes": [0, 0, 0],
                "percentages": [0, 0, 0],
                "duration": self.voting_duration,
                "events": [
                    {"name": event["name"], "duration": event["duration"]}
                    for event in self.current_vote
                ],
            }

            # Send updates
            if self.loop and self.loop.is_running():
                asyncio.create_task(self.update_overlay(self.current_overlay_state))
                asyncio.create_task(self.update_overlay({"type": "reset_timer"}))

            # Announce options
            options = "\n".join([f"{i + 1}. {event['name']}" for i, event in enumerate(self.current_vote)])
            self.rcon_queue.put(f"say Voting started! Use !vote (1-3) to vote for an event:\n{options}")
            print(f"{Colors.VOTE}[VOTING] Voting started:\n{options}")

            # Schedule timer
            if self.loop and self.loop.is_running():
                self.voting_timer = self.loop.call_later(
                    self.voting_duration,
                    lambda: asyncio.create_task(self.end_voting())
                )

        except Exception as e:
            print(f"[ERROR] Error in start_voting: {str(e)}")

    async def execute_commands(self, commands):
        """Execute commands for offline and online players."""
        for cmd in commands:
            if cmd["delay"] > 0:
                await asyncio.sleep(0.05)  # Reduced from default delay to 50ms

            # Modify command to work with any number of players
            command = cmd["cmd"]
            # Replace specific player targeting with all players
            command = command.replace("{player}", "@a")
            command = command.replace("@p", "@a")
            
            # Execute command
            self.rcon_queue.put(command)
            await asyncio.sleep(0.02)  # Reduced from 0.1s to 20ms delay between commands

    async def end_voting(self):
        """End current voting session and execute winning event."""
        if not self.current_vote:
            return

        try:
            # Store current vote state before clearing
            stored_vote = self.current_vote.copy()
            stored_counts = self.vote_counts.copy()

            # Start new vote BEFORE executing commands to minimize delay
            if self.auto_vote:
                print(f"{Colors.VOTE}[VOTING] Auto-vote is enabled. Starting a new voting session...")
                self.start_voting()

            # Determine the winning event
            max_votes = max(stored_counts.values())
            winning_options = [i for i, v in stored_counts.items() if v == max_votes]
            winning_option = random.choice(winning_options)
            winning_event = stored_vote[winning_option - 1]

            # Update overlay with winner and execute commands
            self.current_overlay_state = {
                "type": "end_vote",
                "winner": winning_event["name"],
                "duration": winning_event["duration"]
            }
            await self.update_overlay(self.current_overlay_state)

            # Execute commands
            await self.execute_commands(winning_event["commands"])
            self.rcon_queue.put(f"say Voting ended! The winning event is: {winning_event['name']}")
            print(f"{Colors.VOTE}[VOTING] Voting ended. Winning event: {winning_event['name']}")

        except Exception as e:
            print(f"{Colors.ERROR}[ERROR] Error in end_voting: {str(e)}")
            self.current_vote = None

    def stop_voting(self):
        """Stop and reset the current voting session."""
        try:
            # Cancel timer first
            if self.voting_timer:
                self.voting_timer.cancel()
                self.voting_timer = None

            # Update overlay synchronously to prevent thread issues
            self.current_overlay_state = {"type": "stop_timer"}
            if self.loop and self.loop.is_running():
                async def update():
                    await self.update_overlay(self.current_overlay_state)
                future = asyncio.run_coroutine_threadsafe(update(), self.loop)
                try:
                    future.result(timeout=1.0)
                except Exception as e:
                    print(f"{Colors.ERROR}[ERROR] Failed to update overlay: {e}")

            # Clear voting state
            self.current_vote = None
            self.votes.clear()
            self.vote_counts = {1: 0, 2: 0, 3: 0}

        except Exception as e:
            print(f"{Colors.ERROR}[ERROR] Error in stop_voting: {str(e)}")
            # Force reset state even if error occurs
            self.voting_timer = None
            self.current_vote = None
            self.votes.clear()
            self.vote_counts = {1: 0, 2: 0, 3: 0}

    async def start_overlay_server(self):
        """Optimized overlay server with better error handling."""
        self.overlay_server_running = True
        try:
            self.websocket_server = await websockets.serve(
                self.overlay_handler, 
                "localhost", 
                WEBSOCKET_PORT,
                ping_interval=20,
                ping_timeout=60
            )
            print(f"{Colors.OVERLAY}[OVERLAY] WebSocket server started on ws://localhost:{WEBSOCKET_PORT}")
            await self.websocket_server.wait_closed()
        except asyncio.CancelledError:
            print("[OVERLAY] WebSocket server stopped gracefully.")
        except Exception as e:
            print(f"[OVERLAY] Server error: {str(e)}")
        finally:
            self.overlay_server_running = False

    async def overlay_handler(self, websocket):
        """Enhanced WebSocket connection handler with proper state checks."""
        try:
            self.overlay_clients.add(websocket)
            print(f"{Colors.OVERLAY}[OVERLAY] Client connected")

            # Send current state if available
            if self.current_overlay_state:
                try:
                    await websocket.send(json.dumps(self.current_overlay_state))
                    print(f"{Colors.OVERLAY}[OVERLAY] Sent current state to new client")
                except Exception as e:
                    print(f"[OVERLAY] Error sending initial state: {str(e)}")
                    return  # Exit if we can't send initial state

            # Keep connection alive and handle messages
            async for message in websocket:
                if not websocket.open:
                    break
                print(f"[OVERLAY] Received message: {message}")

        except websockets.exceptions.ConnectionClosed:
            print("[OVERLAY] Client connection closed normally")
        except Exception as e:
            print(f"[OVERLAY] Client error: {str(e)}")
        finally:
            if websocket in self.overlay_clients:
                self.overlay_clients.remove(websocket)
                print(f"{Colors.OVERLAY}[OVERLAY] Client disconnected")

    async def update_overlay(self, data):
        """Improved overlay update with proper connection checks."""
        if not self.overlay_clients:
            return

        try:
            message = json.dumps(data)
            dead_clients = set()

            for client in self.overlay_clients:
                try:
                    # Only consider a client dead if we can't send to it
                    await client.send(message)
                except Exception as e:
                    print(f"[OVERLAY] Error sending to client: {str(e)}")
                    dead_clients.add(client)

            # Only remove clients that failed to receive messages
            if dead_clients:
                self.overlay_clients.difference_update(dead_clients)
                print(f"[OVERLAY] Removed {len(dead_clients)} disconnected client(s)")
        except Exception as e:
            print(f"[OVERLAY] Update failed: {str(e)}")

    async def periodic_cleanup(self):
        """Periodic cleanup of dead connections and resources."""
        while True:
            try:
                # Only trim events history, don't touch overlay clients
                if len(self.events_history) > MAX_EVENTS_HISTORY:
                    self.events_history = self.events_history[-MAX_EVENTS_HISTORY:]
                    print(f"{Colors.CLEANUP}[CLEANUP] Trimmed events history")

                await asyncio.sleep(CLEANUP_INTERVAL)
            except Exception as e:
                print(f"[ERROR] Cleanup error: {str(e)}")
                await asyncio.sleep(CLEANUP_INTERVAL)

    def is_whitelisted(self, username):
        """Check if a user is in the whitelist."""
        # Convert username to lowercase for case-insensitive comparison
        return username.lower() in [name.lower() for name in self.whitelist]

    @commands.command(name="startvote")
    async def start_vote_command(self, ctx, *args):
        """Start a new voting session with configurable options."""
        if not self.is_whitelisted(ctx.author.name):
            await ctx.send(f"Sorry {ctx.author.name}, you are not authorized to use this command.")
            return

        if self.current_vote:
            await ctx.send("A voting session is already active!")
            return

        # Parse arguments for auto and voting-time
        auto = True
        voting_time = None
        for arg in args:
            if arg.startswith("auto="):
                auto = arg.split("=")[1].lower() == "true"
            elif arg.startswith("voting_time=") or arg.startswith("time="):
                try:
                    voting_time = int(arg.split("=")[1])
                except ValueError:
                    await ctx.send("Invalid voting_time value. It must be an integer.")
                    return

        # Start the voting session with the specified options
        self.start_voting(auto=auto, voting_time=voting_time)
        await ctx.send(f"Voting session started! Auto-vote: {auto}, Voting time: {self.voting_duration} seconds.")
        print(f"{Colors.VOTE}[VOTING] Voting session started with auto={auto}, voting_time={self.voting_duration} seconds.")

    @commands.command(name="stopvote")
    async def stop_vote_command(self, ctx):
        """Stop the current voting session."""
        if not self.is_whitelisted(ctx.author.name):
            await ctx.send(f"Sorry {ctx.author.name}, you are not authorized to use this command.")
            return

        if not self.current_vote:
            await ctx.send("No active voting session to stop.")
            return

        # Safely stop the voting
        self.stop_voting()
        self.rcon_queue.put("say Voting session has been stopped.")
        print("[VOTING] Voting session manually stopped.")

        # Update overlay
        self.current_overlay_state = {"type": "stop_timer"}
        if self.loop.is_running():
            asyncio.run_coroutine_threadsafe(
                self.update_overlay(self.current_overlay_state),
                self.loop
            )

        await ctx.send("Voting session has been stopped.")

    @commands.command(name="setvotingtime")
    async def set_voting_time(self, ctx, seconds: int):
        """Command to set the voting duration."""
        if not self.is_whitelisted(ctx.author.name):
            await ctx.send(f"Sorry {ctx.author.name}, you are not authorized to use this command.")
            return

        # Rest of set_voting_time method
        self.voting_duration = seconds
        await ctx.send(f"Voting duration set to {seconds} seconds.")
        print(f"{Colors.VOTE}[VOTING] Voting duration set to {seconds} seconds.")

    @commands.command(name="vote-skip")
    async def vote_skip_command(self, ctx):
        """Command to skip the current voting process."""
        if not self.is_whitelisted(ctx.author.name):
            await ctx.send(f"Sorry {ctx.author.name}, you are not authorized to use this command.")
            return

        # Rest of vote_skip_command method
        if not self.current_vote:
            await ctx.send("No active voting session to skip.")
            return

        await self.end_voting()
        await ctx.send("Current voting session has been skipped.")
        print("[VOTING] Current voting session has been skipped.")

    def refresh_oauth_token(self):
        """Refresh OAuth token when needed."""
        try:
            token_url = "https://id.twitch.tv/oauth2/token"
            payload = {
                "client_id": self.twitch_config["client_id"],
                "client_secret": self.twitch_config["client_secret"],
                "grant_type": "refresh_token",
                "refresh_token": self.oauth_token
            }
            response = requests.post(token_url, data=payload)
            if response.status_code == 200:
                self.oauth_token = response.json()["access_token"]
                print(f"{Colors.OAUTH}[OAUTH] Token refreshed successfully")
            else:
                print(f"{Colors.ERROR}[OAUTH ERROR] Failed to refresh token: {response.json()}")
        except Exception as e:
            print(f"{Colors.ERROR}[OAUTH ERROR] Error refreshing token: {str(e)}")

    async def close(self):
        """Enhanced cleanup with proper WebSocket and event loop handling."""
        try:
            # Cancel all tasks first
            if self.voting_timer:
                self.voting_timer.cancel()
            if self.overlay_server_task:
                self.overlay_server_task.cancel()
            if self.cleanup_task:
                self.cleanup_task.cancel()
            if hasattr(self, 'status_task'):
                self.status_task.cancel()
            
            # Close WebSocket server if it exists
            if hasattr(self, 'websocket_server'):
                self.websocket_server.close()
                await self.websocket_server.wait_closed()
            
            # Close all websocket connections properly
            if self.overlay_clients:
                close_tasks = []
                for client in list(self.overlay_clients):
                    try:
                        if not client.closed:
                            close_tasks.append(client.close())
                    except Exception:
                        pass
                if close_tasks:
                    await asyncio.gather(*close_tasks, return_exceptions=True)
                self.overlay_clients.clear()

            # Clean up other resources
            self.events_history.clear()
            
            if hasattr(self, 'rcon') and self.rcon:
                try:
                    self.rcon.disconnect()
                except:
                    pass
                self.rcon = None
                self.rcon_connected = False

            # Call parent's close method
            await super().close()
            
        except Exception as e:
            print(f"[ERROR] Error during cleanup: {str(e)}")

    async def check_server_status(self):
        """Simplified server status check without player checks."""
        while True:
            try:
                if self.rcon_connected:
                    self.rcon.command("list")  # Just check connection
            except Exception as e:
                print(f"[SERVER] Connection error: {str(e)}")
                self.rcon_connected = False
            await asyncio.sleep(30)  # Check every 30 seconds

# Main entry point
if __name__ == "__main__":
    print(f"{Colors.SYSTEM}[SYSTEM] Starting Minecraft-Twitch integration bot")
    
    bot = VotingSystem(RCON_CONFIG, TWITCH_CONFIG)
    try:
        # Start overlay server in the bot's event loop
        bot.overlay_server_task = bot.loop.create_task(bot.start_overlay_server())
        bot.run()
    except KeyboardInterrupt:
        print("\n[SYSTEM] Shutting down gracefully...")
        # Run cleanup in a new event loop
        cleanup_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(cleanup_loop)
        cleanup_loop.run_until_complete(bot.close())
        cleanup_loop.close()
        sys.exit(0)
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        sys.exit(1)
