class Vertex:
    def __init__(self, index, x, y):
        self.x = x
        self.y = y
        self.index = index
        #self.connectedTo = []
        self.domain = []

    def isColored(self):
        return len(self.domain) == 1

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
            return "dark blue"
        elif colorKey == 7:
            return "light blue"
        elif colorKey == 8:
            return "dark red"
        elif colorKey == 9:
            return "pink"
        elif colorKey == 10:
            return "black"