class Vertex:
    def __init__(self, index, x, y):
        self.x = x
        self.y = y
        self.index = index
        #self.connectedTo = []
        self.domain = []

    def isColored(self):
        return len(self.domain) == 1

    # def __eq__(self, other):
    #     if isinstance(other, self.__class__):
    #         return self.x == other.x and self.y == other.y
    #     else:
    #         return False
    #
    # def __ne__(self, other):
    #     return not self.__eq__(other)

    def getColor(self):
        #print("IS colored: " + str(self.isColored()))
        colorKey = int(self.domain[0])

        if colorKey == 1:
            return "red"
        elif colorKey == 2:
            return "blue"
        elif colorKey == 3:
            return "yellow"
        elif colorKey == 4:
            return "green"
        elif colorKey == 5:
            return "orange"
        elif colorKey == 6:
            return "grey"
        elif colorKey == 7:
            return "black"