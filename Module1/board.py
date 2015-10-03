from graphics import *
from Module1.node import *

height = 9
width = 9
size = 40


win = None

obstacles = []

searchType = "A*"

#goalNode
# startNode
#currentNode

def getWindow():
    return win

def setDimensions(x,y):
    global width
    global height
    global win
    width = x
    height = y

    numberOfNodes = height * width

    win = GraphWin('A*', height*size+5, width*size+5)

# def createObstacle2(startX,startY,owidht,oheight):
#     createObstacle2(startX,startY,owidht,oheight)
#     head2 = Rectangle(Point(startX*size +5,height*size - startY*size +5), Point( startX*size + owidht*size+5,
#     height*size - startY*size - oheight*size+5)) # set center and radius
#
#     head2.setFill("dark red")
#
#     head2.setOutline("dark grey")
#     #head2.setOutline(getNodeColor(node))
#
#     head2.draw(win)

def createObstacle(startX,startY,widht,height):
    for x in range(0,widht):
        for y in range(0,height):
            obstacles.append((startX + x, startY + y))
            drawBox(startX + x, startY + y, "black")


def createStart(startX,startY):
    Node.startNode = Node(startX, startY)
    drawBox(startX, startY, "green")

# Goal node is not yet created
def createGoal(startX,startY):
    Node.goalX = startX
    Node.goalY = startY
    drawBox(startX, startY, "red")

def drawBox(x, y, color):
    head2 = Rectangle(Point(x*size +5,height*size - y*size - size+5), Point( x*size + size+5,height*size - y*size +5)) # set center and radius
    head2.setFill(color)
    #head2.setOutline("black")
    head2.setOutline(color)
    head2.draw(win) 

def drawShortestPathNode(x, y):
    head2 = Rectangle(Point(x*size +5,height*size - y*size - size+5), Point(x*size + size+5,height*size - y*size +5)) # set center and radius
    head2.setFill("dark red")
    head2.setOutline("red")
    #head2.setOutline(getNodeColor(node))
    head2.draw(win)


def getNodeColor(node):
    if node.isGoal():
        return "red"
    elif node.isStart:
        return "green"
    elif node.isShortestPath:
        return "dark red"
    elif node.isTraversed:
        return "grey"
    elif node.isObserved:
        return "dark grey"
    elif node.isObstacle:
        return "black"
    else:
        return "light grey"

# def setHInAllNodes():
#     for x in range(0,height):
#         for y in range(0,width):
#             node = nodes[x][y]
#             #node.h = manhattenDistToGoalNode(node.x,node.y)
#             node.h = euclideanDistToGoalNode(node.x,node.y)



def manhattenDistToGoalNode(node):
    #if searchType  != "A*":
    #    return 0
    xDist = abs(node.x - Node.goalX)
    yDist = abs(node.y - Node.goalY)
    return xDist + yDist

def euclideanDistToGoalNode(node):
    #if searchType  != "A*":
    #    return 0
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



# def main():
#     win = GraphWin('A*', height*size+5, width*size+5) # give title and dimensions
#     #win.yUp() # make right side up coordinates!
#
#     #head = Circle(Point(40,100), 25) # set center and radius
#     #head.setFill("yellow")
#     #head.draw(win)
#
#     for x in nodes:
#         for node in x:
#                 head2 = Rectangle(Point(node.x*size +5,height*size - node.y*size - size+5), Point( node.x*size + size+5,height*size - node.y*size +5)) # set center and radius
#                 head2.setFill(node.getColor())
#                 head2.setOutline("white")
#                 head2.draw(win)




    #eye1 = Circle(Point(30, 105), 5)
    #eye1.setFill('blue')
    #eye1.draw(win)

    #eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    #eye2.setWidth(3)
    #eye2.draw(win)

    #mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
    #mouth.setFill("red")
    #mouth.draw(win)

    #label = Text(Point(100, 120), 'A face')
    #label.draw(win)

    #message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    #message.draw(win)
    # win.getMouse()
    #
    # head2 = Rectangle(Point(5*size +5,height*size - 5*size - size+5), Point( 5*size + size+5,height*size - 5*size +5)) # set center and radius
    # head2.setFill("black")
    # head2.setOutline("white")
    # head2.draw(win)
    #
    # win.getMouse()
    #
    # win.close()

# def redrawBoard():
#     for x in range(0,height):
#         for y in range(0,width):
#             node = nodes[x][y]
#             drawBox(node)

def createBoard():
    for x in range(0,height):
        for y in range(0,width):
            drawBox(x, y, "light grey")

    #createStart(0,0)
    #createGoal(8,8)
    #createObstacle(0,1,6,0)
    #createObstacle(1,3,7,0)
    #createObstacle(0,5,6,0)
    #createObstacle(1,7,7,0)
    #createObstacle(0,3,0,1)

    #setHInAllNodes()


#win.getMouse()
#main()
