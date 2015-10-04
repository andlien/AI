from Module1.examples import *
from time import sleep
from Module1.board import getWindow
from Module1.aStarProgram import aStarAlgorithm

def paintBestPath(t):
    while t.parent is not None:
        t.isShortestPath = True
        #drawBox(t)
        drawShortestPathNode(t.x, t.y)
        t = t.parent

def paintBestPathFromcurrentNode(currentNode):
    t = currentNode
    while t.parent is not None:
        drawShortestPathNode(t.x, t.y)
        t = t.parent

def dedrawBestPathFromcurrentNode(currentNode):
    t = currentNode
    while t.parent is not None:
        drawBox(t)
        t = t.parent


# createExample2()

# f = open('example0.txt', 'r')
# f = open('example1.txt', 'r')
# f = open('example2.txt', 'r')
# f = open('example3.txt', 'r')
# f = open('example4.txt', 'r')
f = open('example5.txt', 'r')

dim = f.readline().split()
setDimensions(int(dim[0]), int(dim[1]))

createBoard()

startAndGoal = f.readline().split()
createStart(int(startAndGoal[0]), int(startAndGoal[1]))
createGoal(int(startAndGoal[2]), int(startAndGoal[3]))

block = f.readline()
while block != '':
    block = block.split()
    createObstacle(int(block[0]), int(block[1]), int(block[2]), int(block[3]))
    block = f.readline()

f.close()

aStarAlgorithm(getSurroundingTiles, manhattenDistToGoalNode, Node.startNode, paintBestPath)
getWindow().getMouse()
#win.getMouse()


