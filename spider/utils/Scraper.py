from os.path import splitext
from PIL import Image
from io import BytesIO

from utils.Resources import *
from utils.Request import *
from utils.Header import *
from utils.Printer import *
from utils.Logger import *

# Default extensions files
default_images = ('.png','.jpg','.jpeg','.gif','.bmp')
default_files = ('.docx','.pdf')

class Scraper:

    # Constructor of Scraper
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self.resources = Resources()
        self.process = 0
        self.headers = Header()
        self.headers.chargeHeaders(5)
        self.printer = Printer()        

    # Function to download files previously scanned with a scanner object
    def scrapResources(self, resources, silent=False):
        self.resources = resources
        self.printer.setSilent(silent=silent)
        self.printer.printBanner('[***] Starting scraper')
        if self.resources.count_images > 0 or self.resources.count_files > 0:
            logger = Logger(self.url,'scrap')
            self.printer.setLogger(logger)
            self.printer.log.title('[$] --- *[SCRAPING]* --- [$]')
            datapath = self.getScrapPath()
            if self.resources.count_images > 0:
                self.headers.updateHeaders(50)
                self.printer.messageInfo('[IMAGES]: ', '[>]')
                for img in self.resources.images:
                    self.scrapImage(img, datapath)
            if self.resources.count_files > 0:
                self.headers.updateHeaders(50)
                self.printer.messageInfo('[FILES]: ', '[>]')
                for file in self.resources.files:
                    self.scrapFile(file, datapath)
            total_resources = self.resources.count_images + self.resources.count_files
            self.printer.messageInfo('Total --> {}/{}'.format(self.process, total_resources), '\n[DOWNLOADED] ')
        else:
            self.printer.messageError(' NOT FOUND RESOURCES')

    # Function that download a resource from the url previously loaded in the scraper object
    def scrapResourceFromUrl(self, silent=False):
        self.printer.setSilent(silent=silent)
        self.printer.printBanner('[*] Scraping resource')
        name, ext = splitext(self.url)
        status = False
        if ext != '':
            if ext in default_images:
                self.scrapImage(self.url, self.path)
                status = True
            if ext in default_files:
                self.scrapFile(self.url, self.path)
                status = True
            if status == False:
                self.printer.messageError(' Resource \'{}\' can\'t be downloaded.'.format(self.url))
            else:
                self.printer.messageOk(' Resource \'{}\' downloaded in default data directory.'.format(self.url))
        else:
            self.printer.messageError(' Resource \'{}\' not found.'.format(self.url))

    # Function that download a image
    def scrapImage(self, url_image, path):
        name = getNameResource(url_image)
        if exists(path+'/'+name) == False:
            req = Request(url_image, self.headers.getHead())
            req.getImage(self.printer)
            if req.content != None:
                try:
                    data = BytesIO(req.content)
                    img = Image.open(data)
                    img.save(path+'/'+name)
                    self.process+=1
                    self.printer.messageOk('{}   [DOWNLOAD]: {}'.format(self.process, name), '   [>] ')
                except:
                    self.printer.messageError('Error downloading --> {}'.format(url_image), '   [X] ')
        else:
            self.printer.messageWarning('The file exist in path --> {}'.format(path), '   [*] ')

    # Function that download a file
    def scrapFile(self, url_file, path):
        name = getNameResource(url_file)
        if exists(path+'/'+name) == False:
            req = Request(url_file, self.headers.getHead())
            req.getFile(self.printer)
            if req.content != None:
                try:
                    with open(path+'/'+name, 'wb') as fd:
                        for chunk in req.content.iter_content(chunk_size=128):
                            fd.write(chunk)
                    self.process+=1
                    self.printer.messageOk('{}   [DOWNLOAD]: {}'.format(self.process, name), '   [>] ')
                except:
                    self.printer.messageError('Error downloading --> {}'.format(url_file), '   [X] ')
        else:
            self.printer.messageWarning('The file exist in path --> {}'.format(path), '   [*] ')

    # Function that returns the path to the directory where the resources will be saved
    def getScrapPath(self):
        datapath = self.path+'/'+self.url
        while exists(datapath) == False:
                mkdir(datapath)
        return datapath

# Function that returns the name of the resource to download
def getNameResource(url):
    spl_url = url.replace('/',' ').split()
    return spl_url[-2]+'_'+spl_url[-1]
