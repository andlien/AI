__author__ = 'simen'

from Module6.createAbstractBoard import *



def listFromNumber(number):
	return list(map(lambda x: (number >> x*4) & 0xf, range(16)))

def convertDirectionToIndex(direction):
    if direction == "d":
        # newBoard = slideDown(board,True)
        return 0
    elif direction == "u":
        # newBoard = slideUp(board,True)
        return 1
    elif direction == "r":
        # newBoard = slideToTheRight(board,True)
        return 2
    elif direction == "l":
        # newBoard = slideToTheLeft(board,True)
        return 3
    else:
        print("Direction not found!!!!")



def getTrainingData():
    f = open("training-data.txt", 'r')
    trainingInput = []
    trainingOutput = []

    testingInput = []
    testingOutput = []

    teller = 0
    print("Reading data")
    for line in f:
        firstLine = line.split(", ")
        # firstLine = f.readline().split(", ")
        index = convertDirectionToIndex( firstLine[1].rstrip() )
        index = firstLine[1].rstrip()
        covertedIndex = convertDirectionToIndex(index)


        convertedBoard = listFromNumber(int(firstLine[0].rstrip()))
        if isBoardToBig(convertedBoard):
            #print("Aborting")
            continue

        convertedBoard = getAbstractBoard(convertedBoard)

        trainingOutput.append(covertedIndex)
        trainingInput.append(convertedBoard)

        #print(teller)
        teller += 1
        # if teller > 5000:
        #    break
        # if teller % 100 == 0 and False:
        #     testingOutput.append(covertedIndex)
        #     testingInput.append(convertedBoard)
        # else:
        #if teller % 100 == 0 or True:
        trainingOutput.append(covertedIndex)
        trainingInput.append(convertedBoard)

    return trainingInput, trainingOutput, testingInput, testingOutput



# for line in f:
#     firstLine = f.readline().split(", ")
#     index = convertDirectionToIndex( firstLine[1].rstrip() )
#     testingOutput.append(index)
#     testingOutput.append(listFromNumber(int(firstLine[0].rstrip())))
#     #print(listFromNumber(int(firstLine[0].rstrip())))
#     #print(teller)
#     teller += 1


#print(trainingInput[0]," should be ", trainingOutput[0])

#print(str(firstLine[1]).rstrip() )