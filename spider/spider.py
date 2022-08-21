from os.path import abspath, exists
from os import getcwd, mkdir
from utils.args import config_args
from utils.Scanner import *
from utils.Scraper import *

# Main function
def run_spyder():
    args = config_args()
    printer = Printer(silent=args.silent)
    # Recursive Scraper Mode
    if args.recursive != None and args.file == None:
        # Url validation
        url_scan = checkHttpUrl(args.recursive)
        # Level validation
        lvl_scan = 5
        if args.level != None:
            if checkNumLevel(args.level):
                lvl_scan = int(args.level)
            else:            
                printer.messageError(msg=' Invalid value of level, default value [5] charged!', time=2)
        # Path validation
        path_scan = getDefaultDataPath()
        if args.path != None:
            if exists(args.path):
                path_scan = args.path
            else:
                printer.messageError(msg='Invalid value of path, default path [../data] charged.')
                printer.messageWarning(msg=' Try with \'/home/$(user)/path\'.', time=2)
        checkDataPath(path_scan)
        # Stating scanner
        scan = Scanner(url=url_scan, depth=lvl_scan)
        scan.depthScan(args.silent)
        # Starting scraper
        scrap = Scraper(scan.parse_url.netloc, path_scan)
        scrap.scrapResources(scan.resources, silent=args.silent)

    # File Scraper Mode
    if args.recursive == None and args.file != None:
        path_scan = getDefaultDataPath()
        checkDataPath(path_scan)
        url_res = checkHttpUrl(args.file)
        # Starting scraper
        scrp = Scraper(url_res, path_scan)
        scrp.scrapResourceFromUrl(silent=args.silent)

# Function that checks the syntax 'http' of a url [origin]
def checkHttpUrl(origin):
    parser = urlparse(origin)
    if parser.scheme == '':
        url = 'http://'+parser.path
        return url
    else:
        return origin

# Function that checks flag level [-l]
def checkNumLevel(level):
    try:
        if int(level) > 0:
            return True
        return False
    except:
        return False

# Function that checks if the path exists and if it does not exist it creates it
def checkDataPath(path):
    try:
        while exists(path) == False:
            mkdir(path)
        return True
    except:
        return False

# Function that returns the default path
def getDefaultDataPath():
    current_path = abspath(getcwd())
    spl_current = current_path.replace('/',' ').split()
    default = ''
    for i in range(0,(len(spl_current)-1)):
        default = default + '/' +spl_current[i]
    return default + '/data'

# Run main function
if __name__=='__main__':
    run_spyder()
