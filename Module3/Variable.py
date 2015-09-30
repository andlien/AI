__author__ = 'Simen'


class Variable:
    def __init__(self,index,coord,rowOrColumn):
        self.domain = []
        self.coord = coord
        self.rowOrColumn = rowOrColumn #1 is row, 2 is column
        self.index = index


    def isAssumed(self):
        return len(self.domain) == 1

    def getRowOrColumn(self):
        return self.rowOrColumn