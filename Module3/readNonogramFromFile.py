from Variable import *
from nonogramGraphics import *
from nonoState import *
from random import randint

#f = open('nono-rabbit.txt', 'r')
#f = open('nono-sailboat.txt4', 'r')
#f = open('nono-camel.txt', 'r')
#f = open('nono-heart-1.txt', 'r')
f = open('test2.txt', 'r')
#f = open('nono-cat.txt', 'r')

#f = open('nono-telephone.txt', 'r')
#f = open('nono-chick.txt', 'r')


# while True:
#     prompt = input("Please type module number and press 'Enter': ")
#
#     if prompt == '1':
#         print("Module 1 selected")
#         break
#
#     elif prompt == '2':
#         print("Module 2 selected")
#         break
#     elif prompt == '3':
#         print("Module 1 selected")
#         break
#     else:
#         print("Module number not valid. Try again")
#
#
#
#
# while True:
#     prompt = input("Please type in the path to your file and press 'Enter': ")
#     try:
#         f = open(prompt + ".txt", 'r')
#     except FileNotFoundError:
#         print("Wrong file or file path")
#     else:
#         break

#print (f)

firstLine = f.readline()
values = ( firstLine.split( ) )

numberOfColumns= int(values[0])
numberOfRows= int(values[1])
print("")
print("numberOfRows: " + str(numberOfRows))
print("numberOfColumns: " + str(numberOfColumns))
print("")

rowsAndColumns = []
rows = []
columns = []

setDimensions( numberOfColumns, numberOfRows )

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




#setDimensions(numberOfVertices)
contraints = []

for line in range(0,numberOfRows):
        vertLine = f.readline()

        values = ( vertLine.split( ) )
        intValues = []
        for v in range(0,len(values)):
            intValues.append(int(values[v]))
        index = line

        coord =  numberOfRows - line -1

        row = Variable(index,coord,1)

        contraints.append({})

        domene = []
        tempDomain = []

        createDomainRecursive(tempDomain,numberOfColumns-1,intValues,domene)

        row.domain = domene
        #print(domene)
        rowsAndColumns.append(row)
        for column in range(0,numberOfColumns):
            contraints[index][column + numberOfRows] = [[0,0], [1,1]]

print("Created all rows")

for line2 in range(0,numberOfColumns):
        vertLine = f.readline()
        values = ( vertLine.split( ) )
        intValues = []
        for v in range(0,len(values)):
            intValues.append(int(values[v]))
        index = line2 + numberOfRows

        coord = line2
        row = Variable(index,coord,2)

        contraints.append({})

        domene = []
        tempDomain = []

        createDomainRecursive(tempDomain,numberOfRows-1,intValues,domene)
        row.domain = domene
        rowsAndColumns.append(row)
        for row in range(0,numberOfRows):
            contraints[index][row] = [[0,0], [1,1]]


# if d2[var1.coord] == d1[var2.coord]:

print("Created all columns")
print("")

#for c in contraints:
    #print(c)

def drawState(state):
    for var in range(0,numberOfRows):
        row = state.vertices[var]
        if row.isAssumed or True:
            for val in range(0,len(row.domain[0])):
                drawBox(val,var, row.domain[0][val])




#drawState()






#Initialization
queue = []


for line in range(0,numberOfRows + numberOfColumns):
        queue.append(rowsAndColumns[line])

