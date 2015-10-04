__author__ = 'Anders'
def aStarAlgorithm(getNeighbours, h_func, initialState, paint, pop=None):

    def propagateBetterPath(node):
        possibleKids = getNeighbours(node)
        for kid in possibleKids:
            if node == kid.parent:
                kid.g = kid.parent.g + 1
                propagateBetterPath(kid)

    if pop is None:
        pop = standardPop

    open = []
    closed = []

    startNode = initialState
    startNode.g = 0
    startNode.h = h_func(startNode)

    numberOfNodesGenerated = 0
    numberOfNodesExpanded = 0



    open.append(startNode)

    redrawCounter = 0

    while True:
        if len(open) == 0:
            print("No goal found")
            return

        currentTile = pop(open) #open.pop()
        numberOfNodesExpanded = numberOfNodesExpanded + 1

        redrawCounter += 1
        #if redrawCounter % 10 == 0:
        paint(currentTile)

        closed.append(currentTile)

        if currentTile.isGoal():
            print("GOAAAAAL")

            numberOfNodesInSolutionPath = 1
            t = currentTile
            while t.parent is not None:
                numberOfNodesInSolutionPath = numberOfNodesInSolutionPath + 1
                t = t.parent

            print("")
            print("A* finished")
            print("Total number of search nodes generated: ", numberOfNodesGenerated)
            print("Total number of search nodes expanded: ", numberOfNodesExpanded)
            print("Total number of search nodes on the path from the root to the solution state.: ", numberOfNodesInSolutionPath)

            return currentTile

        succ = getNeighbours(currentTile)
        numberOfNodesGenerated = numberOfNodesGenerated + len(succ)


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

def standardPop(open):
    bestNode = None
    bestCost = float("inf")

    for node in open:
        cost = node.h + node.g
        if cost < bestCost:
            bestNode = node
            bestCost = cost

    open.remove(bestNode)
    # print("Bestnode has f=", bestCost)
    return bestNode
