__author__ = 'Anders'
def aStarAlgorithm(getNeighbours, h_func, initialState, paintSolution):

    def propagateBetterPath(node):
        possibleKids = getNeighbours(node)
        for kid in possibleKids:
            if node == kid.parent:
                kid.g = kid.parent.g + 1
                propagateBetterPath(kid)

    def pop(open):
        bestNode = None
        bestCost = float("inf")

        for node in open:
            cost = node.h
            if cost < bestCost:
                bestNode = node
                bestCost = cost

        open.remove(bestNode)
        # print("Bestnode has f=", bestCost)
        return bestNode

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

        redrawCounter += 1
        #if redrawCounter % 10 == 0:
        paintSolution(currentTile)
        print(currentTile.h)

        closed.append(currentTile)

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

