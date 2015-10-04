from Module2.state import *
from Module2.cspGrid import *
from Module2.aStarGacProgram import aStarGAC

numberOfColors = 4

lastState = []

# f = open('graph-color-1.txt', 'r')
f = open('spiral-500-4-color1.txt', 'r')
# f = open('rand-100-6-color1.txt', 'r')
# f = open('graph-test.txt', 'r')


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

#print(constraintsTemplate)

print("numberOfVertices: " + str(numberOfVertices))
print("numberOfEdges: " + str(numberOfEdges))

vertices = []
setDimensions(numberOfVertices)
constraints = []

for line in range(0,numberOfVertices):
    vertLine = f.readline()
    #print(vertLine)
    values = vertLine.split()
    index = int(values[0])
    x = float(values[1])
    y = float(values[2])
    vert = Vertex(index,x,y)

    constraints.append({})

    vert.domain = []#[str(i) for i in range(1, numberOfColors+1)]
    for number in range(1, numberOfColors+1):
        vert.domain.append(str(number))
    vertices.append(vert)
    #drawVertex(vert)


print ("Created " + str(line) + " vertices")

#NV+2 to NV+2+NE-1

for line in range(0,numberOfEdges):
    vertLine = f.readline()
    #print (vertLine)
    values = ( vertLine.split( ) )
    index1 = int(values[0])
    index2 = int(values[1])


    constraints[index1][index2] = constraintsTemplate
    constraints[index2][index1] = constraintsTemplate

    drawEdge( vertices[index1], vertices[index2])
print ("Created " + str(line) + " edges")



f.close()

for vert in vertices:
    lastState.append(None)
    drawVertex(vert,False)


def paintBoard(state):
    global lastState
    #newState = []


    for tall in range(0,len(state.vertices)):
        vertex = state.vertices[tall]
        if vertex.isAssumed():
            if str(lastState[tall]) == str(vertex.getColor()):
                continue
            else:
                drawVertex(vertex, False)
                lastState[tall] = vertex.getColor()

        else:
            if not lastState[tall] is None:
                drawVertex(vertex, False)



def paintStatus(generated, expandend,solutionPath):
    drawInfoText(generated, expandend,solutionPath)

aStarGAC(2,vertices, constraints, paintBoard)
getWindow().getMouse()
