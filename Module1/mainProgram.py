from Module1.board import *
from time import sleep
from Module1.aStarProgram import aStarAlgorithm

def paintPath(t):

    surr = getSurroundingTiles(t)

    newPaint = [None] * (width * height)

    sleep(0.1)

    if t.isGoal():
        #Do not paint goalstate
        t = t.parent

    if t is Node.startNode:
        return

    while t.parent is not None:
        newPaint[t.x * height + t.y] = "todraw"
        t = t.parent

    for posFront in surr:
        if lastpaint[posFront.x * height + posFront.y] is None and not posFront.isGoal():
            newPaint[posFront.x * height + posFront.y] = "front"

    for x in range(width):
        for y in range(height):
            if newPaint[x * height + y] == "front":
                drawBox(x, y, "dark grey")
                lastpaint[x * height + y] = "drawn"
            elif lastpaint[x * height + y] == "shortdrawn" and newPaint[x * height + y] is None:
                drawBox(x, y, "grey")
                lastpaint[x * height + y] = "drawn"
            elif newPaint[x * height + y] == "todraw" and lastpaint[x * height + y] != "shortdrawn":
                drawBox(x, y, "dark red")
                lastpaint[x * height + y] = "shortdrawn"




possibleModes = ["astar", "bfs", "dfs"]

while True:


    mode = input("Specify mode, one of [Astar, BFS, DFS]: ").lower()
    while mode not in possibleModes:
        mode = input("Wrong input, specify one of [Astar, BFS, DFS]: ")

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

    startAndGoal = f.readline().split()
    createStart(int(startAndGoal[0]), int(startAndGoal[1]))
    createGoal(int(startAndGoal[2]), int(startAndGoal[3]))

    block = f.readline()
    while block != '':
        block = block.split()
        createObstacle(int(block[0]), int(block[1]), int(block[2]), int(block[3]))
        block = f.readline()

    f.close()

    lastpaint = [None] * (width * height)

    mPop = None
    mHfunc = manhattenDistToGoalNode
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

    aStarAlgorithm(getSurroundingTiles, mHfunc, Node.startNode, paintPath, pop=mPop)
    getWindow().getMouse()
    getWindow().close()



