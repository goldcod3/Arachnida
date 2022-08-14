from utils.Scanner import *

url = "https://webscraper.io/"

scan = Scanner(url)
scan.depthScan()
scan.printScan()
