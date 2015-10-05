from Module3.Variable import *
from Module3.nonogramGraphics import *
from Module3.nonoState import *
from random import randint
from Module2.aStarGacProgram import *

#Custom function used to generate domain for a variable
def createDomainRecursive(currentDomain,remaningPlaces, restrictions, returnList):
    for i in range(0,2): #Block can either be blank(0) or filled with the next block
        updatedDomain = currentDomain.copy()
        updatedRestrictions = restrictions.copy()

        if(i == 0): # Empty space here
            updatedDomain.append(0)
        else:
            for etTall in range(0,updatedRestrictions[0]):
                updatedDomain.append(1)
            updatedRestrictions.pop(0) #Removes the block

        if ((remaningPlaces == len(currentDomain) and len(updatedRestrictions) > 0) or remaningPlaces +1 < len(updatedDomain)):
            #Not a valid domain
            continue

        elif( len(updatedRestrictions) == 0): #Reached end of domain and the domain is valid. Returning it
            for index in range(0,(remaningPlaces+1) - len(updatedDomain)):
                updatedDomain.append(0)
            returnList.append(updatedDomain)
            #Domain created. Adding it to the list

        else:
            if(i == 1): #Adding the divider between blocks
                updatedDomain.append(0)
            if remaningPlaces > len(currentDomain): #Not done with the domain yet. We have to go deeper!
                createDomainRecursive(updatedDomain,remaningPlaces,updatedRestrictions,returnList)



# Custom function that draws the nonogram on the GUI
def drawNonoGramState(state):
    for var in range(0,len(state.vertices)):
        row = state.vertices[var]
        if row.isAssumed:
            for val in range(0,len(row.domain[0])):
                drawBox(val,var, row.domain[0][val])





#Custom revise used for Nonograms. Almost identical to the normal revise
def nonoGramRevise(constraints, vertex1,vertex2):

        revised = False
        if constraints[vertex1.index][vertex2.index] is None:
                return False

        for d1 in vertex1.domain:
                domainChanged = False
                for d2 in vertex2.domain:
                        for const in constraints[vertex1.index][vertex2.index]:
                                # This line is the only change to the general Revise
                                #Only comparing the intersection between the row and column, not the whole domain
                                if d1[vertex2.coord] == const[0] and d2[vertex1.coord] == const[1]:
                                    domainChanged = True

                if not domainChanged:
                        vertex1.domain.remove(d1)
                        revised = True

        return revised

#Not in use anymore
#def paintStatus(generated, expandend,solutionPath):
#    drawInfoText(generated, expandend,solutionPath)

while True:

    while True:
        prompt = input("Please type in the path to your file and press 'Enter': ")
        try:
            f = open(prompt + ".txt", 'r')
        except FileNotFoundError:
            print("Wrong file or file path")
        else:
            break


    firstLine = f.readline()
    values = ( firstLine.split( ) )

    numberOfColumns= int(values[0])
    numberOfRows= int(values[1])
    print("")
    print("numberOfRows: " + str(numberOfRows))
    print("numberOfColumns: " + str(numberOfColumns))
    print("")

    rowsAndColumns = []

    setDimensions( numberOfColumns, numberOfRows ) # inits the GUI

    constraints = []

    for line in range(0,numberOfRows):

            intValues = [int(i) for i in f.readline().split()]

            index = line

            coord =  numberOfRows - line -1

            row = Variable(index,coord)

            constraints.append({})

            domene = []
            tempDomain = []

            createDomainRecursive(tempDomain,numberOfColumns-1,intValues,domene)

            row.domain = domene
            rowsAndColumns.append(row)
            for column in range(0,numberOfColumns):
                constraints[index][column + numberOfRows] = [[0,0], [1,1]]

    print("Created all rows")

    for line2 in range(0,numberOfColumns):
            intValues = [int(i) for i in f.readline().split()]
            index = line2 + numberOfRows

            coord = line2
            row = Variable(index,coord)

            constraints.append({})

            domene = []
            tempDomain = []

            createDomainRecursive(tempDomain,numberOfRows-1,intValues,domene)
            row.domain = domene
            rowsAndColumns.append(row)
            for row in range(0,numberOfRows):
                constraints[index][row] = [[0,0], [1,1]]

    print("Created all columns")
    print("")
    f.close()

    aStarGAC(3, rowsAndColumns, constraints, drawNonoGramState, GAC_Revise=nonoGramRevise)
    getWindow().getMouse()
    getWindow().close()
