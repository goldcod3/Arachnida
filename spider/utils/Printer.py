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
    def __init__(self, silent=False, logger=None):
        self.silent = silent
        self.log = logger

    def setSilent(self, silent):
        self.silent = silent

    def setLogger(self, logger):
        self.log = logger

    # Info message function
    def messageInfo(self, msg, title='[INFO]: ', time=0):
        if self.silent == False:
            print(Printer.BLUE + title + Printer.ENDC + msg)
        if self.log != None:
            self.log.info(msg)
        sleep(time)

    # Success message function
    def messageOk(self, msg, title='[OK]: ', time=0):
        if self.silent == False:
            print(Printer.GREEN_L + title + Printer.ENDC + msg)
        if self.log != None:
            self.log.info(msg)
        sleep(time)

    # Success message function
    def messageScan(self, msg, title='[SCAN]: ', time=0):
        if self.silent == False:
            print(Printer.GREEN_L + title + Printer.ENDC + msg)
        if self.log != None:
            self.log.info(title+msg)
        sleep(time)
        
    # Warning message function
    def messageWarning(self, msg, title='[WARNING]: ', time=0):
        if self.silent == False:
            print(Printer.YELLOW + title + Printer.ENDC + msg)
        if self.log != None:
            self.log.warning(msg)
        sleep(time)
        
    # Error message function
    def messageError(self, msg, title='[ERROR]: ', time=0):
        if self.silent == False:
            print(Printer.RED + title + Printer.ENDC + msg)
        if self.log != None:
            self.log.error(msg)
        sleep(time)
        
    # Banner message function
    def printBanner(self, msg):
        if self.silent == False:
            system('clear')
            print(Printer.GREEN_D + Printer.BANNER + Printer.YELLOW + Printer.AUTHOR + Printer.ENDC)
            print('\n\n')
            initBar = tqdm(range(100),msg)
            for i in initBar:
                sleep(0.02)
            print('\n\n')

    # Function that checks request status codes
    def check_status_code(self, url, code, description):
        if code in range(100,199):
            self.messageError('STATUS CODE [{} - {}] - Informative server response. --> {}'.format(code,description,url), '[->][ERROR]: ')
        if code in range(201,299):
            self.messageError('STATUS CODE [{} - {}] - Successfull server response. --> {}'.format(code,description,url), '[->][ERROR]: ')
        if code in range(300,399):
            self.messageError('STATUS CODE [{} - {}] - Redirection detected on server. --> {}'.format(code,description,url),  '[->][ERROR]: ')
        if code in range(400,499):
            self.messageError('STATUS CODE [{} - {}] - Client error detected. --> {}'.format(code,description,url),  '[->][ERROR]: ')
        if code in range(500,599):
            self.messageError('STATUS CODE [{} - {}] - Server error detected. --> {}'.format(code,description,url),  '[->][ERROR]: ')

