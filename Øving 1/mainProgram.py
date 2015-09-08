from node import *
from board import *
from examples import *

from collections import deque #https://docs.python.org/3.1/tutorial/datastructures.html

#open = deque()
open = []
closed = []



currentTile = None

#createBoard()
#createDemo()
createExample2()
setHInAllNodes()

startNode = getStartNode()
startNode.g = 0

def getBestNode():
	bestNode = None
	bestCost = float("inf")

	for node in open:
		cost = node.g + node.h
		if(cost < bestCost):
			bestNode = node
			bestCost = cost

	open.remove(bestNode)
	return bestNode



open.append(startNode)

done = startNode.isGoal

while not done:
	if len(open) == 0:
		print("No goal found")
		break

	currentTile = getBestNode() #open.pop()
	closed.append(currentTile)
	#open.append()
	currentTile.isTravedersd = True
	drawBox(currentTile)

	succ = getSurroundingTiles(currentTile)

	for node in succ:


		if node.isGoal:
			node.parent = currentTile
			done = True
			break

		#First time node is visited
		if node not in open and node not in closed:
			node.parent = currentTile
			node.isObserved = True
			node.g = currentTile.g + 1
			open.append(node)
			drawBox(node)
		elif currentTile.g + 1 < node.g:
			print("Hello")
			node.parent = currentTile
			node.g = currentTile.g + 1
			if node in closed:
				propagateBetterPath(node)




t = getGoalNode()
while t.parent != None:
	t.isShortestPath = True
	drawBox(t)
	t = t.parent

getWindow().getMouse()
#win.getMouse()