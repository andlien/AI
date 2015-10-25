from Module4.main2048 import slideDown, slideToTheLeft, slideToTheRight, slideUp

cords = []
for y in range(0,4):
    for x in range(0,4):
        cords.append([y,x])

def getHeuristicValueForBoard22(board):
    sum = 0
    sum += getEmptyCellsInBoard(board) * 3
    #optimalBoard = [3,2,1,0,4,5,6,7,11,10,9,8,12,13,14,15]
    #optimalBoard.reverse()


    sortedIndex = getIndeciesForList(board)
    largetCell = getLargestCellInBoard(board)

    if isCellInCorner(largetCell):
        sum += 2
    #print(sortedIndex)
    for i in range(1,int(len(sortedIndex)/2)):
        if board[sortedIndex[i]] <= 3:
            break
        c1 = sortedIndex[i-1]
        c1 = largetCell
        c2 = sortedIndex[i]

        #print("Dist: ", getDistance(c2,c1))

        sum += (1 / (1 + getDistance(c2,c1))**2)

    if getEmptyCellsInBoard(board) <= 1:
        teller = isBoardStuck(board)
        #sum -= teller
        if (teller > 1):
            #print("Board is stuck")
            sum /= (teller)

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


def getHeuristicValueForBoard(board):
    sum = 0
    #optimalBoard = [3,2,1,0,4,5,6,7,11,10,9,8,12,13,14,15]
    #optimalBoard.reverse()
    # sortedIndex = getIndeciesForList(board)
    # if sortedIndex[0] == 15:
    #     sum += 10
    #     if sortedIndex[1] == 14:
    #         sum += 10
    #         if sortedIndex[2] == 13:
    #             sum += 10
    #         if sortedIndex[3] == 12:
    #             sum += 10
    #

    sum += (getEmptyCellsInBoard(board))# ** 2

    if sum <= 1:
        teller = isBoardStuck(board)
        sum += 1/teller

    # largetCell = getLargestCellInBoard(board)
    # if isCellInCorner(largetCell):
    #     sum += 2
    return sum

def getHeuristicValueForBoard55(board):
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

def getHeuristicValueForBoard2(board):
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

def getHeuristicValueForBoard3(board):
    sum = getEmptyCellsInBoard(board)*100
    if isCellInCorner(getLargestCellInBoard(board)):
        sum += 100*getLargestCellInBoard(board)

    for cell in board:
        if cell > 2:
            sum += cell

    return sum

def getIndeciesForList(board):
    sortedBoard = list(board)
    sortedBoard.sort()
    indices = []
    for sortedCell in sortedBoard:
        for cell in board:
            if sortedCell == cell and cell not in indices:
                indices.append(cell)


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