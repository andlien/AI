from cspVertex import *
from cspGrid import *

#f = open('graph-color-2.txt', 'r')
#f = open('spiral-500-4-color1.txt', 'r')
f = open('rand-100-6-color1.txt', 'r')


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
                temp.append(x)
                temp.append(y)
                constraintsTemplate.append(temp)

print(constraintsTemplate)

print("numberOfVertices: " + str(numberOfVertices))
print("numberOfEdges: " + str(numberOfEdges))

vertices = []
setDimensions(numberOfVertices)
contraints = []

for line in range(0,numberOfVertices):
        vertLine = f.readline()
        #print (vertLine)
        values = ( vertLine.split( ) )
        index = int(values[0])
        x = float(values[1])
        y = float(values[2])
        vert = Vertex(index,x,y)

        contraints.append({})

        vert.domain = range(0, numberOfColors)
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

        #tempDict1 = {index2: constraintsTemplate};
        contraints[index][index2] = constraintsTemplate
        contraints[index2][index] = constraintsTemplate

        #vertices[index1].connectedTo.append(vertices[index2])
        #vertices[index2].connectedTo.append(vertices[index1])

        drawEdge( vertices[index1], vertices[index2])
print ("Created " + str(line) + " edges")



for vert in vertices:
         drawVertex(vert)


def revise(vertex1,vertex2):
        revised = False

        if contraints[vertex1.index][vertex2.index] == None:
                return False

        for d1 in vertex1.domain:
                domainChanged = False
                for d2 in vertex2.domain:
                        for const in constraintsTemplate:
                                if d1 == const[0] and d2 == const[1]:
                                        domainChanged = True

                if not domainChanged:
                        vertex1.domain.remove(d1)
                        revised = True

        return revised






getWindow().getMouse()
