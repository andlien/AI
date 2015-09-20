from cspVertex import *
from cspGrid import *
from state import *
from random import randint

f = open('graph-color-1.txt', 'r')
#f = open('spiral-500-4-color1.txt', 'r')
#f = open('rand-100-6-color1.txt', 'r')


print (f)

firstLine = f.readline()
values = ( firstLine.split( ) )

numberOfVertices = int(values[0])
numberOfEdges = int(values[1])

numberOfColors = 4

constraintsTemplate = []

for x in range (1, numberOfColors + 1):
        for y in range (1, numberOfColors + 1):
                if x == y:
                        continue
                temp = []
                temp.append(str(x))
                temp.append(str(y))
                constraintsTemplate.append(temp)

print(constraintsTemplate)

print("numberOfVertices: " + str(numberOfVertices))
print("numberOfEdges: " + str(numberOfEdges))

vertices = []
setDimensions(numberOfVertices)
contraints = []

for line in range(0,numberOfVertices):
        vertLine = f.readline()
        print (vertLine)
        values = ( vertLine.split( ) )
        index = int(values[0])
        x = float(values[1])
        y = float(values[2])
        vert = Vertex(index,x,y)

        contraints.append({})

        vert.domain = []
        for number in range(1, numberOfColors+1):
                vert.domain.append(str(number))
        vertices.append(vert)
        #drawVertex(vert)


print ("Created " + str(line) + " vertices")

#NV+2 to NV+2+NE-1

for line in range(0,numberOfEdges):
        vertLine = f.readline()
        print (vertLine)
        values = ( vertLine.split( ) )
        index1 = int(values[0])
        index2 = int(values[1])


        contraints[index1][index2] = constraintsTemplate
        contraints[index2][index1] = constraintsTemplate

        drawEdge( vertices[index1], vertices[index2])
print ("Created " + str(line) + " edges")

print( str(contraints) )

for vert in vertices:
         drawVertex(vert,False)

#Initialization
queue = []
for vertex in contraints:
        for connectedVertex in vertex:
                if connectedVertex not in queue:
                        queue.append(vertices[connectedVertex])




def revise(vertex1,vertex2):
        revised = False

        if contraints[vertex1.index][vertex2.index] is None:
                return False

        for d1 in vertex1.domain:
                domainChanged = False
                for d2 in vertex2.domain:
                        for const in contraints[vertex1.index][vertex2.index]:
                                if d1 == const[0] and d2 == const[1]:
                                        domainChanged = True

                if not domainChanged:
                        print("Doamin to " +str(vertex1.index) +  str(vertex1.domain) + ". Removing: " + d1)
                        vertex1.domain.remove(d1)
                        print("Doamin to " +str(vertex1.index)+  str(vertex1.domain))
                        revised = True



        return revised

#The Domain-Filtering Loop
def domainFiltering(queue, stateVertices):
        while len(queue) >= 1:
                todoReviseVertex = queue.pop()
                #queue.remove(todoReviseVertex)
                for const in contraints[todoReviseVertex.index]:
                        neighbour = stateVertices[const]
                        change = revise(todoReviseVertex,neighbour)
                        if change:
                                for v in contraints[todoReviseVertex.index]:
                                        if v not in queue:
                                                queue.append(stateVertices[v])





def generateSuccesorStates(vertices):
        newStates = []

        for vertex in vertices:
                if not vertex.isColored():
                        for color in vertex.domain:
                                index = vertex.index
                                state = State(vertices)
                                state.vertices[index].domain = [color]
                                state.lastModifiedVertex = state.vertices[index]
                                newStates.append(state)


        return newStates

domainFiltering(queue,vertices)

currentState = State(vertices)
getWindow().getMouse()
while not currentState.isFinished():
#for tall in range(0,100000):

        #vert = vertices[tall]
        #print("Doamin to " + str(tall) + " is " + str(vert.domain))


        #color = vert.domain[0]
        #vert.domain = [color]
        newStates = generateSuccesorStates(currentState.vertices)
        print("Lengden: " + str(len(newStates)))

        if len(newStates) == 0:
                print("breaking")
                currentState = State(vertices)
                continue

        currentState = newStates[randint(0,len(newStates)-1)]

        for hei in currentState.vertices:
                drawVertex(hei,False)

        vert = currentState.lastModifiedVertex

#Rerun
        queue = []
        for connectedVertex in contraints[vert.index]:
                if connectedVertex not in queue and not currentState.vertices[connectedVertex].isColored():
                        queue.append(currentState.vertices[connectedVertex])

        domainFiltering(queue,currentState.vertices)

        if currentState.isError():
                currentState = State(vertices)

        print("- ")

print("Done?")
getWindow().getMouse()