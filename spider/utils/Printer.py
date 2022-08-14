from tqdm import tqdm
from os import system
from time import sleep

class Printer:
    
    # Palet of colors message
    GREEN_D = '\033[0;32m'
    GREEN_L = '\033[0;92m'
    BLUE = '\033[0;34m'
    YELLOW = '\033[0;93m'
    RED = '\033[0;91m'
    CURSI = '\033[3m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

    # Banner
    BANNER = """
             ______       _____    ____      _____        ______        _____   
         ___|\     \  ___|\    \  |    | ___|\    \   ___|\     \   ___|\    \  
        |    |\     \|    |\    \ |    ||    |\    \ |     \     \ |    |\    \ 
        |    |/____/||    | |    ||    ||    | |    ||      _____/||    | |    |
     ___|    \|   | ||    |/____/||    ||    | |    ||     \   \_|/|    |/____/ 
    |    \    \___|/ |    ||    |||    ||    | |    ||     /___/|  |    |\    \ 
    |    |\     \    |    ||____|/|    ||    | |    ||     \____|\ |    | |    |
    |\ ___\|_____|   |____|       |____||____|/____/||____       /||____| |____|
    | |    |     |   |    |       |    ||    /    | ||    /_____/ ||    | |    |
     \|____|_____|   |____|       |____||____|____|/ |____|     | /|____| |____|
                                                          |_____|/  """
    # Author
    AUTHOR = 'github.com/goldcod3'

    # Constructor of Printer
    def __init__(self):
        pass

    # Info message function
    def messageInfo(self, msg, title='[INFO]: '):
        print(Printer.BLUE + title + Printer.ENDC + msg)

    # Success message function
    def messageOk(self, msg, title='[OK]: '):
        print(Printer.GREEN_L + title + Printer.ENDC + msg)

    # Warning message function
    def messageWarning(self, msg, title='[WARNING]: '):
        print(Printer.YELLOW + title + Printer.ENDC + msg)

    # Error message function
    def messageError(self, msg, title='[ERROR]: '):
        print(Printer.RED + title + Printer.ENDC + msg)

    # Banner message function
    def printBanner(self, msg):
        system('clear')
        print(Printer.GREEN_D + Printer.BANNER + Printer.YELLOW + Printer.AUTHOR + Printer.ENDC)
        print('\n\n')
        initBar = tqdm(range(100),msg)
        for i in initBar:
            sleep(0.02)
        print('\n\n')

        