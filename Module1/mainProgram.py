from Module1.board import *
from time import sleep
from Module1.aStarProgram import aStarAlgorithm

# Paints the board
# While executing the search algorithm, the shortest path to the currently processed node is shown
def paintBoard(t):
    global lastpaint
    surr = getSurroundingTiles(t)

    newPaint = [None] * (width * height)

    sleep(0.02)

    #Do not paint goalstate
    if t.isGoal():
        t = t.parent

    # do not paint startnode
    if t is Node.startNode:
        return

    # The states to be painted dark red
    while t.parent is not None:
        newPaint[t.x * height + t.y] = "todrawshort"
        t = t.parent

    # The states to be painted as the frontier
    for posFront in surr:
        if lastpaint[posFront.x * height + posFront.y] is None and not posFront.isGoal():
            newPaint[posFront.x * height + posFront.y] = "front"

    # Paint what needs to be painted
    for x in range(width):
        for y in range(height):
            if newPaint[x * height + y] == "front":
                drawBox(x, y, "dark grey")
                lastpaint[x * height + y] = "visited"
            # Is already painted short, but are no longer -> must already be visited
            elif lastpaint[x * height + y] == "shortdrawn" and newPaint[x * height + y] is None:
                drawBox(x, y, "grey")
                lastpaint[x * height + y] = "visited"
            # Paint nodes that should be short, but aren't already, red
            elif newPaint[x * height + y] == "todrawshort" and lastpaint[x * height + y] != "shortdrawn":
                drawBox(x, y, "dark red")
                lastpaint[x * height + y] = "shortdrawn"


possibleModes = ["astar", "bfs", "dfs"]

while True:

    # Get input from the user which mode to use
    mode = input("Specify mode, one of [Astar, BFS, DFS]: ").lower()
    while mode not in possibleModes:
        mode = input("Wrong input, specify one of [Astar, BFS, DFS]: ")

    # Get input from the user which file to use
    while True:
        prompt = input("Please type in the path to your file and press 'Enter': ")
        try:
            f = open(prompt + ".txt", 'r')
        except FileNotFoundError:
            print("Wrong file or file path")
        else:
            break

    width, height = [int(i) for i in f.readline().split()]
    setDimensions(width, height)

    createBoard()

    startAndGoal = [int(i) for i in f.readline().split()]
    createStart(startAndGoal[0], startAndGoal[1])
    createGoal(startAndGoal[2], startAndGoal[3])

    block = f.readline()
    while block != '':
        block = [int(i) for i in block.split()]
        createObstacle(block[0], block[1], block[2], block[3])
        block = f.readline()

    f.close()

    lastpaint = [None] * (width * height)

    mPop = None
    mHfunc = euclideanDistToGoalNode

    # Define custom functions if dfs or bfs
    if mode == "dfs":
        def mPop(open):
            return open.pop()
        def mHfunc(node):
            return 0
    elif mode == "bfs":
        def mPop(open):
            return open.pop(0)
        def mHfunc(node):
            return 0

    aStarAlgorithm(getSurroundingTiles, mHfunc, Node.startNode, paintBoard, pop=mPop)
    getWindow().getMouse()
    getWindow().close()



