from posixpath import splitext
from PIL import Image
from io import BytesIO

from utils.Request import *
from utils.Header import *
from utils.Printer import *
from utils.Logger import checkPath, getDefaultPath

# Default image extensions 
default_exts = ('.png','.jpg','jpeg','gif','.bmp')

class Scraper:

    def __init__(self):
        self.resources = list()
        self.total_imgs = 0
        self.path = getDefaultPath()
        self.process = list()
        self.total_proc = 0
        self.logs = None
        self.headers = Header()
        self.headers.updateHeaders()

    def initScraper(self, scanner):
        self.resources = scanner.imgs
        self.total_imgs = scanner.total_img
        self.path = scanner.logs.path
        self.logs = scanner.logs

    def scrapImages(self, silent=False):
        self.logs.info('')
        self.logs.info('[$] --- *[SCRAPING]* --- [$]')
        self.logs.info('')
        self.logs.info('')
        printer = Printer()
        if silent == False:
            printer.printBanner('[***] Starting scraper')
            print()
        if self.total_imgs > 0:
            for img in self.resources:
                if img not in self.process:
                    self.logs.debug('   [REQUEST]: '+img)
                    if self.scrapResource(img):
                        self.process.append(img)
                        self.total_proc +=1
                        self.logs.debug('   [DOWNLOAD]: '+getNameImg(img))
                        self.logs.info('')
                        if silent == False:
                            printer.messageOk(getNameImg(img),'[->]  {}   [DOWNLOAD]: '.format(self.total_proc))
                    else:
                        self.logs.error('   [-] Error downloading --> {}'.format(getNameImg(img)))
                    if self.total_proc % 5 == 0:
                        self.headers.updateHeaders()
            self.logs.info('')
            self.logs.warning('     [TOTAL RESOURCES DOWNLOADED]: {}'.format(self.total_proc))
            if silent == False:
                print()
                printer.messageWarning('','     [TOTAL RESOURCES DOWNLOADED]: {}'.format(self.total_proc))
        else:
            self.logs.error('   [NOT FOUND RESOURCES]')
            if silent == False:
                printer.messageError('','   [NOT FOUND RESOURCES]')

    def scrapResource(self, target):
        printer = Printer()
        req = Request(target, self.headers.getHead())
        req.getResource()
        if req.content != None:
            name = getNameImg(target)
            try:
                data = BytesIO(req.content)
                img = Image.open(data)
                img.save(self.path+'/'+name)
                return True
            except:
                return False
        else:
            printer.check_status_code(target, req.status_code, req.reason)
            return False

def checkUrlImage(url):
    name = getNameImg(url)
    name_img, ext = splitext(name)
    if ext in default_exts:
        return True
    else:
        return False

def getNameImg(url):
    spl_url = url.replace('/',' ').split()
    return spl_url[-1]