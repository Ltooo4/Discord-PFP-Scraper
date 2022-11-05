import ctypes
from colorama import Fore
import pystyle
from pystyle import Colorate, Center

class Colors:
    purple = Fore.LIGHTMAGENTA_EX
    white = Fore.LIGHTWHITE_EX
    blue = Fore.LIGHTBLUE_EX
    green = Fore.LIGHTGREEN_EX
    red = Fore.LIGHTRED_EX
    cyan = Fore.LIGHTCYAN_EX
    yellow = Fore.LIGHTYELLOW_EX

logo = Colorate.Vertical(pystyle.Colors.blue_to_white, Center.XCenter("""

 ██▓███    █████▒██▓███       ██████  ▄████▄   ██▀███   ▄▄▄       ██▓███  ▓█████  ██▀███      ██▓  ▄▄▄█████▓
▓██░  ██▒▓██   ▒▓██░  ██▒   ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒   ▓██▒  ▓  ██▒ ▓▒
▓██░ ██▓▒▒████ ░▓██░ ██▓▒   ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒   ▒██░  ▒ ▓██░ ▒░
▒██▄█▓▒ ▒░▓█▒  ░▒██▄█▓▒ ▒     ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄     ▒██░  ░ ▓██▓ ░ 
▒██▒ ░  ░░▒█░   ▒██▒ ░  ░   ▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒   ░██████▒▒██▒ ░ 
▒▓▒░ ░  ░ ▒ ░   ▒▓▒░ ░  ░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▒░▓  ░▒ ░░   
░▒ ░      ░     ░▒ ░        ░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░   ░ ░ ▒  ░  ░    
░░        ░ ░   ░░          ░  ░  ░  ░          ░░   ░   ░   ▒   ░░          ░     ░░   ░      ░ ░   ░      
                                  ░  ░ ░         ░           ░  ░            ░  ░   ░            ░  ░       
                                     ░                                                                      
                        
                       ⌜――――――――――――――――――――――――――――――――――――――――――――――――――――⌝
                               [Discord] lto4#0207                        
                               [Github]  https://github.com/Ltooo4         
                       ⌞――――――――――――――――――――――――――――――――――――――――――――――――――――⌟
"""))

def log(s):
    print(f"{Colors.blue}[{Colors.purple}LT Scraper{Colors.blue}]{Colors.white} {s}")

def title(text):
    ctypes.windll.kernel32.SetConsoleTitleW(text)