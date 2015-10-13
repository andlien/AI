from visuals import GameWindow
from Tkinter import *
from random import randint
import time

teller = 0

root = Tk()
#root.geometry("250x150+300+300")
#app = GameWindow()


#main.mainloop()


#frame = Frame(width=768, height=576, bg="", colormap="new")
window = GameWindow()

board = [   # A list of values currently present in the board on the form 2^x.
            # Eg: the number 4 implies that the graphical board should display,
            # 2^4 = 16, the digit 16. This board represents the board in the screen dump below.
            0, 1, 2, 3,
            4, 5, 6, 7,
            8, 9, 10, 11,
            12, 13, 14, 15
        ]

board = [   # A list of values currently present in the board on the form 2^x.
            # Eg: the number 4 implies that the graphical board should display,
            # 2^4 = 16, the digit 16. This board represents the board in the screen dump below.
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0
        ]
def slideToTheRight(board):
    newBoard = list(board)
    print("Board: " , newBoard)

    def canSlideRight(cellIndex):
        if cellIndex in [3,7,11,15]:
            return False
        elif cellIndex < 0:
            return False
        elif newBoard[cellIndex +1] == 0:
            return True
        else:
            return False

    for cellIndex in reversed(xrange(0,len(board)-2)):

        if newBoard[cellIndex] == 0:
            continue
        currentIndex = cellIndex

        while canSlideRight(currentIndex) or newBoard[currentIndex] == newBoard[currentIndex+1]:
            if newBoard[currentIndex] == newBoard[currentIndex+1]:
                newBoard[currentIndex+1] += 1
                newBoard[currentIndex] = 0
                print("Stacked!")
                break #According to ios version, a cell can only stack ones per slide
            else:
                newBoard[currentIndex+1] = newBoard[currentIndex]
                newBoard[currentIndex] = 0
            currentIndex = currentIndex+1
            if currentIndex == 15:
                break
            #print("Hei")

    return newBoard

def slideToTheLeft(board):
    newBoard = list(board)

    def canSlideLeft(cellIndex):
        if cellIndex in [0,4,8,12]:
            return False
        elif cellIndex < 0:
            return False
        elif newBoard[cellIndex -1] == 0:
            return True
        else:
            return False

    for cellIndex in xrange(0,len(board)):
        if newBoard[cellIndex] == 0:
            continue
        currentIndex = cellIndex
        while canSlideLeft(currentIndex) or newBoard[currentIndex] == newBoard[currentIndex-1]:
            if newBoard[currentIndex] == newBoard[currentIndex-1]:
                newBoard[currentIndex-1] += 1
                newBoard[currentIndex] = 0
                print("Stacked!")
                break #According to ios version, a cell can only stack ones per slide
            else:
                newBoard[currentIndex-1] = newBoard[currentIndex]
                newBoard[currentIndex] = 0
            currentIndex = currentIndex-1
            print("Hei")

    return newBoard

def slideUp(board):
    newBoard = list(board)

    def canSlideUp(cellIndex):
        if cellIndex in [0,1,2,3]:
            return False
        elif cellIndex < 0:
            return False
        elif newBoard[cellIndex - 4] == 0:
            return True
        else:
            return False

    for cellIndex in xrange(4,len(board)):

        if newBoard[cellIndex] == 0:
            continue
        currentIndex = cellIndex

        while canSlideUp(currentIndex) or newBoard[currentIndex] == newBoard[currentIndex-4]:
            if newBoard[currentIndex] == newBoard[currentIndex-4]:
                newBoard[currentIndex-4] += 1
                newBoard[currentIndex] = 0
                print("Stacked!")
                break #According to ios version, a cell can only stack ones per slide
            else:
                newBoard[currentIndex-4] = newBoard[currentIndex]
                newBoard[currentIndex] = 0
            currentIndex = currentIndex-4
            if currentIndex < 4:
                break
            print("Hei")

    return newBoard


def slideDown(board):
    newBoard = list(board)

    def canSlideDown(cellIndex):
        if cellIndex in [12,13,14,15]:
            return False
        elif cellIndex < 0:
            return False
        elif newBoard[cellIndex + 4] == 0:
            return True
        else:
            return False

    for cellIndex in [8,4,0,9,5,1,10,6,2,11,7,3]: #reversed(xrange(0,len(board)-4))

        if newBoard[cellIndex] == 0:
            continue
        currentIndex = cellIndex

        while canSlideDown(currentIndex) or newBoard[currentIndex] == newBoard[currentIndex+4]:
            if newBoard[currentIndex] == newBoard[currentIndex+4]:
                newBoard[currentIndex+4] += 1
                newBoard[currentIndex] = 0
                print("Stacked!")
                break #According to ios version, a cell can only stack ones per slide
            else:
                newBoard[currentIndex+4] = newBoard[currentIndex]
                newBoard[currentIndex] = 0
            currentIndex = currentIndex+4
            if currentIndex >= 12:
                break
            #print("Hei")

    return newBoard

def addNewCellToBoard(board):
    cell = getRandomOpenCellInBoard(board)
    if cell == -1:
        print("Baard is full")
        return None

    prob = randint(0,100)
    print("Prob: ",prob)
    newBoard = list(board)

    if prob > 90:
        newBoard[cell] = 2
    else:
       newBoard[cell] = 1

    return newBoard

def getRandomOpenCellInBoard(board):
    openCells = []
    for cell in xrange(0,len(board)):
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


board = addNewCellToBoard(board)
board = slideDown(board)
window.update_view( board ) # 1D list representing the board
#window.after(1000,hei)


def leftKey(event):
    global board
    print "Left key pressed"
    newBoard = slideToTheLeft(board)
    board = newBoard
    board = addNewCellToBoard(board)
    window.update_view( board )

def rightKey(event):
    global board
    print "Right key pressed"
    newBoard = slideToTheRight(board)
    board = newBoard
    board = addNewCellToBoard(board)
    window.update_view( board )

def upKey(event):
    global board
    print "Up key pressed"
    newBoard = slideUp(board)
    board = newBoard
    board = addNewCellToBoard(board)
    window.update_view( board )

def downKey(event):
    global board
    print "Down key pressed"
    newBoard = slideDown(board)
    board = newBoard
    board = addNewCellToBoard(board)
    window.update_view( board )

#frame = Frame(main, width=100, height=100)
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)
root.focus_set()
#root.pack()

root.mainloop()


