__author__ = 'Simen'
class State:
    def __init__(self, vertices):
        self.vertices = []
        #self.id
        for v in vertices:
            vert = Vertex(v.index,v.x,v.y)
            vert.domain = []
            for d in v.domain:
                vert.domain.append(d)

            self.vertices.append(vert)
