from utils.Scanner import *
from utils.Scraper import *

test1 = "https://webscraper.io/"
test2 = "https://www.qoppa.com/pdfstudioviewer/download/"
test3 = "https://httpstat.us/"
test4 = "goldcod3.github.io"

res = "https://www.qoppa.com/wp-content/uploads/logo9.png"

scan = Scanner(test4)
scan.depthScan()
scan.printScan()
scan.logsScanResult()

scrap = Scraper()
scrap.initScraper(scan)
scrap.scrapImages()