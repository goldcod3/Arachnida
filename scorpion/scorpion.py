from posixpath import splitext
from sys import argv
from time import sleep
from os import system
from os.path import isfile, isdir

from utils.MetadataImage import *

# Banner
BANNER = """
             ______        _____           _____         _____        _____    ____         _____    
         ___|\     \   ___|\    \     ____|\    \    ___|\    \   ___|\    \  |    |   ____|\    \   
        |    |\     \ /    /\    \   /     /\    \  |    |\    \ |    |\    \ |    |  /     /\    \  
        |    |/____/||    |  |    | /     /  \    \ |    | |    ||    | |    ||    | /     /  \    \ 
     ___|    \|   | ||    |  |____||     |    |    ||    |/____/ |    |/____/||    ||     |    |    |
    |    \    \___|/ |    |   ____ |     |    |    ||    |\    \ |    ||    |||    ||     |    |    |
    |    |\     \    |    |  |    ||\     \  /    /||    | |    ||    ||____|/|    ||\     \  /    /|
    |\ ___\|_____|   |\ ___\/    /|| \_____\/____/ ||____| |____||____|       |____|| \_____\/____/ |
    | |    |     |   | |   /____/ | \ |    ||    | /|    | |    ||    |       |    | \ |    ||    | /
     \|____|_____|    \|___|    | /  \|____||____|/ |____| |____||____|       |____|  \|____||____|/ 
                           |____|/    """
# Author
AUTHOR = 'github.com/goldcod3'

default_images = ('.png','.jpg','.jpeg','.gif','.bmp')
default_files = ('.docx','.pdf')

def run_scorpion(args):
    if len(args) > 1:
        if args[1] == '-d' or args[1] == '--directory':
            if args[2]:
                print(args[2]) # Falta
            else:
                print('\033[0;91m'+'    [ERROR]'+'\033[0m'+' Set a directory path!')
        elif args[1] == '-h' or args[1] == '--help':
            print('\033[0;34m'+BANNER+'\033[0;93m'+AUTHOR+'\033[0m'+'\n')
            print("""
usage: scorpion FILE1 FILE2 ...
       scorpion -d <DIRECTORY PATH>

*** Arachnida - Scorpion *** File metadata display - Get metadata for images, docx and pdf.

options: 
    -d <PATH>, --directory <PATH> Get metadata of the files in a directory.""")
        else:
            system('clear')
            print('\033[0;34m'+BANNER+'\033[0;93m'+AUTHOR+'\033[0m'+'\n')
            for path in args[1:]:
                type = getTypeFile(path)
                if type == 'image':
                    meta_img = MetadataImage(path)
                    meta_img.getMetadata()
                sleep(1)

    else:
        print('\033[0;91m'+'    [ERROR]'+'\033[0m'+' Run "scorpion -h" for help!')

def getTypeFile(path):
    if isfile(path):
        name, ext = splitext(path)
        if ext in default_images:
            return 'image'
        if ext in default_files:
            return 'file'
    return None


if __name__=='__main__':
    run_scorpion(argv)