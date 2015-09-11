from examples import *

def aStarAlgorithm(getNeighbours):
    open = []
    closed = []

    #createBoard()
    #createDemo()
    createExample4()
    setHInAllNodes()

    startNode = getStartNode()
    startNode.g = 0

    open.append(startNode)

    while True:
        if len(open) == 0:
            print("No goal found")
            return

        currentTile = pop(open) #open.pop()
        closed.append(currentTile)
        currentTile.isTraversed = True
        drawBox(currentTile)

        if currentTile.isGoal:
            break

        succ = getNeighbours(currentTile)

        for node in succ:

            #First time node is visited
            if node not in open and node not in closed:
                node.parent = currentTile
                node.isObserved = True
                node.g = currentTile.g + 1
                open.append(node)
                drawBox(node)
            elif currentTile.g + 1 < node.g:
                node.parent = currentTile
                # node.g = currentTile.g + actual_path_cost
                node.g = currentTile.g + 1
                if node in closed:
                    propagateBetterPath(node)

    paintBestPath()


def pop(open):
    bestNode = None
    bestCost = float("inf")

    for node in open:
        cost = node.g + node.h
        if cost < bestCost:
            bestNode = node
            bestCost = cost

    open.remove(bestNode)
    return bestNode

def paintBestPath():
    t = getGoalNode()
    while t.parent is not None:
        t.isShortestPath = True
        drawBox(t)
        t = t.parent


aStarAlgorithm(getSurroundingTiles)
getWindow().getMouse()
#win.getMouse()

