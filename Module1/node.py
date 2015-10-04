class Node:

    # "static" variables to keep track of start and goal
    startNode = None

    goalX = -1
    goalY = -1

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.h = float("inf")
        self.g = -1
        self.parent = None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def isGoal(self):
        return self.x == Node.goalX and self.y == Node.goalY