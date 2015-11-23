__author__ = 'simen'

from heuristicFunctions import *
import math

def convertBoardToBinary(board):
    newBoard = []
    for tile in board:
        if tile > 0:
            #newBoard.append(1)
            newBoard.append(tile/12)
            #newBoard.append(math.log(tile)+1)
        else:
            newBoard.append(0)

    # newBoard.sort()
    return newBoard





def numberThatCanSlideUp(newBoard):
    sum = 0
    sortedIndex = getIndeciesForList(newBoard)
    sortedIndex.reverse()
    for i in range(16):
        cellIndex = sortedIndex[i]
        if cellIndex in [12,13,14,15] or newBoard[cellIndex] <= 3:
            sum +=0
        elif cellIndex < 0:
            sum +=0
        elif  newBoard[cellIndex + 4] == 0 or newBoard[cellIndex] == newBoard[cellIndex+4]:
            sum +=1
        else:
            sum +=0
    return sum/16


def numberThatCanSlideDown(newBoard):
    sum = 0
    sortedIndex = getIndeciesForList(newBoard)
    sortedIndex.reverse()
    for i in range(16):
        cellIndex = sortedIndex[i]
        if cellIndex in [0,1,2,3] or newBoard[cellIndex] <= 3:
            sum +=0
        elif cellIndex < 0:
            sum +=0
        elif  (newBoard[cellIndex - 4] == 0 or newBoard[cellIndex] == newBoard[cellIndex-4]):
            sum +=1
        else:
            sum +=0
    return sum/16

def numberThatCanSlideRight(newBoard):
    sum = 0
    sortedIndex = getIndeciesForList(newBoard)
    sortedIndex.reverse()
    for i in range(16):
        cellIndex = sortedIndex[i]
        if cellIndex in [3,7,11,15] or newBoard[cellIndex] <= 3:
            sum +=0
        elif cellIndex < 0:
            sum +=0
        elif  (newBoard[cellIndex+1] == 0 or newBoard[cellIndex] == newBoard[cellIndex+1]):
            sum +=1
        else:
            sum +=0
    return sum/16

def numberThatCanSlideLeft(newBoard):
    sum = 0
    sortedIndex = getIndeciesForList(newBoard)
    sortedIndex.reverse()
    for i in range(16):
        cellIndex = sortedIndex[i]
        if cellIndex in [0,4,8,12] or newBoard[cellIndex] <= 3:
            sum +=0
        elif cellIndex < 0:
            sum +=0
        elif  (newBoard[cellIndex-1] == 0 or  newBoard[cellIndex] == newBoard[cellIndex-1]):
            sum +=1
        else:
            sum +=0


    return sum/16


def isBoardToBig(board):
    cell = getLargestCellInBoard(board)
    if board[cell] >= 11:
        return True
    return False

def getBiggestTiles(board):
    returnList = [0]*11
    currentTile = 1
    for biggerTile in range(11):
        for tile in board:
            if tile == biggerTile +1:
                returnList[biggerTile] = (biggerTile+1)/12
                break

    return returnList

def getAbstractBoard(board):
    returnList = []#convertBoardToBinary(board)

    #MIX
    # returnList.append( getEmptyCellsInBoard(board) )
    # returnList.append( getAScoreForCellsAround(board) )
    # returnList.append((getLargestCellInBoard(board)))
    # returnList.append((getSnakeScoreForBoard(board)) )
    # returnList.append(getHeuristicValueForBoard(board))
    # returnList.append(isGreatestTileInCorner(board))
    # returnList += greatestCellInCorner(board)
    # returnList += getBiggestTiles(board)
    # returnList += getAScoreForCellsAroundList(board)
    # returnList += getSnakeScoreForBoardList(board)




    #returnList.append(scanColumns(board))
    #returnList.append(scanRows(board))

    # returnList.append(numberThatCanSlideRight(board))
    # returnList.append(numberThatCanSlideLeft(board))
    # returnList.append(numberThatCanSlideUp(board))
    # returnList.append(numberThatCanSlideDown(board))
    #returnList.append(greatestCellInCorner(board))




    #Snake
    returnList += getSnakeScoreForBoardList(board)
    returnList.append(getHeuristicValueForBoard(board))
    returnList += getBiggestTiles(board)
    #returnList += getAScoreForCellsAroundList(board)
    returnList += greatestCellInCorner(board)
    returnList.append((getSnakeScoreForBoard(board)) )






    return returnList
