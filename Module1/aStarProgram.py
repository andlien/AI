
# A* algorithm, fairly similar to the psudocode
def aStarAlgorithm(getNeighbours,
                   h_func,
                   initialState,
                   paint,
                   pop=None,
                   arcCost=None):

    # Default method from the psudocode
    def propagateBetterPath(node):
        possibleKids = getNeighbours(node)
        for kid in possibleKids:
            if node == kid.parent:
                kid.g = kid.parent.g + arcCost(node, kid)
                propagateBetterPath(kid)

    # If custom functions are not defined, go default
    if pop is None:
        pop = standardPop
    if arcCost is None:
        def arcCost(node1, node2):
            return 1

    open = []
    closed = []

    startNode = initialState
    startNode.g = 0
    startNode.h = h_func(startNode)

    # Counters to display at the end
    numberOfNodesGenerated = 0
    numberOfNodesExpanded = 0

    open.append(startNode)

    redrawCounter = 0

    while True:
        if len(open) == 0:
            print("No goal found")
            return currentTile

        currentTile = pop(open) #open.pop()
        numberOfNodesExpanded = numberOfNodesExpanded + 1

        paint(currentTile)

        closed.append(currentTile)

        if currentTile.isGoal():

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
                kid.g = currentTile.g + arcCost(currentTile, kid)
                kid.h = h_func(kid)
                open.append(kid)

            elif currentTile.g + arcCost(currentTile, kid) < kid.g:
                kid.parent = currentTile
                kid.g = currentTile.g + arcCost(currentTile, kid)
                if kid in closed:
                    propagateBetterPath(kid)

# Pops the best element from the open list
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
