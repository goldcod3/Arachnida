from os.path import splitext
from urllib.parse import urlparse

from utils.Level import *
from utils.Resources import *
from utils.Header import *
from utils.Request import *
from utils.Printer import *
from utils.Logger import *

# Default image extensions 
default_images = ('.png','.jpg','.jpeg','.gif','.bmp')
default_files = ('.docx','.pdf')

class Scanner:

    # Constructor of Scanner
    def __init__(self, url, depth):
        self.origin = url
        self.parse_url = urlparse(url)
        self.url = self.parse_url.scheme+'://'+self.parse_url.netloc
        self.depth = depth
        self.levels = initScanLevels(depth, url)
        self.resources = Resources()
        self.headers = Header()
        self.headers.chargeHeaders(30)
        self.printer = Printer()

    # Function that scans url initialized in Scanner object.
    def depthScan(self, silent=False):
        logger = Logger(self.parse_url.netloc,'scan')
        self.printer.setLogger(logger)
        self.printer.setSilent(silent=silent)
        self.printer.printBanner('[***] Starting scanning')
        logger.title('[~] --- *[SCANNING]* --- [~]')
        # Recursive scan
        self.getLinksUrl(self.origin, self.headers.getHead())
        for lvl in self.levels:
            for ref in lvl.links:
                self.getLinksUrl(ref, self.headers.getHead())
            self.headers.updateHeaders(30)
        self.printer.messageOk('[*] --- *[SCANNING COMPLETED]* --- [*]\n', time=3)
        self.resources.images.sort()
        self.resources.files.sort()
        self.printScan()

    # Function that loads all the links and images of a url [target]
    def getLinksUrl(self, target, head):
        req = Request(target,head)
        self.printer.messageScan(target)
        self.printer.log.info('   [AGENT]: '+req.header['User-Agent'])
        req.getContent(self.printer)
        if req.content != None:
            links = req.getLinksHrefs()
            if len(links) > 0:
                for link in links:
                    self.checkHref(link)
            imgs = req.getLinksImg()
            if len(imgs) > 0:
                for img in imgs:
                    self.checkImage(img, target)
            self.printer.messageInfo('Total Hrefs scaned: '+str(len(links)),'   [->] ')
            self.printer.messageInfo('Total Images scaned: '+str(len(imgs)),'   [->] ')        
            self.printer.messageInfo('','')
        else:
            self.printer.check_status_code(target, req.status_code, req.reason)
            self.printer.messageInfo('','')

    # Function that subdivides url [content] into levels 
    def chargeHref(self, content):
        url = urlparse(content)
        domain = self.parse_url.scheme+'://'+self.parse_url.netloc
        spl_path = url.path.replace('/',' ').split()
        i = 0
        while i < len(spl_path):
            target = domain +'/' 
            j = 0
            while j <= i:
                target = target + spl_path[j]+ '/'
                j+=1
            self.addHref(i+1, target)
            i+=1
    
    # Link checking function
    def checkHref(self, href):
        if href != None:
            name , ext = splitext(href)
            if ext == "":
                if href.startswith(self.url):
                    self.chargeHref(href)
                if href.startswith("/"):
                    self.chargeHref(self.url+href)
            else:
                if ext in default_files:
                    self.checkFile(href)


    def checkFile(self, file):
        if file != None:
            if file.startswith(self.url):
                self.addFile(file)
            if file.startswith("/"):
                self.addFile(self.url+file)

    # Image checking function
    def checkImage(self, img, target_url):
        if img != None:
            if img.startswith(self.url):
                res, ext = splitext(img)
                if ext in default_images:
                    self.addImg(img)
            else:
                res, ext = splitext(img)
                if img.startswith('/'):
                    img = self.url+img
                    if ext in default_images:
                        self.addImg(img)
                if img.startswith('http') == False:
                    if target_url.endswith('/'):
                        img = target_url+img
                    else:
                        img = target_url+'/'+img
                    if ext in default_images:
                        self.addImg(img)                 

    # Function that adds link at the indicated level
    def addHref(self, depth, url):
        for level in self.levels:
            if level.depth == depth:
                if url not in level.links:
                    level.links.append(url)
                    level.total_links += 1
                break

    def addFile(self, file):
        if file not in self.resources.files:
            self.resources.addResFile(file)

    # Function that adds img to list
    def addImg(self, img):
        if img not in self.resources.images:
            self.resources.addResImage(img)

    # Function that prints scan result
    def printScan(self):
        self.printer.printBanner('[***] Loading scan')
        self.printer.log.title('[+] --- *[RESUME]* --- [+]\n')
        self.printer.messageOk('*[LEVELS]*\n','[/] ---> ')
        for level in self.levels:
            self.printer.messageInfo('[LEVEL DEPTH]: '+str(level.getDepth()), '[>]')
            if level.getTotalLinks() > 0:
                self.printer.messageWarning('Total -> '+str(level.getTotalLinks()), '     [URL\'S SCANNED]: ')
            else:
                self.printer.messageError('Not found links.')
            self.printer.messageInfo('','')
        self.printer.messageOk('*[RESOURCES]*\n','[*] ---> ',1)
        self.printer.messageOk('*[IMAGES]*\n','[+] ---> ')
        if self.resources.count_images > 0:
            for img in self.resources.images:
                self.printer.messageWarning(img,'    [*] ', 0.02)
            self.printer.messageInfo('Total -> '+str(self.resources.count_images)+'\n','\n    [IMG\'S FOUND]: ')
        else:
            self.printer.messageError('Not found resources.')
        self.printer.messageOk('*[FILES]*\n','[+] ---> ',1)
        if self.resources.count_files > 0:
            for file in self.resources.files:
                self.printer.messageWarning(file,'    [*] ', 0.02)
            self.printer.messageInfo('Total -> '+str(self.resources.count_files)+'\n','\n    [FILES FOUND] ')
        else:
            self.printer.messageError('Not found resources.')
        self.printer.messageInfo('','', 3)
        


# Function that initializes the levels as a function of depth
def initScanLevels(depth, url):
    levels = list()
    for i in range(0,depth+1):
        lvl = Level()
        if i == 0:
            lvl.links.append(url)
            lvl.total_links +=1
        levels.append(lvl)
    return levels