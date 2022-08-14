import logging
from datetime import datetime
from time import time
from os.path import abspath, exists
from os import getcwd, mkdir


class Logger:

    def __init__(self, name, path=None):
        if path == None:
            path = getDefaultPath()
        self.path = path
        if checkPath(path):
            name = path+'/'+name
        self.name = name
        logging.basicConfig(filename=self.name, level='DEBUG')

    def info(self, msg):
        logging.basicConfig(filename=self.name, level='DEBUG')
        logging.info(msg)

    def debug(self, msg):
        logging.basicConfig(filename=self.name, level='DEBUG')
        logging.debug(msg)

    def warning(self, msg):
        logging.basicConfig(filename=self.name, level='DEBUG')
        logging.warning(msg)

    def error(self, msg):
        logging.basicConfig(filename=self.name, level='DEBUG')
        logging.error(msg)

def getNameDir(url):
        format_date = '%Y-%m-%d-%H-%M-%S'
        time_ = datetime.utcfromtimestamp(time())
        time_str = datetime.strftime(time_, format_date)
        return time_str+'_'+url

def checkPath(path):
    try:
        while exists(path) == False:
            mkdir(path)
        return True
    except:
        return False

def getDefaultPath():
    current_path = abspath(getcwd())
    spl_current = current_path.replace('/',' ').split()
    default = ''
    for i in range(0,(len(spl_current)-1)):
        default = default + '/' +spl_current[i]
    return default + '/data'
