from Module4.main2048 import slideDown, slideToTheLeft, slideToTheRight, slideUp

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

def getSnakeScore(board, largestCell):
    sum = 0
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
    #second snakerow
    else:
        nextRowStart = lastSnakeCell - diff * 3

        if board[nextRowStart] < board[largestCell-3*diff]:
            sum += ((board[nextRowStart] * 2) ** 2)
            diff = -diff
            for i in range(1, 4):
                if board[nextRowStart-(i-1)*diff] < board[nextRowStart-i*diff]:
                    break
                if board[nextRowStart-(i-1)*diff] == board[nextRowStart-i*diff]:
                    continue
                sum += ((board[nextRowStart-i*diff] * 2) ** 2)
    return sum




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