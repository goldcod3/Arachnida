from datetime import datetime
from time import time
from os.path import abspath, exists
from os import getcwd, mkdir

class Logger:

    # Constructor of Logger
    def __init__(self, name, type):
        self.path = getLogsPath()
        timelog = getDateLog()
        self.namefile = type+'_'+name+'_'+timelog
        self.logfile = self.path+'/'+self.namefile
        self.createLogFile()

    # Function that creates a log file
    def createLogFile(self):
        if exists(self.logfile) == False:
            with open(self.logfile,'w') as logFile:
                logFile.write('')

    # Function that adds a message to the log file
    def messageLog(self, msg=''):
        if exists(self.logfile):
            with open(self.logfile,'a') as logFile:
                logFile.write(msg+'\n')

    # Title message function
    def title(self, title):
        self.messageLog('\n\n'+title+'\n\n')

    # Text message function
    def text(self, text):
        self.messageLog(text)

    # Info message function
    def info(self, msg):
        self.messageLog('[INFO]: '+msg)

    # Debug message function
    def debug(self, msg):
        self.messageLog('[DEBUG]: '+msg)

    # Scan message function
    def scan(self, msg):
        self.messageLog('[SCAN]: '+msg)

    # Warning message function
    def warning(self, msg):
        self.messageLog('[WARNING]: '+msg)

    # Error message function
    def error(self, msg):
        self.messageLog('[ERROR]: '+msg)

# Function that return a format time for log file
def getDateLog():
        format_date = '%Y%m%d-%H%M%S'
        time_ = datetime.utcfromtimestamp(time())
        return datetime.strftime(time_, format_date)

# Function that return a default path for log files
def getLogsPath():
    current_path = abspath(getcwd())
    spl_current = current_path.replace('/',' ').split()
    default = ''
    for i in range(0,(len(spl_current)-1)):
        default = default + '/' +spl_current[i]
    logpath = default + '/logs'
    while exists(logpath) == False:
            mkdir(logpath)
    return logpath
