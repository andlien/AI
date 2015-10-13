def getHeuristicValueForBoard(board):
    sum = getEmptyCellsInBoard(board)
    if isCellInCorner(getLargestCellInBoard(board)):
        sum += 100

    for cell in board:
        sum += cell

    return sum

def isCellInCorner(cell):
    if cell in [0,3,12,15]:
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
    for cell in xrange(0,len(board)):
        if board[cell] > largestValue:
            largestValue = board[cell]
            cellWithLargestValue = cell


    return cellWithLargestValue