import requests
from os.path import abspath, exists
from os import getcwd, mkdir

from Printer import *

class Scraper:

    def __init__(self, scanner):
        self.resources = scanner.imgs
        self.total_imgs = scanner.total_img
        self.process = list()
        self.total_proc = 0

    def getContent(self, target):
        pass

    def getResources(self):
        pass

def getNameImg(target):
    pass

def checkPath(path):
    try:
        while exists(path) == False:
            mkdir(path)
        with open(path+'/'+'.fill','w') as fill:
            fill.write('')
        return True
    except:
        return False

def getDefaultPath():
    current_path = abspath(getcwd())
    spl_current = current_path.replace('/',' ').split()
    default = ''
    for i in range(0,(len(spl_current)-2)):
        default = default + '/' +spl_current[i]
    return default + '/data'

data_path = getDefaultPath()
print(data_path)
print(checkPath(data_path))