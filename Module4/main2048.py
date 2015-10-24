from Module4.visuals import GameWindow
from tkinter import *
from random import randint
from Module4.heuristicFunctions import *
from multiprocessing import Process, Queue
import time


board = [   # A list of values currently present in the board on the form 2^x.
                # Eg: the number 4 implies that the graphical board should display,
                # 2^4 = 16, the digit 16. This board represents the board in the screen dump below.
                0, 0, 0, 0,
                0, 0, 0, 0,
                0, 0, 0, 0,
                0, 1, 2, 2
            ]

def runUp(q):
    #global upScore

    newBoard = slideUp(board,True)
    if newBoard == None:
        q.put(-1)
        return
    upScore = createTree(newBoard,0,1,True)
    q.put(upScore)
    #print("Up dune: ", upScore)
    return

def runDown(q):
    #global downScore
    newBoard = slideDown(board,True)
    if newBoard == None:
        q.put(-1)
        return

    downScore = createTree(newBoard,0,1,True)
    q.put(downScore)
    #print("downScore dune ", downScore)
    return

def runRight(q):
    #global rightScore
    newBoard = slideToTheRight(board,True)
    if newBoard == None:
        q.put(-1)
        return

    rightScore = createTree(newBoard,0,1,True)
    q.put(rightScore)
    #print("rightScore dune", rightScore)
    return

def runLeft(q):
    #global leftScore
    newBoard = slideToTheLeft(board,True)
    if newBoard == None:
        q.put(-1)
        return

    leftScore = createTree(newBoard,0,1,True)
    q.put(leftScore)
    #print("leftScore dune ", leftScore)
    return



def slideToTheRight(board,init):
    newBoard = list(board)
    #print("Board: " , newBoard)
    didSomethingChange = False

    def canSlideRight(cellIndex):
        if cellIndex in [3,7,11,15]:
            return False
        elif cellIndex < 0:
            return False
        elif newBoard[cellIndex +1] == 0:
            return True
        else:
            return False

    for cellIndex in reversed(range(0,len(board)-1)):

        if newBoard[cellIndex] == 0:
            continue
        currentIndex = cellIndex

        while canSlideRight(currentIndex) or newBoard[currentIndex] == newBoard[currentIndex+1]:
            if newBoard[currentIndex] == newBoard[currentIndex+1]:
                newBoard[currentIndex+1] += 1
                newBoard[currentIndex] = 0
                didSomethingChange = True
                #print("Stacked!")
                break #According to ios version, a cell can only stack ones per slide
            else:
                didSomethingChange = True
                newBoard[currentIndex+1] = newBoard[currentIndex]
                newBoard[currentIndex] = 0
            currentIndex = currentIndex+1
            if currentIndex == 15:
                break
            #print("Hei")

    if not didSomethingChange and init:# and getEmptyCellsInBoard(newBoard) == 0:
        #print("Dead end!!!")
        return None
    return newBoard

def slideToTheLeft(board,init):
    newBoard = list(board)
    didSomethingChange = False
    def canSlideLeft(cellIndex):
        if cellIndex in [0,4,8,12]:
            return False
        elif cellIndex < 0:
            return False
        elif newBoard[cellIndex -1] == 0:
            return True
        else:
            return False

    for cellIndex in range(0,len(board)):
        if newBoard[cellIndex] == 0:
            continue
        currentIndex = cellIndex
        while canSlideLeft(currentIndex) or newBoard[currentIndex] == newBoard[currentIndex-1]:
            if newBoard[currentIndex] == newBoard[currentIndex-1]:
                newBoard[currentIndex-1] += 1
                newBoard[currentIndex] = 0
                didSomethingChange = True
                #print("Stacked!")
                break #According to ios version, a cell can only stack ones per slide
            else:
                newBoard[currentIndex-1] = newBoard[currentIndex]
                didSomethingChange = True
                newBoard[currentIndex] = 0
            currentIndex = currentIndex-1
            #print("Hei")

    if not didSomethingChange and init:# and :
        #print("Dead end!!!")
        return None
    return newBoard

