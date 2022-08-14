import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from utils.Printer import *

class Request:

    # Constructor of Request
    def __init__(self, url, head):
        self.url = url
        self.header = head
        self.content = None

    # Function that obtains html code from url - Request
    def get_content(self):
        printer = Printer()
        try:
            target = check_url(self.url)
            req = requests.get(target, headers=self.header)
            if req.status_code == 200:
                html = req.content
                soup = BeautifulSoup(html,'lxml')
                self.content = soup
                printer.messageOk('','[->][SCAN]: {}'.format(target))
                printer.messageInfo('   '+self.header['User-Agent'],'     [AGENT]: \n')
            else:
                check_status_code(self.url, req.status_code, req.reason)
        except Exception:
            printer.messageError('Domain not found --> {}'.format(target))

    # Function that obtains links to pages to be scanned
    def get_links_hrefs(self):
        links = list()
        if self.content != None:
            elements = self.content.findAll('a')
            for a in elements:
                href = a.get('href')
                links.append(href)
        return links

    # Function that obtains links to img to be downloaded
    def get_links_img(self):
        links = list()
        if self.content != None:
            elements = self.content.findAll('img')
            for img in elements:
                src = img.get('src')
                links.append(src)
        return links


# Function that checks the syntax of a url [origin]
def check_url(origin):
    parser = urlparse(origin)
    if parser.scheme == '':
        url = 'http://'+parser.path
        printer = Printer()
        printer.messageWarning('The syntax of the url is invalid, it has been modified by: {}'.format(url))
        return url
    else:
        return origin

# Function that checks request status codes
def check_status_code(url, code, description):
    printer = Printer()
    printer.messageWarning('Status code 200 is required for -> {}'.format(url))
    if code in range(100,199):
        printer.messageError('STATUS CODE [{} - {}] - Informative server response.'.format(code,description))
    if code in range(201,299):
        printer.messageError('STATUS CODE [{} - {}] - Successfull server response.'.format(code,description))
    if code in range(300,399):
        printer.messageError('STATUS CODE [{} - {}] - Redirection detected on server.'.format(code,description))
    if code in range(400,499):
        printer.messageError('STATUS CODE [{} - {}] - Client error detected.'.format(code,description))
    if code in range(500,599):
        printer.messageError('STATUS CODE [{} - {}] - Server error detected.'.format(code,description))
