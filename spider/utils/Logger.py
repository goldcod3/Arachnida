from datetime import datetime
from time import time
from os.path import abspath, exists
from os import getcwd, mkdir

class Logger:

    def __init__(self, name, type):
        self.path = getLogsPath()
        timelog = getDateLog()
        self.namefile = type+'_'+name+'_'+timelog
        self.logfile = self.path+'/'+self.namefile
        self.createLogFile()

    def createLogFile(self):
        if exists(self.logfile) == False:
            with open(self.logfile,'w') as logFile:
                logFile.write('')

    def messageLog(self, msg=''):
        if exists(self.logfile):
            with open(self.logfile,'a') as logFile:
                logFile.write(msg+'\n')

    def title(self, title):
        self.messageLog('\n\n'+title+'\n\n')

    def text(self, text):
        self.messageLog(text)

    def info(self, msg):
        self.messageLog('[INFO]: '+msg)

    def debug(self, msg):
        self.messageLog('[DEBUG]: '+msg)

    def scan(self, msg):
        self.messageLog('[SCAN]: '+msg)

    def warning(self, msg):
        self.messageLog('[WARNING]: '+msg)

    def error(self, msg):
        self.messageLog('[ERROR]: '+msg)


def getDateLog():
        format_date = '%Y%m%d-%H%M%S'
        time_ = datetime.utcfromtimestamp(time())
        return datetime.strftime(time_, format_date)

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