def slideUp(board,init):
    newBoard = list(board)
    didSomethingChange = False
    def canSlideUp(cellIndex):
        if cellIndex in [0,1,2,3]:
            return False
        elif cellIndex < 0:
            return False
        elif newBoard[cellIndex - 4] == 0:
            return True
        else:
            return False

    for cellIndex in range(4,len(board)):

        if newBoard[cellIndex] == 0:
            continue
        currentIndex = cellIndex

        while canSlideUp(currentIndex) or newBoard[currentIndex] == newBoard[currentIndex-4]:
            if newBoard[currentIndex] == newBoard[currentIndex-4]:
                newBoard[currentIndex-4] += 1
                newBoard[currentIndex] = 0
                didSomethingChange = True
                #print("Stacked!")
                break #According to ios version, a cell can only stack ones per slide
            else:
                newBoard[currentIndex-4] = newBoard[currentIndex]
                newBoard[currentIndex] = 0
                didSomethingChange = True
            currentIndex = currentIndex-4
            if currentIndex < 4:
                break
            #print("Hei")

    if not didSomethingChange and init:# and getEmptyCellsInBoard(newBoard) == 0:
        #print("Dead end!!!")
        return None
    return newBoard


def slideDown(board,init):
    #print("Baard: " , board)
    newBoard = list(board)
    didSomethingChange = False

    def canSlideDown(cellIndex):
        if cellIndex in [12,13,14,15]:
            return False
        elif cellIndex < 0:
            return False
        elif newBoard[cellIndex + 4] == 0:
            return True
        else:
            return False

    for cellIndex in [8,4,0,9,5,1,10,6,2,11,7,3]: #reversed(range(0,len(board)-4))

        if newBoard[cellIndex] == 0:
            continue
        currentIndex = cellIndex

        while canSlideDown(currentIndex) or newBoard[currentIndex] == newBoard[currentIndex+4]:
            if newBoard[currentIndex] == newBoard[currentIndex+4]:
                newBoard[currentIndex+4] += 1
                newBoard[currentIndex] = 0
                didSomethingChange = True
                #print("Stacked!")
                break #According to ios version, a cell can only stack ones per slide
            else:
                newBoard[currentIndex+4] = newBoard[currentIndex]
                newBoard[currentIndex] = 0
                didSomethingChange = True
            currentIndex = currentIndex+4
            if currentIndex >= 12:
                break
            #print("Hei")

    if not didSomethingChange and init:# and getEmptyCellsInBoard(newBoard) == 0:
        #print("Dead end!!!")
        return None
    return newBoard

def addNewCellToBoard(board):
    cell = getRandomOpenCellInBoard(board)
    if cell == -1:
        print("Baard is full")
        return None

    prob = randint(0,100)
    #print("Prob: ",prob)
    newBoard = list(board)

    if prob > 90:
        newBoard[cell] = 2
    else:
       newBoard[cell] = 1

    return newBoard




def createTree(inputBoard, depht, prob, init):
    global maxSearchDepth
    if getEmptyCellsInBoard(board) > 4:
        maxSearchDepth = 2
    elif getEmptyCellsInBoard(board) == 2:
        maxSearchDepth = 2
    elif getEmptyCellsInBoard(board) <= 1:
        maxSearchDepth = 3
    else:
        maxSearchDepth = 2
    sum = 0
    if maxSearchDepth <= depht:
        return getHeuristicValueForBoard(inputBoard) * prob
    for direction in range(0,4):
        if init:
            shiftedBoard = inputBoard
        elif direction == 0:
            shiftedBoard = slideDown(inputBoard,False)
        elif direction == 1:
            shiftedBoard = slideUp(inputBoard,False)
        elif direction == 2:
            shiftedBoard = slideToTheRight(inputBoard,False)
        else:
            shiftedBoard = slideToTheLeft(inputBoard,False)

        if shiftedBoard is None:
            break

        #print("shiftedBoard: ", shiftedBoard)
        childBoards = createAllEmptyBoardsCombos(shiftedBoard,1)
        #print("childBoards:",childBoards)
        for child in childBoards:
            sum += createTree(child,depht +1, prob*0.9, False)

        if  depht == 0 and  getEmptyCellsInBoard(board) <= 2:
            childBoards = createAllEmptyBoardsCombos(shiftedBoard,2)
            for child in childBoards:
                sum += createTree(child,depht +1, prob*0.1,False)

    return sum

def createAllEmptyBoardsCombos(board,value):
    openCells = []
    for cell in range(0,len(board)):
        if board[cell] == 0:
            #for value in [1,2]:
            newBoard = list(board)
            newBoard[cell] = value
            openCells.append(newBoard)

    return openCells

def getRandomOpenCellInBoard(board):
    openCells = []
    for cell in range(0,len(board)):
        if board[cell] == 0:
            openCells.append(cell)
    if len(openCells) == 0:
        return -1
    return openCells[randint(0,len(openCells)-1)]

