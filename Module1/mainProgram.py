from Module1.examples import *
from time import sleep
from Module2.cspGrid import getWindow
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


createExample2()
aStarAlgorithm(getSurroundingTiles, manhattenDistToGoalNode, Node.startNode, paintBestPath)
# getWindow().getMouse()
#win.getMouse()


