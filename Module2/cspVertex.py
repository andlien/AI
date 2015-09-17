class Vertex:
    def __init__(self, index, x, y):
        self.x = x
        self.y = y
        self.index = index
        self.connectedTo = []
