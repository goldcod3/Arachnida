from utils.Scanner import *

test1 = "https://webscraper.io/"
test2 = "https://www.qoppa.com/pdfstudioviewer/download/"
test3 = "https://httpstat.us/"
test4 = "https://goldcod3.github.io"

res = "https://www.qoppa.com/wp-content/uploads/logo9.png"

scan = Scanner(test1)
scan.depthScan()
scan.printScan()
