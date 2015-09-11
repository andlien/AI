class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.h = 0
        self.g = float("inf")


        self.isObstacle = False
        self.isGoal = False
        self.isStart = False
        self.isObserved = False
        self.isTraversed = False
        self.parent = None
        self.isShortestPath = False



