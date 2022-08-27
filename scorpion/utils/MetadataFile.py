from PyPDF2 import PdfFileReader
from docx import Document
from os.path import splitext

class MetadataFile:

    # Constructor of MetadataFile object
    def __init__(self, path):
        self.path = path
        self.filename = path.replace('/',' ').split()[-1]
        name, ext = splitext(path)
        self.type = ext

    # Function that prints the file metadata
    def getMetadata(self):
        print('\033[0;34m'+'***[TARGET FILE]***'+'\033[0m'+' -> {}\n'.format(self.path))
        if self.type == '.docx':
            print('\033[0;92m'+'[BASIC METADATA]'+'\033[0m')        
            self.printDocx()
        elif self.type == '.pdf':
            print('\033[0;92m'+'[BASIC METADATA]'+'\033[0m')
            self.printPDF()
        else:
            print('\033[0;91m'+'    [ERROR]'+'\033[0m'+': Invalid File.')
        print()

    # Function that obtains and prints the metadata of the docx file.
    def printDocx(self):
        try:
            doc_file = Document(open(self.path, "rb"))
            doc_info = doc_file.core_properties
            attrib = ["title", "author", "category", "version",
                    "created", "modified", "last_modified_by", "last_printed",
                    "identifier", "keywords", "language","revision",
                     "subject", "comments", "content_status"]
            for atr in attrib:
                value = getattr(doc_info, atr)                    
                print('\033[0;93m'+'    [>] '+'\033[0m'+f"{atr:30}-> {str(value)}")
        except:
            print('\033[0;91m'+'    [ERROR]'+'\033[0m'+': Document can\'t be opened.')

    # Function that obtains and prints the metadata of the pdf file.
    def printPDF(self):
        pdf_info = None
        try:
            pdf_file = PdfFileReader(open(self.path, "rb"))
            pdf_info = pdf_file.getDocumentInfo()
        except Exception as e:
            print('\033[0;91m'+'    [ERROR]'+'\033[0m'+': Document can\'t be opened - {}'.format(e))
        if pdf_info:
            for meta in pdf_info:
                try:
                    print('\033[0;93m'+'    [>] '+'\033[0m'+f"{meta[1:]:30}-> {str(pdf_info[meta])}")
                except:
                    print('\033[0;91m'+'    [ERROR]'+'\033[0m'+': The metadata for {} value can\'t be readed.'.format(meta[-1]))
        else:
            print('\033[0;91m'+'    [ERROR]'+'\033[0m'+': Document has no metadata!')