def revise(vertex1,vertex2):
        revised = False
        toBeRemoved = []
        index = 0

        #print("vertex1.index: " + str(vertex1.index))
        #print("vertex.domain lengde: " +str(vertex1.index)+ " - " + str(len(vertex1.domain)))
        if contraints[vertex1.index][vertex2.index] is None:
                print("Breaking revise")
                return False

        for d1 in vertex1.domain:


                domainChanged = False
                #print("Var witj index " + str(vertex1.index))
                #print("Comparing element: " + str(vertex2.coord) + "(its value is "+ str(d1[vertex2.coord]) + ") in row: " + str(d1))
                for d2 in vertex2.domain:
                        for const in contraints[vertex1.index][vertex2.index]:

                        #print("d1[" + str(vertex2.coord) + "/" + str(len(d1)-1) + "]. D2[" + str( vertex1.coord) + "/"+ str(len(d2)-1) +"]")
                        #print("Comparing: " + str(d1[vertex2.coord]) + " with " + str(d2[vertex1.coord]))
                        #if d1[vertex2.coord] ==  d2[vertex1.coord]:
                                if d1[vertex2.coord] == const[0] and d2[vertex1.coord] == const[1]:
                                #print("ITs equal")
                                    domainChanged = True
                                        #print("Puh, found a valid domain")
                        #else:
                            #print("Matching " + str(vertex1.coord) + " with " + str(vertex2.coord))
                            #print("Mismatch ///////////////////////////////////////////////////////")
                            #print(d1)
                            #print(d2)
                            #print("End ///////////////////////////////////////////////////////")

                if not domainChanged:

                        #print("Doamin to " +str(vertex1.index) +  str(vertex1.domain) + ". Removing: " + d1)
                        #print("removing a domain from " + str(vertex1.index) + ". Is " + str(vertex1.rowOrColumn))

                        #print("Domain before: " + str(vertex1.domain))
                        #print("Domain to be removed: " + str(d1) + " from " + str(vertex1.index))

                        #vertex1.domain.remove(d1)
                        vertex1.domain.pop(index)
                        if index not in toBeRemoved:
                            toBeRemoved.append(d1)
                        if len(vertex1.domain) == 0:
                            print("Lengden av domenet er 0!!!!!!!!!!!")
                            return


                       #print("Domain after: " + str(vertex1.domain))
                        #print("Doamin to " +str(vertex1.index)+  str(vertex1.domain))
                        #print("vertex.domain lengde: " + str(len(vertex1.domain)) + " for vertex " + str(vertex1.index) + " fordi den krasjer med " + str(vertex2.index))
                        revised = True
                        #getWindow().getMouse()
                index = index +1
                #print("-")

        # for i in toBeRemoved:
        #     print("Popping domain with index " + str(i) + ". Domain lenght is " + str(len(vertex1.domain)))
        #     vertex1.domain.remove(i)
        #     if len(vertex1.domain) == 0:
        #             print("Lengden av domenet er 0!!!!!!!!!!!")

        return revised

#The Domain-Filtering Loop
def domainFiltering(queue, stateVertices):

        while len(queue) >= 1:

                todoReviseVertex = queue.pop(0)
                for const in contraints[todoReviseVertex.index]:
                        neighbour = stateVertices[const]

                        change = revise(todoReviseVertex,neighbour)
                        if change:
                                for v5 in contraints[todoReviseVertex.index]:
                                        if stateVertices[v5] not in queue:
                                                queue.append(stateVertices[v5])
                                        #else:
                                            #print(" hei hei he hei ih ihasd asdad a sd ")



def generateSuccesorStates(vertices):
        newStates = []

        for vertex in vertices:
                if not vertex.isAssumed():
                        for color in vertex.domain:
                                index = vertex.index
                                state = nonoState(vertices)
                                state.vertices[index].domain = [color]
                                state.lastModifiedVertex = state.vertices[index]
                                newStates.append(state)


        return newStates







# contraints = []
# contraints.append({})
# contraints.append({})
# contraints[0][1] = [[0,0], [1,1]]
# contraints[1][0] = [[0,0], [1,1]]
#
# print("row")
# row = Variable(0,2,1)
# domene = []
# tempDomain = []
# hei(tempDomain,10-1,[2,1,3],domene)
# row.domain = list(reversed(domene))
#
# print(row.domain)
# print("Lenge: " + str(len(row.domain)))
#
#
# print("Column")
# column = Variable(1,6,2)
# domene = []
# tempDomain = []
# hei(tempDomain,10-1,[3,4],domene)
# column.domain = list(reversed(domene))
#
# print(column.domain)
# print("Lenge: " + str(len(column.domain)))
#
#
# domainFiltering([row],[row,column])
print("Running init")
print("")
#getWindow().getMouse()
domainFiltering(queue,rowsAndColumns)

print("Init done")
#getWindow().getMouse()
currentState = nonoState(rowsAndColumns)


#getWindow().getMouse()


drawState(currentState)

if currentState.isFinished():
    print("Solution found. No need for A*")
else:
    print("Done with init, but no solution yet. Running A*")
while not currentState.isFinished():
#for tall in range(0,100000):

        #vert = vertices[tall]
        #print("Doamin to " + str(tall) + " is " + str(vert.domain))


        #color = vert.domain[0]
        #vert.domain = [color]
        newStates = generateSuccesorStates(currentState.vertices)
        print("Lengden: " + str(len(newStates)))

        #getWindow().getMouse()
        if len(newStates) == 0:
                print("breaking")
                currentState = nonoState(rowsAndColumns)
                getWindow().getMouse()
                continue
        currentState = newStates[randint(0,len(newStates)-1)]
        canContinue = False

        drawState(currentState)
        vert = currentState.lastModifiedVertex
        queue = []
        for connectedVertex in contraints[vert.index]:
                if connectedVertex not in queue and not currentState.vertices[connectedVertex].isAssumed():
                        queue.append(currentState.vertices[connectedVertex])






        domainFiltering(queue,currentState.vertices)


#Rerun




        if currentState.isError():
                currentState = nonoState(rowsAndColumns)
                print("Going back a level")
        elif currentState.isFinished():
            print("Am i finished now?")
            #getWindow().getMouse()


        print("- ")

drawState(currentState)

getWindow().getMouse()