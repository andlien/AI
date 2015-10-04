from graphics import *
from Module1.node import *

height = 9
width = 9
size = 40


win = None

obstacles = []

def getWindow():
    return win

def setDimensions(x,y):
    global width
    global height
    global win
    width = x
    height = y

    win = GraphWin('A* search', height*size+5, width*size+5)

def createObstacle(startX,startY,widht,height):
    for x in range(0,widht):
        for y in range(0,height):
            obstacles.append((startX + x, startY + y))
            drawBox(startX + x, startY + y, "black")

# Save and draw startnode
def createStart(startX,startY):
    Node.startNode = Node(startX, startY)
    drawBox(startX, startY, "green")

# Goal node is not yet created, save coordinates and draw
def createGoal(startX,startY):
    Node.goalX = startX
    Node.goalY = startY
    drawBox(startX, startY, "red")

# Main draw method for module 1
def drawBox(x, y, color):
    head2 = Rectangle(Point(x*size +5,height*size - y*size - size+5), Point( x*size + size+5,height*size - y*size +5)) # set center and radius
    head2.setFill(color)
    #head2.setOutline("black")
    head2.setOutline(color)
    head2.draw(win) 

def manhattenDistToGoalNode(node):
    xDist = abs(node.x - Node.goalX)
    yDist = abs(node.y - Node.goalY)
    return xDist + yDist

def euclideanDistToGoalNode(node):
    xDist = (node.x - Node.goalX)**2
    yDist = (node.y - Node.goalY)**2
    return (xDist + yDist) ** 0.5

# Generates the new child-nodes to this node
# Ignores wall, of course
def getSurroundingTiles(node):
    surroundingTiles = []

    x = node.x
    y = node.y

    if x > 0 and not (x-1, y) in obstacles:
        surroundingTiles.append(Node(x-1, y))
    if x < width - 1 and not (x+1, y) in obstacles:
        surroundingTiles.append(Node(x+1, y))
    if y > 0 and not (x, y-1) in obstacles:
        surroundingTiles.append(Node(x, y-1))
    if y < height - 1 and not (x, y+1) in obstacles:
        surroundingTiles.append(Node(x, y+1))

    if node.parent in surroundingTiles:
        surroundingTiles.remove(node.parent)
    return surroundingTiles

# Initializes board with only grey tiles
def createBoard():
    for x in range(0,height):
        for y in range(0,width):
            drawBox(x, y, "light grey")

