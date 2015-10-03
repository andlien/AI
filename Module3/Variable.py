__author__ = 'Simen'


class Variable:
    def __init__(self,index,coord):
        self.domain = []
        self.coord = coord
        self.index = index


    def isAssumed(self):
        return len(self.domain) == 1

    def getRowOrColumn(self):
        return self.rowOrColumn