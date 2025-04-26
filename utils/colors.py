from colorama import init, Fore, Back, Style

init(autoreset=True)

class Colors:
    SYSTEM = Fore.CYAN
    ERROR = Fore.RED + Style.BRIGHT
    WARNING = Fore.YELLOW
    SUCCESS = Fore.GREEN
    INFO = Fore.WHITE
    VOTE = Fore.MAGENTA
    RCON = Fore.BLUE
    OAUTH = Fore.YELLOW + Style.BRIGHT
    CLEANUP = Fore.CYAN
    OVERLAY = Fore.GREEN + Style.BRIGHT
    TWITCH = Fore.MAGENTA + Style.BRIGHT
