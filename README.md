# Minecraft-Twitch Integration Bot

A Python bot that integrates Twitch chat voting with Minecraft server commands, allowing viewers to vote on random events that affect gameplay.

## Features

- Twitch chat voting system
- Real-time overlay for OBS
- Automated event execution
- Support for both RCON and Bedrock servers
- 65+ unique Minecraft events

## Prerequisites

- Python 3.8 or higher
- Minecraft Server (Java or Bedrock)
- Twitch Account
- OBS (for overlay)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Twich-Rcon-script.git
cd Twich-Rcon-script
```

2. Install required Python packages:
```bash
pip install mcrcon twitchio colorama websockets requests
```

## Configuration

1. Edit the Twitch configuration in `rcon.py`:
```python
TWITCH_CONFIG = {
    "channel": "your_channel",
    "bot_username": "your_bot_name",
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "redirect_uri": "http://localhost:8080",
    "whitelist": ["your_channel", "trusted_user1", "trusted_user2"]
}
```

2. Set your server configuration:
```python
# For Java servers using RCON:
RCON_CONFIG = {
    "type": "rcon",
    "host": "your_server_ip",
    "password": "your_rcon_password",
    "port": 25575  # Default RCON port
}

# For Bedrock servers:
BEDROCK_CONFIG = {
    "type": "bedrock",
    "host": "your_server_ip",
    "port": 19132,
    "username": "bot_username"
}
```

## Usage

1. Start the bot:
```bash
python rcon.py
```

2. Add the overlay to OBS:
- Add a new Browser Source
- Set URL to `file:///path/to/overlay.html`
- Set width: 1920 and height: 1080
- Check "Custom CSS" and add:
```css
body { background-color: rgba(0, 0, 0, 0); margin: 0px auto; overflow: hidden; }
```

### Twitch Commands

- `!vote <1-3>` - Vote for an event (all viewers)
- `!startvote` - Start a new voting session (whitelisted users)
- `!stopvote` - Stop current voting session (whitelisted users)
- `!setvotingtime <seconds>` - Set voting duration (whitelisted users)
- `!vote-skip` - Skip current voting session (whitelisted users)

## Customization

- Edit events in `events.py` to add/modify Minecraft events
- Modify overlay appearance in `overlay.html`
- Adjust voting duration and other settings in `rcon.py`

## Troubleshooting

1. Connection Issues:
- Verify server IP and port
- Check RCON password
- Ensure server has RCON enabled (for Java) or allows external connections (for Bedrock)

2. Twitch Auth Issues:
- Verify client ID and secret
- Make sure your redirect URI matches Twitch developer settings
- Try refreshing OAuth token

3. Overlay Not Working:
- Check if WebSocket server is running (port 8765)
- Verify OBS browser source settings
- Try refreshing browser cache

## License

MIT License - feel free to modify and use as needed!

## Support

If you encounter any issues or need help, please open an issue on GitHub.

