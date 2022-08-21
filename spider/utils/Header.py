from random import choice

from utils.Printer import *

# Users-Agents default dictionaries files
default_dics = ['utils/user-agents/Chrome.txt','utils/user-agents/Safari.txt','utils/user-agents/Firefox.txt']

class Header:

    # Constructor of Header
    def __init__(self):
        self.agents = list()
        self.headers = list()

    # Function that obtains a random User-Agents.
    def getAgent(self):
        return choice(self.agents)

    # Function that obtains a random Header
    def getHead(self):
        return choice(self.headers)

    # Function that loads the specified amount [len] of random User-Agents
    def chargeUserAgents(self, len):
        try:
            for i in range(0, len):
                file = choice(default_dics)
                with open(file,"r") as dictionary:
                    agents = dictionary.read().splitlines()
                self.agents.append(choice(agents))
        except Exception:
            printer = Printer()
            printer.messageError('Dictionary user agent {} not found.'.format(file))
            self.agents = None

    # Function that loads a number [count] of headers into Header object.
    def chargeHeaders(self, count=10):
        self.chargeUserAgents(count)
        for agent in self.agents:
            head = {"User-Agent":agent,
                    "Accept-Encoding":"gzip,deflate",
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
            self.headers.append(head)

    # Function that updates the headers of the Header object.
    def updateHeaders(self, count=10):
        self.agents.clear()
        self.headers.clear()
        self.chargeHeaders(count)

    # Function that prints the headers of the Header object
    def printHeaders(self):
        printer = Printer()
        for header in self.headers:
            printer.messageOk('\n'+str(header), '[HEADER] -->')

