
class Level:

    # Counter objects Level
    lvl_count = 0

    # Constructor of Level
    def __init__(self):
        self.depth = Level.lvl_count
        Level.lvl_count = Level.lvl_count + 1
        self.links = list()
        self.total_links = 0
        self.resources = list()

    # Get depth of Level
    def getDepth(self):
        return self.depth

    # Get links of Level
    def getLinks(self):
        return self.links

    # Get total links of Level
    def getTotalLinks(self):
        return self.total_links


# Function that initializes the levels as a function of depth
def initLevels(depth, url):
    levels = list()
    for i in range(0,depth+1):
        lvl = Level()
        if i == 0:
            lvl.links.append(url)
            lvl.total_links +=1
        levels.append(lvl)
    return levels
