from graphics import *
from random import randint
from Module2.cspVertex import *


height = 9
width = 9
size = 1

redrawCounter = 0
runningStrings = ["Running   ","Running.  ","Running.. ","Running...","Running...."]

isCentreInTheMidle = False

def getWindow():
    return win

def setDimensions(numberOfVertices):
    global width
    global height
    global win
    global size
    global isCentreInTheMidle

    isCentreInTheMidle = True
    size = 400/numberOfVertices
    size = 0.03
    width = 900
    height = 1000

    if numberOfVertices < 99:
        size = 10
        width = 900
        height = 900
        isCentreInTheMidle = False
    elif numberOfVertices < 150:
        size = 7
        width = 900
        height = 900
        isCentreInTheMidle = False



    numberOfNodes = height * width

    win = GraphWin('A*', height+5, width+5)





def drawVertex(vertex, fancyBorder):
    #head2 = Rectangle(Point(node.x*size +5,height*size - node.y*size - size+5), Point( node.x*size + size+5,height*size - node.y*size +5)) # set center and radius
    #head2 = Circle(Point(vertex.x*size, vertex.y*size), 5)


    if isCentreInTheMidle:
         head2 = Circle(Point(vertex.x*size + 25 + height/2 ,width/2 - vertex.y*size), 5)
    else:
         head2 = Circle(Point(vertex.x*size + 200  , vertex.y*size + 200), 5)

    if vertex.isAssumed():
        head2.setFill(vertex.getColor())
    else:
        head2.setFill("white")

    if fancyBorder:
        head2.setOutline("black")
    else:
        head2.setOutline("grey")
    #head2.setOutline("black")
    head2.setOutline("grey")
    head2.draw(win)


def drawEdge(vertex1,vertex2):
    #head2 = Rectangle(Point(node.x*size +5,height*size - node.y*size - size+5), Point( node.x*size + size+5,height*size - node.y*size +5)) # set center and radius
    #head2 = Circle(Point(vertex.x*size, vertex.y*size), 5)
    head2 = Line(Point(vertex1.x*size + 25 + height/2 ,width/2 - vertex1.y*size), Point(vertex2.x*size + 25 + height/2 ,width/2 - vertex2.y*size))

    if isCentreInTheMidle:
         head2 = Line(Point(vertex1.x*size + 25 + height/2 ,width/2 - vertex1.y*size), Point(vertex2.x*size + 25 + height/2 ,width/2 - vertex2.y*size))
    else:
         head2 = Line(Point(vertex1.x*size + 200 , vertex1.y*size+ 200 ), Point(vertex2.x*size + 200  , vertex2.y*size+ 200 ))



    color = 90 + randint(1, 100) #Varies the color on edges to make them easier to distinguish

    head2.setOutline(color_rgb(color, color, color))
    head2.setWidth(1)
    head2.draw(win)


def drawInfoText(generated, expandend,solutionPath):
    label = Text(Point(110, 30), 'Nodes generated: ' + str(generated))
    label.setSize(20)
    label.draw(win)

    label = Text(Point(110, 60), 'Nodes expanded: ' + str(expandend))
    label.setSize(20)
    label.draw(win)

    label = Text(Point(140, 90), 'Nodes in solutions path: ' + str(solutionPath))
    label.setSize(20)
    label.draw(win)