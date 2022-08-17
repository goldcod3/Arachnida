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
    def __init__(self, url, depth, path):
        self.parse_url = urlparse(url)
        self.origin = url
        self.url = self.parse_url.scheme+'://'+self.parse_url.netloc
        self.depth = depth
        self.lvls = initLevels(depth, url)
        self.imgs = list()
        self.total_img = 0
        self.headers = Header()
        self.headers.updateHeaders()
        self.path = path
        self.path_scan = getNameDir(self.parse_url.netloc)
        checkPath(path)
        self.logs = Logger(('scan_'+self.parse_url.netloc),(path+'/'+self.path_scan))


    # Function that scans url initialized in Scanner object.
    def depthScan(self, silent=False):
        printer = Printer()
        if silent == False:
            printer.printBanner('[$$$] Starting scanning')
        self.logs.info('')
        self.logs.info('[~] --- *[SCANNING]* --- [~]')
        self.logs.info('')
        self.logs.info('')
        self.getLinksUrl(self.origin, self.headers.getHead(), printer, silent)
        for lvl in self.lvls:
            for ref in lvl.links:
                self.getLinksUrl(ref, self.headers.getHead(), printer, silent)
            self.headers.updateHeaders()
        sleep(3)

    # Function that loads all the links and images of a url [target]
    def getLinksUrl(self, target, head, printer, silent):
        req = Request(target,head)
        self.logs.info('')
        self.logs.debug('   [SCAN]: '+target)
        self.logs.debug('   [AGENT]: '+req.header['User-Agent'])
        req.getContent()
        if req.content != None:
            links = req.getLinksHrefs()
            if len(links) > 0:
                for link in links:
                    href = self.checkHref(link)
                    if href != None:
                        self.chargeHref(href)
            imgs = req.getLinksImg()
            if len(imgs) > 0:
                for img in imgs:
                    ref = self.checkImage(img, target)
                    if ref != None:
                        self.addImg(ref)
            self.logs.debug('   [-] Total Hrefs scaned: '+str(len(links)))
            self.logs.debug('   [-] Total Images scaned: '+str(len(imgs)))
            if silent == False:
                printer.messageOk('','[->][SCAN]: {}'.format(target))
                printer.messageInfo('Total Hrefs scaned: '+str(len(links)), '        [->] ')
                printer.messageInfo('Total Images scaned: '+str(len(imgs)), '        [->] ')
                sleep(0.1)         
        else:
            self.logs.error('       {} --> [{} - {}]'.format(target,req.status_code,req.reason))
            if silent == False:
                printer.check_status_code(target, req.status_code, req.reason)

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
            name , ext = splitext(href)
            if ext == "":
                if href.startswith(self.url):
                    return href
                elif href.startswith("/"):
                    return self.url+href
                else:
                    return None
            else:
                return None

    # Function that adds img to list
    def addImg(self, img):
        if img not in self.imgs:
            self.imgs.append(img)
            self.total_img +=1

    # Image checking function
    def checkImage(self, img, target_url):
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
                    if target_url.endswith('/'):
                        tmp = target_url+img
                    else:
                        tmp = target_url+'/'+img
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

    def logsScanResult(self):
        log = self.logs
        log.name = 'scan_resume_'+self.parse_url.netloc
        log.info('')
        log.info('')
        log.info('')
        log.info('[*] --- *[RESUME]* --- [*]')
        log.info('')
        log.info('[/] --- *[LEVELS]* --- [/]')
        log.info('')
        for lvl in self.lvls:
            log.debug('[>]    [LEVEL DEPTH]: {}'.format(str(lvl.getDepth())))
            if lvl.getTotalLinks() > 0:
                log.debug('       [TOTAL URL\'S SCANNED]: {}'.format(str(lvl.getTotalLinks())))
            else:
                log.error('       Not found links.')
            log.info('')
        log.info('')
        log.info('[+] --- *[RESOURCES]* --- [+]')
        log.info('')
        if self.total_img > 0:
            for img in self.imgs:
                log.warning('[*]    {}'.format(img))
            log.info('')
            log.warning('   [TOTAL IMG\'S FOUND]: {}'.format(str(self.total_img)))
        else:
            log.error('   Not found resources.')
        log.info('')
        log.info('')
        sleep(3)
