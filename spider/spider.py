from utils.args import config_args
from utils.Scanner import *
from utils.Scraper import *

# Main
def run_spyder():
    args = config_args()
    printer = Printer()
    if args.recursive != None and args.image == None:
        url_scan = checkUrl(args.recursive)
        lvl_scan = 5
        path_scan = getDefaultPath()
        if args.level != None:
            if checkLevel(args.level):
                lvl_scan = int(args.level)
            else:
                if args.silent == False:
                    printer.messageError(' Invalid value of level, default value [5] charged.')
                    sleep(2)
        if args.path != None:
            if checkPath(args.path):
                path_scan = args.path
            else:
                if args.silent == False:
                    printer.messageError('Invalid value of path, default path [../data] charged.')
                    printer.messageWarning(' Try with \'/home/user/path\'.')
                    sleep(2)
        scan = Scanner(url=url_scan, depth=lvl_scan, path=path_scan)
        scan.depthScan(args.silent)
        if args.silent == False:
            scan.printScan()
        scan.logsScanResult()   
        scrap = Scraper()
        scrap.initScraper(scan)
        scrap.scrapImages(args.silent)
    if args.recursive == None and args.image != None:
        url_res = checkUrl(args.image)
        if checkUrlImage(url_res):
            scrp = Scraper()
            checkPath(scrp.path)
            result = scrp.getResource(url_res)
            if args.silent == False:
                printer.printBanner('[*] Scraping resource')
                if result:
                    printer.messageOk(' Resource \'{}\' downloaded in default data directory.'.format(url_res))
                else:
                    printer.messageError(' Resource \'{}\' can\'t be downloaded.'.format(url_res))
        else:
            if args.silent == False:
                printer.messageError(' Resource \'{}\' not found.'.format(url_res))


def checkLevel(lvl):
    try:
        if int(lvl) > 0:
            return True
        return False
    except:
        return False

def checkPath(path):
    try:
        if exists(path):
            return True
        else:
            return False
    except:
        return False

if __name__=="__main__":
    run_spyder()