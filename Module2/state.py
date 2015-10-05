from Module2.cspVertex import *
from Module3.Variable import *

class State:
    def __init__(self, oldVertices, moduleNr):
        self.g = -1
        self.h = float("inf")
        self.moduleNr = moduleNr
        self.vertices = []
        for v in oldVertices:
            vert = None
            if moduleNr == 2:
                vert = Vertex(v.index,v.x,v.y)
            elif moduleNr == 3:
                vert = Variable(v.index,v.coord)
            else:
                print("Unkown module!")


            for d in v.domain:
                vert.domain.append(d)

            self.vertices.append(vert)

        self.lastModifiedVertex = None
        self.parent = None


    def getUniqeID(self):
        id = ""
        for vert in self.vertices:
            if vert.isColored():
                id += str(vert.domain[0])
            else:
                id += str(0)

        return id

    def isGoal(self):
        if self.isError():
            return False

        for vert in self.vertices:
            if len(vert.domain) != 1:
                return False
        return True

    def isError(self):
        for vert in self.vertices:
            if len(vert.domain) == 0:
                return True
        return False

    def getNumberOfVariablesNotAssigned(self):
        sum = 0
        for vert in self.vertices:
            if len(vert.domain) > 1:
                sum = sum + 1
        return sum
