from Module1.examples import *
from time import sleep

def aStarAlgorithm(getNeighbours, h_func, initialState, paintSolution):
    open = []
    closed = []

    startNode = initialState
    startNode.g = 0
    startNode.h = h_func(startNode)

    open.append(startNode)

    redrawCounter = 0

    while True:
        if len(open) == 0:
            print("No goal found")
            return

        currentTile = pop(open) #open.pop()
        # print("open has", len(open))
        # print("closed has", len(closed))


        if redrawCounter % 100 == 0:
            paintSolution(currentTile)
        #     paintBestPathFromcurrentNode(currentTile)
        #     #sleep(0.005)
        #     dedrawBestPathFromcurrentNode(currentTile)

        redrawCounter +=1


        closed.append(currentTile)
        # currentTile.isTraversed = True
        # drawBox(currentTile.x, currentTile.y, "grey")
        #redrawBoard()

        if currentTile.isGoal():
            paintSolution(currentTile)
            print("GOAAAAAL")
            break

        succ = getNeighbours(currentTile)

        for kid in succ:
            #First time node is visited
            if kid not in open and kid not in closed:
                kid.parent = currentTile
                # kid.isObserved = True
                kid.g = currentTile.g + 1
                kid.h = h_func(kid)
                open.append(kid)

                # drawBox(kid.x, kid.y, "dark grey")
                # drawBox(kid)
            elif currentTile.g + 1 < kid.g:
                kid.parent = currentTile
                # node.g = currentTile.g + actual_path_cost
                kid.g = currentTile.g + 1
                if kid in closed:
                    propagateBetterPath(kid)



def pop(open):
    bestNode = None
    bestCost = float("inf")

    for node in open:
        cost = node.g + node.h
        if cost < bestCost:
            bestNode = node
            bestCost = cost

    open.remove(bestNode)
    # print("Bestnode has f=", bestCost)
    return bestNode

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
# aStarAlgorithm(getSurroundingTiles, manhattenDistToGoalNode, Node.startNode, paintBestPath)
# getWindow().getMouse()
#win.getMouse()


