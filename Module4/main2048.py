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
                0, 0, 0, 0
            ]

def runUp(q, board):
    #global upScore

    newBoard = slideUp(board,True)
    if newBoard is None:
        q.put(-1)
        return
    upScore = createTree(newBoard,0,1,True)
    q.put(upScore)
    #print("Up dune: ", upScore)
    return

def runDown(q, board):
    #global downScore
    newBoard = slideDown(board,True)
    if newBoard is None:
        q.put(-1)
        return

    downScore = createTree(newBoard,0,1,True) #* 0.9
    q.put(downScore)
    #print("downScore dune ", downScore)
    return

def runRight(q, board):
    #global rightScore
    newBoard = slideToTheRight(board,True)
    if newBoard is None:
        q.put(-1)
        return

    rightScore = createTree(newBoard,0,1,True)
    q.put(rightScore)
    #print("rightScore dune", rightScore)
    return

def runLeft(q, board):
    #global leftScore
    newBoard = slideToTheLeft(board,True)
    if newBoard is None:
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
        elif newBoard[cellIndex +1] == 0 or newBoard[cellIndex] == newBoard[cellIndex+1]:
            return True
        else:
            return False

    for cellIndex in [2,1,0,6,5,4,10,9,8,14,13,12]:
    # for cellIndex in [i for i in range(len(board)-1, -1, -1) if (i-3) % 4 != 0]:

        if newBoard[cellIndex] == 0:
            continue
        currentIndex = cellIndex

        while canSlideRight(currentIndex):
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
        elif newBoard[cellIndex-1] == 0 or newBoard[cellIndex] == newBoard[cellIndex-1]:
            return True
        else:
            return False

    for cellIndex in [1,2,3,5,6,7,9,10,11,13,14,15]:
    # for cellIndex in [i for i in range(1, len(board)) if i % 4 != 0]:
        if newBoard[cellIndex] == 0:
            continue
        currentIndex = cellIndex
        while canSlideLeft(currentIndex):
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
        elif newBoard[cellIndex - 4] == 0 or newBoard[cellIndex] == newBoard[cellIndex-4]:
            return True
        else:
            return False

    for cellIndex in [4,8,12,5,9,13,6,10,14,7,11,15]:
    # for cellIndex in range(4, len(board)):

        if newBoard[cellIndex] == 0:
            continue
        currentIndex = cellIndex

        while canSlideUp(currentIndex):
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
        elif newBoard[cellIndex + 4] == 0 or newBoard[cellIndex] == newBoard[cellIndex+4]:
            return True
        else:
            return False

    for cellIndex in [8,4,0,9,5,1,10,6,2,11,7,3]: #reversed(range(0,len(board)-4))
    # for cellIndex in range(len(board)-4-1, -1, -1): #reversed(range(0,len(board)-4))

        if newBoard[cellIndex] == 0:
            continue
        currentIndex = cellIndex

        while canSlideDown(currentIndex):
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
            #print("Hei")

    if not didSomethingChange and init:# and getEmptyCellsInBoard(newBoard) == 0:
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
    if getEmptyCellsInBoard(board) > 5:#and heighestScore < 12:
        maxSearchDepth = 2
    elif getEmptyCellsInBoard(board) == 2:
        maxSearchDepth = 3
    elif getEmptyCellsInBoard(board) == 1:
        maxSearchDepth = 3
    elif getEmptyCellsInBoard(board) == 0:
        maxSearchDepth = 3
    else:
        maxSearchDepth = 2

    #maxSearchDepth = 2
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

        if  (depht == 0 and  getEmptyCellsInBoard(board) <= 3 ):# or (getEmptyCellsInBoard(board) == 0):
            childBoards = createAllEmptyBoardsCombos(shiftedBoard,2)
            for child in childBoards:
                sum += createTree(child,depht +1, prob*0.1,False)

    return sum #+ getHeuristicValueForBoard(inputBoard) * prob

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

# def hei():
#     global teller
#     teller += 2
#     global board
#     newBoard = addNewCellToBoard(board)
#     if newBoard == None:
#         return
#     window.update_view( newBoard )
#     board = newBoard
#     window.after(1000,hei)
#     #time.sleep(2)




def getProbs():
    global board

    up = Queue()
    down = Queue()
    left = Queue()
    right = Queue()

    t1 = Process(target=runDown, args=(down,board))
    # t1.daemon = True
    t1.start()
    #print("runUp started")
    t2 = Process(target=runUp, args= (up,board))
    # t2.daemon = True
    t2.start()
    #print("runDown started")

    t3 = Process(target=runLeft, args= (left,board))
    # t3.daemon = True
    t3.start()
    #print("runLeft started")
    t4 = Process(target=runRight, args= (right,board))
    # t4.daemon = True
    t4.start()
    #print("runRight started")

    t1.join()  # This waits until the thread has completed
    t2.join()
    t3.join()  # This waits until the thread has completed
    t4.join()


    downScore = down.get()
    upScore = up.get()
    rightScore = right.get()
    leftScore = left.get()

    scores = [downScore,upScore,rightScore,leftScore]

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
    else:
        print("Baard is full")
        return

    window.update_view(board)
    window.after(1,getProbs)




def leftKey(event):
    global board
    print("Left key pressed")
    newBoard = slideToTheLeft(board, True)
    if newBoard == None:
        return
    board = newBoard
    board = addNewCellToBoard(board)
    window.update_view( board )

def rightKey(event):
    global board
    print("Right key pressed")
    newBoard = slideToTheRight(board, True)
    if newBoard == None:
        return
    board = newBoard
    board = addNewCellToBoard(board)
    window.update_view( board )

def upKey(event):
    global board
    print("Up key pressed")
    newBoard = slideUp(board, True)
    if newBoard == None:
        return
    board = newBoard
    board = addNewCellToBoard(board)
    window.update_view( board )

def downKey(event):
    global board
    print("Down key pressed")
    newBoard = slideDown(board, True)
    if newBoard == None:
        return
    board = newBoard
    board = addNewCellToBoard(board)
    window.update_view( board )


def spaceKey(event):
    window.after(1,getProbs)

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
    root.bind('<space>', spaceKey)
    
    root.focus_set()
    #root.pack()
    
    #createCoordList()
    window.after(1,getProbs)
    
    root.mainloop()


