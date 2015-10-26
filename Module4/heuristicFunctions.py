from Module4.main2048 import slideDown, slideToTheLeft, slideToTheRight, slideUp
from math import log

cords = []
for y in range(0,4):
    for x in range(0,4):
        cords.append([y,x])


def getHeuristicValueForBoard3243(board):
    sum = 0
    sum += (getEmptyCellsInBoard(board) + 1) *10
    optimalBoard = [3,2,1,0,4,5,6,7,11,10,9,8,12,13,14,15]
    optimalBoard.reverse()
    sortedIndex = getIndeciesForList(board)
    sortedIndex.reverse()
    for cell in range(0, len(board)):
        if board[cell] <= 0:
            continue

        c1 = optimalBoard[cell]
        c2 = sortedIndex[cell]

        sum += ((1 / (1 + getDistance(c2,c1)))) #* (32 - cell*2))

    return sum

def getHeuristicValueForBoard900(board):
    sum = 0
    sum += (getEmptyCellsInBoard(board) + 1)
    #optimalBoard = [3,2,1,0,4,5,6,7,11,10,9,8,12,13,14,15]
    #optimalBoard.reverse()


    sortedIndex = getIndeciesForList(board)
    sortedIndex.reverse()
    largetCell = getLargestCellInBoard(board)

    if isCellInCorner(largetCell):
        sum += 20
    #print(sortedIndex)
    for i in range(1,int(len(sortedIndex))):
        if board[sortedIndex[i]] <= 2:
              break
        c1 = sortedIndex[i-1]
        #c1 = largetCell
        c2 = sortedIndex[i]
        #sum += board[c1]

        #print("Dist: ", getDistance(c2,c1))

        #sum += ((1 / (1 + getDistance(c2,c1))**2) * (16-i) ) * 0.5
        dist = getDistance(c2,c1)
        if dist == 1 and not board[c1] == board[c2]:
            #print("skjer ofte")
            sum += 1
        elif dist == 1:
            sum += 0.5
        elif dist == 2:
            sum += 0.2
        #
        # if not board[c1] == board[c2]:
        #     sum += ((1 / (1 + getDistance(c2,c1))**2) * (32-i))

        #c1 = largetCell
        #sum += ( (1 / (1 + getDistance(c2,c1))**2) * (16-i) ) * 0.5

    if getEmptyCellsInBoard(board) <= 0:
        teller = isBoardStuck(board)
        sum += 1/teller

    return sum


def isBoardStuck(board):
    teller = 1
    newBoard = slideUp(board,True)
    if newBoard == None:
        teller += 1
    newBoard = slideDown(board,True)
    if newBoard == None:
        teller += 1
    newBoard = slideToTheLeft(board,True)
    if newBoard == None:
        teller += 1
    newBoard = slideToTheRight(board,True)
    if newBoard == None:
        teller += 1

    return teller


def getHeuristicValueForBoard345(board):
    sum = 0
    #optimalBoard = [3,2,1,0,4,5,6,7,11,10,9,8,12,13,14,15]
    #optimalBoard.reverse()
    sortedIndex = getIndeciesForList(board)
    if sortedIndex[0] == 15:
        sum += 1
        if sortedIndex[1] == 14:
            sum += 2
            if sortedIndex[2] == 13:
                sum += 3
            if sortedIndex[3] == 12:
                sum += 4


    sum += (getEmptyCellsInBoard(board))# ** 2

    if sum <= 1:
        teller = isBoardStuck(board)
        sum += 1/teller

    # largetCell = getLargestCellInBoard(board)
    # if isCellInCorner(largetCell):
    #     sum += 2
    return sum

def getHeuristicValueForBoard4322(board):
    sum = getEmptyCellsInBoard(board)
    sortedBoard = list(board)
    sortedBoard.sort()
    #print("sortedBoard ", sortedBoard)
    largetCell = getLargestCellInBoard(board)
    #print(largetCell)


    sortedIndex = getIndeciesForList(board)
    #print(sortedIndex)
    for i in range(1,len(sortedIndex)):
        if board[sortedIndex[i]] < 4:
            break
        c1 = sortedIndex[i-1]
        c1 = largetCell
        c2 = sortedIndex[i]

        #print("Dist: ", getDistance(c2,c1))

        sum += (1 / (1 + getDistance(c2,c1))**2) * board[sortedIndex[i]]*20


    for x in range(0,len(board)-1):
        if sortedBoard[x] <= 3:
            break
        if sortedBoard[x] == sortedBoard[x-1]:
            sum -= 0#sortedBoard[x] ** 2
        else:
            sum += sortedBoard[x] ** 2


    if isCellInCorner(largetCell):
        sum += board[largetCell] ** 2
    else:
        sum -= 0#board[largetCell] ** 2

    return sum

