from os.path import splitext
from urllib.parse import urlparse
from tqdm import tqdm
from time import sleep

from utils.Level import *
from utils.Header import *
from utils.Request import *
from utils.Printer import *
from utils.Logger import *

# Default image extensions 
default_exts = ('.png','.jpg','jpeg','gif','.bmp')

class Scanner:

    # Constructor of Scanner
    def __init__(self, url, depth=5, path=getDefaultPath()):
        self.parse_url = urlparse(url)
        self.origin = url
        self.url = self.parse_url.scheme+'://'+self.parse_url.netloc
        self.depth = depth
        self.lvls = initLevels(depth, url)
        self.imgs = list()
        self.total_img = 0
        self.headers = Header()
        self.headers.updateHeaders()
        self.path_scan = getNameDir(self.parse_url.netloc)
        checkPath(path)
        self.logs = Logger(('scan_'+self.parse_url.netloc),(path+'/'+self.path_scan))


    # Function that scans url initialized in Scanner object.
    def depthScan(self):
        printer = Printer()
        printer.printBanner('[$$$] Starting scanning')
        self.getLinksUrl(self.origin, self.headers.getHead(), printer)
        for lvl in self.lvls:
            for ref in lvl.links:
                self.getLinksUrl(ref, self.headers.getHead(), printer)
            self.headers.updateHeaders()

    # Function that loads all the links and images of a url [target]
    def getLinksUrl(self, target, head, printer):
        req = Request(target,head)
        printer.messageOk('','[->][SCAN]: {}'.format(target))
        self.logs.debug('   [SCAN]: '+target)
        self.logs.debug('   [AGENT]: '+req.header['User-Agent'])
        req.get_content()
        if req.content != None:
            links = req.get_links_hrefs()
            self.logs.debug('   [-] Total Hrefs scaned: '+str(len(links)))
            if len(links) > 0:
                lnk_bar = tqdm(range(len(links)),'   [-] Href scan: ',)
                for l in lnk_bar:
                    href = self.checkHref(links[l])
                    if href != None:
                        self.chargeHref(href)
                    #sleep(0.009)
            imgs = req.get_links_img()
            self.logs.debug('   [-] Total Images scaned: '+str(len(links)))
            if len(imgs) > 0:
                img_bar = tqdm(range(len(imgs)),'   [-] Img scan: ')
                for i in img_bar:
                    ref = self.checkImage(imgs[i])
                    if ref != None:
                        self.addImg(ref)
                    #sleep(0.009)
        else:
            printer.check_status_code(target, req.status_code, req.reason)
            self.logs.error('   {} --> [{} - {}]'.format(target,req.status_code,req.reason))

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

    # Function that adds link at the indicated level
    def addHref(self, depth, url):
        for lvl in self.lvls:
            if lvl.depth == depth:
                if url not in lvl.links:
                    lvl.links.append(url)
                    lvl.total_links += 1
                break
    
    # Link checking function
    def checkHref(self, href):
        if href != None:
            if href.startswith(self.url):
                return href
            elif href.startswith("/"):
                return self.url+href
            else:
                return None

    # Function that adds img to list
    def addImg(self, img):
        if img not in self.imgs:
            self.imgs.append(img)
            self.total_img +=1

    # Image checking function
    def checkImage(self, img):
        tmp = img
        if img != None:
            if tmp.startswith(self.url):
                res, ext = splitext(tmp)
                if ext in default_exts:
                    return tmp
            else:
                if tmp.startswith('/'):
                    tmp = self.url+img
                if tmp.startswith('http') == False:
                    tmp = self.url+'/'+img
                res, ext = splitext(tmp)
                if ext in default_exts:
                    return tmp       
        return None

    # Function that prints scan result
    def printScan(self):
        printer = Printer()
        printer.printBanner('[***] Loading scan')
        printer.messageOk('','[/] --- *[LEVELS]* --- [/]')
        for lvl in self.lvls:
            printer.messageInfo(str(lvl.getDepth()), '[>][LEVEL DEPTH]: ')
            if lvl.getTotalLinks() > 0:
                printer.messageWarning(str(lvl.getTotalLinks()), '     [TOTAL URL\'S SCANNED]: ')
            else:
                printer.messageError('Not found links.')
            print()
        printer.messageOk('','[+] --- *[RESOURCES]* --- [+]')
        sleep(1)
        if self.total_img > 0:
            for img in self.imgs:
                printer.messageWarning(img,'    [*] ')
                sleep(0.02)
            print()
            printer.messageInfo(str(self.total_img),'[TOTAL IMG\'S FOUND]: ')
        else:
            printer.messageError('Not found resources.')

