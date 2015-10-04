__author__ = 'Simen'
from graphics import *

height = 9
width = 9
size = 40


def getWindow():
    return win

def setDimensions(x,y):
    global width
    global height
    global win
    width = x
    height = y

    numberOfNodes = height * width

    win = GraphWin('Nonograms*', x*size+5, y*size+5 + 100)


def drawBox(x,y,value):
    head2 = Rectangle(Point(x*size +5,height*size - y*size - size+5), Point( x*size + size+5,height*size - y*size +5)) # set center and radius
    if value == 0:
         head2.setFill("dark grey")
         head2.setOutline("dark grey")
    elif value == 1:
         head2.setFill("dark red")
         head2.setOutline("dark red")
    #
    #head2.setOutline("black")
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