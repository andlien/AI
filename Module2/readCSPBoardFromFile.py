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

print("numberOfVertices: " + str(numberOfVertices))
print("numberOfEdges: " + str(numberOfEdges))

vertices = []
setDimensions(numberOfVertices)

for line in range(0,numberOfVertices):
        vertLine = f.readline()
        print (vertLine)
        values = ( vertLine.split( ) )
        index = int(values[0])
        x = float(values[1])
        y = float(values[2])
        vert = Vertex(index,x,y)
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

        vertices[index1].connectedTo.append(vertices[index2])
        vertices[index2].connectedTo.append(vertices[index1])

        drawEdge( vertices[index1], vertices[index2])
print ("Created " + str(line) + " vertices")


for vert in vertices:
         drawVertex(vert)

getWindow().getMouse()
