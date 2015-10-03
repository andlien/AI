__author__ = 'Simen'
from Module2.cspVertex import *
class State:
    def __init__(self, oldVertices):
        self.g = -1
        self.h = float("inf")
        self.vertices = []
        for v in oldVertices:
            vert = Vertex(v.index,v.x,v.y)

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