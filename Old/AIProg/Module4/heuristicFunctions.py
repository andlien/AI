from main2048 import *#slideDown, slideToTheLeft, slideToTheRight, slideUp

cords = []
for y in range(0,4):
    for x in range(0,4):
        cords.append([y,x])


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



def getHeuristicValueForBoard(board):
    sum = 0

    largestCell = getLargestCellInBoard(board)
    if isCellInCorner(largestCell):
        sum += board[largestCell] ** 2

        # snake
        sum += getSnakeScore(board, largestCell)

    for cell in range(0, len(board)):
        sum += compareToCellsAround(cell, board)

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
    # if emptyCells == 0:
    #     #teller = isBoardStuck(board)
    #     emptyCells += 1/teller

    sum += emptyCells * 15
    if sum < 0:
        sum = 0


    return sum
#def areTheFourLargestTilesOnTheSameRow(board):


#

def getSnakeScoreForBoardList(board):
    sum = 0
    returnList = []

    largestCell = getLargestCellInBoard(board)
    if isCellInCorner(largestCell):
        return getSnakeScoreList(board, largestCell)
    return [0]*3


def getSnakeScoreForBoard(board):
    sum = 0
    largestCell = getLargestCellInBoard(board)

    if isCellInCorner(largestCell):
        sum += board[largestCell] ** 2

        # snake
        sum += getSnakeScore(board, largestCell)



    return sum

def getAScoreForCellsAround(board):
    sum =0
    for cell in range(0, len(board)):
        sum += compareToCellsAround(cell, board)

    return sum


def getAScoreForCellsAroundList(board):
    returnList1 = 0
    returnList2 = 0
    returnList3 = 0
    returnList4 = 0
    sortedBoard = list(board)
    sortedBoard.sort()
    for cell in range(0, 3):
        returnList1 += compareToCellsAround(sortedBoard[cell], board)
    for cell in range(3, 8):
        returnList2 += compareToCellsAround(sortedBoard[cell], board)
    for cell in range(8, 11):
        returnList3 += compareToCellsAround(sortedBoard[cell], board)
    for cell in range(11, len(board)):
        returnList4 += compareToCellsAround(sortedBoard[cell], board)
    return returnList1,returnList2,returnList3,returnList4

def getIndeciesForList(board):
    sortedBoard = list(board)
    sortedBoard.sort()
    indices = []
    for sortedCell in sortedBoard:
        for index in range(0,len(board)):
            if sortedCell == board[index] and index not in indices:
                indices.append(index)


    return indices

def getSnakeScoreList(board, largestCell):
    sum = 0
    returnList = [0.0]*3
    neighbours = getNeighbourCells(largestCell)
    if board[neighbours[0]] > board[neighbours[1]]:
        diff = largestCell - neighbours[0]
        lastSnakeCell = neighbours[1]
    else:
        diff = largestCell - neighbours[1]
        lastSnakeCell = neighbours[0]
    #first snakerow
    for i in range(1, 4):
        if board[largestCell-(i-1)*diff] < board[largestCell-i*diff]:
            break
        if board[largestCell-(i-1)*diff] == board[largestCell-i*diff]:
            continue
        sum += ((board[largestCell-i*diff] * 2) ** 2)
        returnList[0] +=((board[largestCell-i*diff] * 2) ** 2)
    #second snakerow
    else:
        nextRowStart = lastSnakeCell - diff * 3

        if board[nextRowStart] < board[largestCell-3*diff]:
            sum += ((board[nextRowStart] * 2) ** 2)
            returnList[1] +=((board[largestCell-i*diff] * 2) ** 2)
            diff = -diff
            for i in range(1, 4):
                if board[nextRowStart-(i-1)*diff] < board[nextRowStart-i*diff]:
                    break
                if board[nextRowStart-(i-1)*diff] == board[nextRowStart-i*diff]:
                    continue
                sum += ((board[nextRowStart-i*diff] * 2) ** 2)
                returnList[2] +=((board[nextRowStart-i*diff] * 2) ** 2)
    return returnList

def getSnakeScore(board, largestCell):
    sum = 0
    #returnList = []
    neighbours = getNeighbourCells(largestCell)
    if board[neighbours[0]] > board[neighbours[1]]:
        diff = largestCell - neighbours[0]
        lastSnakeCell = neighbours[1]
    else:
        diff = largestCell - neighbours[1]
        lastSnakeCell = neighbours[0]
    #first snakerow
    for i in range(1, 4):
        if board[largestCell-(i-1)*diff] < board[largestCell-i*diff]:
            break
        if board[largestCell-(i-1)*diff] == board[largestCell-i*diff]:
            continue
        sum += ((board[largestCell-i*diff] * 2) ** 2)
       # returnList.append(((board[largestCell-i*diff] * 2) ** 2))
    #second snakerow
    else:
        nextRowStart = lastSnakeCell - diff * 3

        if board[nextRowStart] < board[largestCell-3*diff]:
            sum += ((board[nextRowStart] * 2) ** 2)
            #returnList.append(((board[nextRowStart] * 2) ** 2))
            diff = -diff
            for i in range(1, 4):
                if board[nextRowStart-(i-1)*diff] < board[nextRowStart-i*diff]:
                    break
                if board[nextRowStart-(i-1)*diff] == board[nextRowStart-i*diff]:
                    continue
                sum += ((board[nextRowStart-i*diff] * 2) ** 2)
                #eturnList.append(((board[nextRowStart-i*diff] * 2) ** 2))
    return sum

def isGreatestTileInCorner(board):
    largestCell = getLargestCellInBoard(board)
    if isCellInCorner(largestCell):
        return 1
    return 0

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


def greatestCellInCornerSingle(board):
    largestCell = getLargestCellInBoard(board)
    if largestCell in [0,3,12,15]:
        return largestCell/16
    return 0


def greatestCellInCorner(board):
    largestCell = getLargestCellInBoard(board)
    sum = [0,0,0,0]
    corners = [0,3,12,15]
    if largestCell in corners:
        for i in range(3):
            if corners[i] == largestCell:
               sum[i] = 1
               #print(sum)
    else:
        if largestCell in [1,4]:
            sum[0] += 0.5
        if largestCell in [2,7]:
            sum[1] += 0.5
        if largestCell in [8,13]:
            sum[2] += 0.5
        if largestCell in [14,11]:
            sum[3] += 0.5
    return sum

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
            if cell == 0:
                sum += 1


    return sum

def scanRows(board):
    startIndex = 0
    sum = 0
    for row in range(0,3):
        lista = []
        for index in [0,4,8,12]:
            cell = board[row+index]
            if cell == 0:
                sum += 1

    return sum


def compareToCellsAround(cell ,board):
    sum = 0
    for nabo in getNeighbourCells(cell):
        if board[nabo] == board[cell]:
            sum += board[cell] + 1
            # sum += 2 ** board[cell]
        elif (board[nabo] -1 == board[cell] ) and board[cell] > 0:
            sum +=0.1
        elif board[nabo] == 0:
            sum += 0.1
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