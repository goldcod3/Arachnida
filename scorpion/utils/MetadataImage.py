from PIL import Image
from exifread import process_file
from os.path import getsize

class MetadataImage:

    # Constructor of MetadataImage object
    def __init__(self, path):
        self.path = path
        self.filename = None
        self.format = None
        self.description = None
        self.height = None
        self.width = None
        self.mode = None
        self.size = None
        self.animate = None
        self.frames = None

    # Function that prints the metadata of an image
    def getMetadata(self):
        print('\033[0;34m'+'***[TARGET IMAGE]***'+'\033[0m'+' -> {}\n'.format(self.path))
        self.filename = self.path.replace('/',' ').split()[-1]
        try:
            image = Image.open(self.path)
            self.format = image.format
            self.description = image.format_description
            self.height = image.height
            self.width = image.width
            self.mode = image.mode
            self.size = round((getsize(self.path) / 1024), 1)
            self.animate = getattr(image, "is_animated", False)
            self.frames = getattr(image, "n_frames", 1)
            self.printMetadata()
            print()
            self.getEXIF()
            print()
        except:
            print('\033[0;91m'+'    [ERROR]'+'\033[0m'+': Invalid File.')

    # Function that prints the EXIF metadata of the resource
    def getEXIF(self):
        print('\033[0;92m'+'[EXIF METADATA]'+'\033[0m')
        img = open(self.path, 'rb')
        tags = process_file(img)
        if len(tags) > 0:
            for t in tags.keys():
                if checkTagEXIF(t):
                    print('\033[0;93m'+'    [>] '+'\033[0m'+f"{str(t):30}-> {str(tags[t])}")
        else:
            print('\033[0;91m'+'    [ERROR]'+'\033[0m'+': Exif data not found!')

    # Function that prints the basic metadata of the resource
    def printMetadata(self):
        print('\033[0;92m'+'[BASIC METADATA]'+'\033[0m')
        print('\033[0;93m'+'    [*] '+'\033[0m'+f"{'Image Path':30}-> {self.path}")
        print('\033[0;93m'+'    [*] '+'\033[0m'+f"{'Image File Name':30}-> {self.filename}")
        print('\033[0;93m'+'    [*] '+'\033[0m'+f"{'Image Format':30}-> {self.format}")
        print('\033[0;93m'+'    [*] '+'\033[0m'+f"{'Image Format Description':30}-> {self.description}")
        print('\033[0;93m'+'    [*] '+'\033[0m'+f"{'Image Height':30}-> {self.height} px")
        print('\033[0;93m'+'    [*] '+'\033[0m'+f"{'Image Width':30}-> {self.width} px")
        print('\033[0;93m'+'    [*] '+'\033[0m'+f"{'Image Mode':30}-> {self.mode}")
        print('\033[0;93m'+'    [*] '+'\033[0m'+f"{'Image Size':30}-> {self.size} KB")
        print('\033[0;93m'+'    [*] '+'\033[0m'+f"{'Image Animate':30}-> {self.animate}")
        print('\033[0;93m'+'    [*] '+'\033[0m'+f"{'Image Frames':30}-> {self.frames}")

# Function that checks and filters the EXIF TAGS of the analyzed file
def checkTagEXIF(tag):
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename','EXIF MakerNote', 'EXIF ExifImageLength',
         'EXIF ExifImageWidth', 'Image PrintIM', 'Interoperability InteroperabilityVersion',
         'Interoperability InteroperabilityIndex'):
        if tag.startswith('MakerNote') == False and tag.startswith('Thumbnail') == False:
            return True
    return False