def getHeuristicValueForBoard2222(board):
    sum = getEmptyCellsInBoard(board) * 20
    sortedBoard = list(board)
    sortedBoard.sort()
    #print("sortedBoard ", sortedBoard)
    largetCell = getLargestCellInBoard(board)
    #print(largetCell)

    if isCellInCorner(largetCell):
        sum += 100*getLargestCellInBoard(board)
        # close = getCellsCloseToCorners(largetCell)
        # if board[close[0]] == sortedBoard[1] or board[close[0]] == sortedBoard[2]:
        #     sum += sortedBoard[1] * 50
        # if board[close[1]] == sortedBoard[1] or board[close[1]] == sortedBoard[2]:
        #     sum += sortedBoard[1] * 50

        sortedIndex = getIndeciesForList(board)
        #print(sortedIndex)
        for i in range(1,len(sortedIndex)):
            if board[sortedIndex[i]] < 4:
                break
            c1 = sortedIndex[i-1]
            c1 = largetCell
            c2 = sortedIndex[i]

            #print("Dist: ", getDistance(c2,c1))

            sum += (1 / (1 + getDistance(c2,c1))**2) * board[sortedIndex[i]]*20
            #print((1 / 1 + getDistance(c2,c1)**2) * 2000)

    for cell in board:
        if cell > 2:
            sum += cell**2


    return sum


def getHeuristicValueForBoard34234(board):
    sum = 0#getEmptyCellsInBoard(board)
    sortedIndex = getIndeciesForList(board)
    #print(sortedIndex)
    if sortedIndex[0] == 15:
        print("Ja, det skjer");
        sum += 1
        if sortedIndex[1] == 14:
            sum += 1

    # for i in range(1,len(sortedIndex)):
    #     if board[sortedIndex[i]] < 4:
    #         break
    #     c1 = sortedIndex[i-1]
    #     c1 = largetCell
    #     c2 = sortedIndex[i]
    #
    #     #print("Dist: ", getDistance(c2,c1))
    #
    #     sum += (1 / (1 + getDistance(c2,c1))**2) * board[sortedIndex[i]]*20

    return sum


def getHeuristicValueForBoard666(board):
    sum = getEmptyCellsInBoard(board)
    if isCellInCorner(getLargestCellInBoard(board)):
        sum += 2

    # for cell in board:
    #     if cell > 2:
    #         sum += cell

    return sum



def getHeuristicValueForBoard(board):
    sum = 0#getEmptyCellsInBoard(board)*20
    #sum = getEmptyCellsInBoard(board)*20
    #sum += 2 ** board[getLargestCellInBoard(board)]

    if isCellInCorner(getLargestCellInBoard(board)):
        sum += board[getLargestCellInBoard(board)] ** 2

    for cell in range(0, len(board)):
        sum += compareToCellsAround(cell, board)

    #sum += scanColumns(board)
    #sum += scanRows(board)

    sortedIndex = getIndeciesForList(board)
    sortedIndex.reverse()
    for cell in range(0, 15):
        if board[sortedIndex[cell]] <= 2:
             break
        if sortedIndex[cell] in [5,6,9,10] and cell <= 6:
            sum -= board[sortedIndex[cell]] ** 2
        if board[sortedIndex[cell]] == board[sortedIndex[cell+1]]:
            sum -= board[sortedIndex[cell]] * (getDistance(sortedIndex[cell],sortedIndex[cell+1]) -1)

        c1 = sortedIndex[cell+1]
        c1 = getLargestCellInBoard(board)
        c2 = sortedIndex[cell]

        #print("Dist: ", getDistance(c2,c1))

        sum += (1 / (1 + getDistance(c2,c1))**2) * board[sortedIndex[cell]]
            #if getDistance(sortedIndex[cell],sortedIndex[cell+1]) > 1:
                #sum -= board[sortedIndex[cell]]
            #sum += board[sortedIndex[cell]]


    emptyCells = getEmptyCellsInBoard(board)
    if emptyCells == 0:
        teller = isBoardStuck(board)
        emptyCells += 1/teller

    sum += emptyCells * 15
    if sum < 0:
        sum = 0


    return sum
