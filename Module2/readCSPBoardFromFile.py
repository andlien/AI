from Module2.state import *
from Module2.cspGrid import *
from Module2.aStarGacProgram import aStarGAC

numberOfColors = 4

def revise(constraints, vertex1,vertex2):
    revised = False

    if constraints[vertex1.index][vertex2.index] is None:
        return False

    for d1 in vertex1.domain:
        domainChanged = False
        for d2 in vertex2.domain:
            for const in constraints[vertex1.index][vertex2.index]:
                if d1 == const[0] and d2 == const[1]:
                    domainChanged = True

        if not domainChanged:
            # print("Doamin to " +str(vertex1.index) +  str(vertex1.domain) + ". Removing: " + str(d1))
            vertex1.domain.remove(d1)
            # print("Doamin to " +str(vertex1.index)+  str(vertex1.domain))
            revised = True



    return revised

#Initialize
def mGACInitialize(vertices, constraints):
    queue = []
    for vertex in constraints:
        for connectedVertex in vertex:
            if connectedVertex not in queue:
                queue.append(vertices[connectedVertex])
    return queue

#The Domain-Filtering Loop
def domainFiltering(queue, stateVertices, contraints):
    while len(queue) >= 1:
        todoReviseVertex = queue.pop()
        #queue.remove(todoReviseVertex)
        for const in contraints[todoReviseVertex.index]:
            neighbour = stateVertices[const]
            change = revise(constraints, todoReviseVertex,neighbour)
            if change:
                for v in contraints[todoReviseVertex.index]:
                    if stateVertices[v] not in queue:
                        queue.append(stateVertices[v])


def generateSuccesorStates(oldState):
    newStates = []

    # modulo numberOfColors
    nextColor = str((oldState.g % numberOfColors) + 1)

    for vertex in oldState.vertices:
        if not vertex.isColored() and nextColor in vertex.domain:
            # for color in vertex.domain:
            #     index = vertex.index
            #     state = State(oldState.vertices)
            #     #Assumption
            #     state.vertices[index].domain = [color]
            #     state.lastModifiedVertex = state.vertices[index]
            #     newStates.append(state)
            # Produce new state by copying parent state
            state = State(oldState.vertices)
            # Assumption
            state.vertices[vertex.index].domain = [nextColor]
            state.lastModifiedVertex = state.vertices[vertex.index]
            newStates.append(state)

    return newStates


def mRerun(currentState, constraints):
    #Rerun
    queue = []
    for connectedVertex in constraints[currentState.lastModifiedVertex.index]:
        if connectedVertex not in queue and not currentState.vertices[connectedVertex].isColored():
            queue.append(currentState.vertices[connectedVertex])

    domainFiltering(queue,currentState.vertices, constraints)

def aStarH(node):
    summen = 0
    for v in node.vertices:
        if not v.isColored():
            summen += len(v.domain)
    return summen

def paintSol(state):
    for vertex in state.vertices:
        drawVertex(vertex, False)

# f = open('graph-color-1.txt', 'r')
f = open('spiral-500-4-color1.txt', 'r')
# f = open('rand-100-6-color1.txt', 'r')
# f = open('graph-test.txt', 'r')

print (f)

firstLine = f.readline()
values = firstLine.split()

numberOfVertices = int(values[0])
numberOfEdges = int(values[1])

constraintsTemplate = []

for x in range (1, numberOfColors + 1):
    for y in range (1, numberOfColors + 1):
        if x == y:
            continue
        temp = (str(x), str(y))
        constraintsTemplate.append(temp)

print(constraintsTemplate)

print("numberOfVertices: " + str(numberOfVertices))
print("numberOfEdges: " + str(numberOfEdges))

vertices = []
setDimensions(numberOfVertices)
constraints = []

for line in range(0,numberOfVertices):
    vertLine = f.readline()
    print(vertLine)
    values = vertLine.split()
    index = int(values[0])
    x = float(values[1])
    y = float(values[2])
    vert = Vertex(index,x,y)

    constraints.append({})

    vert.domain = [str(i) for i in range(1, numberOfColors+1)]
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


    constraints[index1][index2] = constraintsTemplate
    constraints[index2][index1] = constraintsTemplate

    drawEdge( vertices[index1], vertices[index2])
print ("Created " + str(line) + " edges")

print( str(constraints) )

for vert in vertices:
    drawVertex(vert,False)


aStarGAC(vertices, constraints, mGACInitialize, domainFiltering, generateSuccesorStates, mRerun, aStarH, paintSol)
getWindow().getMouse()
