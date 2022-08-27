from posixpath import splitext
from sys import argv
from time import sleep
from os import system, listdir
from os.path import isfile, isdir

from utils.MetadataImage import *
from utils.MetadataFile import *

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

# Default extensions files
default_images = ('.png','.jpg','.jpeg','.gif','.bmp')
default_files = ('.docx','.pdf')

# Main function
def run_scorpion(args):
    if len(args) > 1:
        # Option directory mode
        if args[1] == '-d' or args[1] == '--directory':
            try:
                path = args[2]
                if isdir(path):
                    counter = 0
                    for resource in listdir(path):
                        res = path+'/'+resource
                        type = getTypeResource(res)
                        if type == 'image':
                            meta_img = MetadataImage(res)
                            meta_img.getMetadata()
                            counter +=1
                        elif type == 'file':
                            meta_file = MetadataFile(res)
                            meta_file.getMetadata()
                            counter +=1
                        else:
                            print('\033[0;91m'+'    [ERROR]'+'\033[0m'+': Invalid file or file path.')
                        sleep(1)
                    if counter > 0:
                        print('\033[0;34m'+' [TOTAL RESOURCES PROCESSED]'+'\033[0m'+': {}'.format(counter)+'\n')
                    else:
                        print('\033[0;91m'+'    [ERROR]'+'\033[0m'+' Files not found in the directory path!')   
                else:
                    raise Exception
            except:
                print('\033[0;91m'+'    [ERROR]'+'\033[0m'+' Invalid directory path!')
        # Option help mode
        elif args[1] == '-h' or args[1] == '--help':
            print('\033[0;34m'+BANNER+'\033[0;93m'+AUTHOR+'\033[0m'+'\n')
            print("""
usage: scorpion FILE1 FILE2 ...
       scorpion -d <DIRECTORY PATH>

*** Arachnida - Scorpion *** File metadata display - Get metadata for images, docx and pdf.

options: 
    -d <PATH>, --directory <PATH> Get metadata of the files in a directory.""")
        # Option file mode
        else:
            system('clear')
            print('\033[0;34m'+BANNER+'\033[0;93m'+AUTHOR+'\033[0m'+'\n')
            for path in args[1:]:
                type = getTypeResource(path)
                if type == 'image':
                    meta_img = MetadataImage(path)
                    meta_img.getMetadata()
                elif type == 'file':
                    meta_file = MetadataFile(path)
                    meta_file.getMetadata()
                else:
                    print('\033[0;91m'+'    [ERROR]'+'\033[0m'+': Invalid file or file path.')
                sleep(1)

    else:
        print('\033[0;91m'+'    [ERROR]'+'\033[0m'+' Run "scorpion -h" for help!')

# Function that returns the type of file to be analyzed
def getTypeResource(path):
    if isfile(path):
        name, ext = splitext(path)
        if ext in default_images:
            return 'image'
        if ext in default_files:
            return 'file'
    return None

# Run main function
if __name__=='__main__':
    run_scorpion(argv)