#def areTheFourLargestTilesOnTheSameRow(board):



def getIndeciesForList(board):
    sortedBoard = list(board)
    sortedBoard.sort()
    indices = []
    for sortedCell in sortedBoard:
        for index in range(0,len(board)):
            if sortedCell == board[index] and index not in indices:
                indices.append(index)


    return indices






def getDistance(cell1, cell2):
    #cords = createCoordList()
    global cords
    c1 = cords[cell1]
    c2 = cords[cell2]
    return abs(c2[0]-c1[0]) + abs(c2[1]-c1[1])

def isCellInCorner(cell):
    if cell in [0,3,12,15]:
        return True
    return False

            # 0, 1, 2, 3,
            # 4, 5, 6, 7,
            # 8, 9, 10, 11,
            # 12, 13, 14, 15

def getCellsCloseToCorners(cornerCell):
    if cornerCell == 15:
        return [14,11]
    if cornerCell == 12:
        return [8,13]
    if cornerCell == 0:
        return [1,4]
    if cornerCell == 3:
        return [2,7]
    return [0]

def getNeighbourCells(cell):
    if cell == 0:
        return [1,4]
    elif cell == 3:
        return [2,7]
    elif cell == 12:
        return [8,13]
    elif cell == 15:
        return [11,14]
    elif cell in [1,2]:
        return [cell-1, cell+1,cell +4]
    elif cell in [4,8]:
        return [cell-4, cell+4,cell +1]
    elif cell in [7,11]:
        return [cell-4, cell-1,cell +4]
    elif cell in [13,14]:
        return [cell-4, cell-1,cell +1]
    else:
        return [cell -4, cell + 4, cell +1, cell -1]


def scanColumns(board):
    startIndex = 0
    sum = 0
    for row in [0,4,8,12]:
        lista = []
        for index in range(0,3):
            cell = board[row+index]
            if cell not in lista:
                lista.append(cell)

        sum += ( (1/len(lista)))
    return sum

def scanRows(board):
    startIndex = 0
    sum = 0
    for row in range(0,3):
        lista = []
        for index in [0,4,8,12]:
            cell = board[row+index]
            if cell not in lista:
                lista.append(cell)

        sum += ((1/len(lista)))
    return sum


def compareToCellsAround(cell ,board):
    sum = 0
    if board[cell] == 0:
        return 2
    for nabo in getNeighbourCells(cell):
        if board[nabo] == board[cell]:
            sum += board[cell] ** 2
            # sum += 2 ** board[cell]
        elif (board[nabo] -1 == board[cell] or board[nabo] -1 == board[cell] -1) and board[cell] > 0:
            sum +=1
        elif board[nabo] == 0:
            sum += 2
        else:
            sum -= 0#board[cell]
    return sum

def punishEqualCellsThatAreFarAway(board):
    sortedIndex = getIndeciesForList(board)
    sortedIndex.reverse()
    # for si in range(0,len(board)):


def isCellCloseToCornerCell(cell,cornerCell):
    if cornerCell == 15:
        if cell in [14,11]:
            return True
    if cornerCell == 12:
        if cell in [8,13]:
            return True
    if cornerCell == 0:
        if cell in [1,4]:
            return True
    if cornerCell == 3:
        if cell in [2,7]:
            return True

    return False

def getEmptyCellsInBoard(board):
    numberOfEmptyCells = 0
    for cell in board:
        if cell == 0:
            numberOfEmptyCells += 1

    return numberOfEmptyCells

def getLargestCellInBoard(board):
    largestValue = 0
    cellWithLargestValue = -1
    for cell in range(0,len(board)):
        if board[cell] > largestValue:
            largestValue = board[cell]
            cellWithLargestValue = cell


    return cellWithLargestValue