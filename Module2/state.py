__author__ = 'Simen'
from cspVertex import *
class State:
    def __init__(self, oldVertices):
        self.vertices = []
        for v in oldVertices:
            vert = Vertex(v.index,v.x,v.y)
            vert.domain = []
            for d in v.domain:
                vert.domain.append(d)

            self.vertices.append(vert)

        self.lastModifiedVertex = None

    def getUniqeID(self):
        id = ""
        for vert in self.vertices:
            if vert.isColored():
                id += str(vert.domain[0])
            else:
                id += str(0)

        return id

    def isFinished(self):
        for vert in self.vertices:
            if len(vert.domain) > 1:
                return False
        return True

    def isError(self):
        for vert in self.vertices:
            if len(vert.domain) == 0:
                return True
        return False