def hei():
    global teller
    teller += 2
    global board
    newBoard = addNewCellToBoard(board)
    if newBoard == None:
        return
    window.update_view( newBoard )
    board = newBoard
    window.after(1000,hei)
    #time.sleep(2)




def getProbs():
    global board

    global upScore
    # global downScore,leftScore,rightScore
    # downScore = createTree(slideDown(board),0,1)
    # upScore = createTree(slideUp(board),0,1)
    # rightScore = createTree(slideToTheRight(board),0,1)
    # leftScore = createTree(slideToTheLeft(board),0,1)
    #print("Down: ", down)
    #print("Up: ", up)
    #print("Right: ", right)
    #print("Left: ", left)



    up = Queue()
    down = Queue()
    left = Queue()
    right = Queue()

    t1 = Process(target=runUp, args=(up,))
    t1.daemon = True
    t1.start()
    #print("runUp started")
    t2 = Process(target=runDown, args= (down,))
    t2.daemon = True
    t2.start()
    #print("runDown started")

    t3 = Process(target=runLeft, args= (left,))
    t3.daemon = True
    t3.start()
    #print("runLeft started")
    t4 = Process(target=runRight, args= (right,))
    t4.daemon = True
    t4.start()
    #print("runRight started")

    t1.join()  # This waits until the thread has completed
    t2.join()
    t3.join()  # This waits until the thread has completed
    t4.join()

    #print("All threads finished?")

    upScore = up.get()
    downScore=down.get()
    rightScore=right.get()
    leftScore=left.get()

    scores = [downScore,upScore,rightScore,leftScore]

    # bestScore = downScore
    # bestNumber = 0
    # teller = 1
    print("Scores: ", scores)
    # for dir in [upScore,rightScore,leftScore]:
    #     if dir > bestScore:
    #         bestScore = dir
    #         bestNumber = teller
    #     teller += 1

    bestNumber = scores.index(max(scores))

    if bestNumber == 0:
        newBoard = slideDown(board,True)
    if bestNumber == 1:
        newBoard = slideUp(board,True)
    if bestNumber == 2:
        newBoard = slideToTheRight(board,True)
    if bestNumber == 3:
        newBoard = slideToTheLeft(board,True)

    if not newBoard is None:
        board = newBoard
        largestTile = newBoard[getLargestCellInBoard(board)]

        global heighestScore
        global start
        if largestTile > heighestScore:
            heighestScore = largestTile
            if 2 ** largestTile >= 512:
                print("New highest tile: " + str(2 ** largestTile) + " - " + str((time.time() - start)/60) + " min")
            else:
                print("New highest tile: " + str(2 ** largestTile) + " - " + str(time.time() - start) + " sec")

        board = addNewCellToBoard(board)

    window.update_view( board )
    window.after(1,getProbs)




def leftKey(event):
    global board
    print("Left key pressed")
    newBoard = slideToTheLeft(board, False)
    board = newBoard
    board = addNewCellToBoard(board)
    window.update_view( board )

def rightKey(event):
    global board
    print("Right key pressed")
    newBoard = slideToTheRight(board, False)
    board = newBoard
    board = addNewCellToBoard(board)
    window.update_view( board )

def upKey(event):
    global board
    print("Up key pressed")
    newBoard = slideUp(board, False)
    board = newBoard
    board = addNewCellToBoard(board)
    window.update_view( board )

def downKey(event):
    global board
    print("Down key pressed")
    newBoard = slideDown(board, False)
    board = newBoard
    board = addNewCellToBoard(board)
    window.update_view( board )

if __name__ == '__main__':
    
    teller = 0
    
    root = Tk()
    
    maxSearchDepth = 3
    #root.geometry("250x150+300+300")
    #app = GameWindow()
    upScore = 0
    downScore = 0
    leftScore = 0
    rightScore = 0
    
    createCoordList()
    heighestScore = 0
    start = time.time()


    window = GameWindow()


    board = addNewCellToBoard(board)
    #board = slideDown(board)
    window.update_view( board ) # 1D list representing the board
    #window.after(1000,hei)
    
    #frame = Frame(main, width=100, height=100)
    root.bind('<Left>', leftKey)
    root.bind('<Right>', rightKey)
    root.bind('<Up>', upKey)
    root.bind('<Down>', downKey)
    root.bind('<space>', getProbs)
    
    root.focus_set()
    #root.pack()
    

    
    #createCoordList()
    window.after(1,getProbs)
    
    root.mainloop()


