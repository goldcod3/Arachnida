
class Resources:

    def __init__(self):
        self.images = list()
        self.count_images = 0
        self.files = list()
        self.count_files = 0

    def addResImage(self, img):
        self.images.append(img)
        self.count_images +=1

    def addResFile(self, file):
        self.files.append(file)
        self.count_files +=1
