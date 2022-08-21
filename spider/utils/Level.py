
class Level:

    # Counter objects Level
    lvl_count = 0

    # Constructor of Level
    def __init__(self):
        self.depth = Level.lvl_count
        Level.lvl_count = Level.lvl_count + 1
        self.links = list()
        self.total_links = 0

    # Get depth of Level
    def getDepth(self):
        return self.depth

    # Get links of Level
    def getLinks(self):
        return self.links

    # Get total links of Level
    def getTotalLinks(self):
        return self.total_links
