from Module2.cspGrid import *
from Module2.aStarGacProgram import aStarGAC


#Code used to interpt input from the user
while True:

    lastState = []

    f = None
    numberOfColors = -1

    while True:
        prompt = input("Please type in the path to your file and press 'Enter': ")
        try:
            f = open(prompt + ".txt", 'r')
        except FileNotFoundError:
            print("Wrong file or file path")
        else:
            break

    while True:
        numberOfColors = input("Please type in the number of colors: ")
        try:
            numberOfColors = int(numberOfColors)
        except ValueError:
            print("Not an integer! Try again: ")
        else:
            break

    # First line is info about number of vertices and number of edges
    firstLine = f.readline().split()

    numberOfVertices = int(firstLine[0])
    numberOfEdges = int(firstLine[1])

    constraintsTemplate = []
    print("")

    # Creates a tempplate of the contraints
    for x in range (1, numberOfColors + 1):
        for y in range (1, numberOfColors + 1):
            if x == y:
                continue
            temp = (str(x), str(y))
            constraintsTemplate.append(temp)

    print(constraintsTemplate)
    print("")

    print("numberOfVertices: " + str(numberOfVertices))
    print("numberOfEdges: " + str(numberOfEdges))

    vertices = []
    setDimensions(numberOfVertices) # Inits the graphics
    constraints = []

    # Creates all the vertices
    for line in range(0,numberOfVertices):
        vertLine = f.readline().split()
        index = int(vertLine[0])
        x = float(vertLine[1])
        y = float(vertLine[2])
        vert = Vertex(index,x,y)

        constraints.append({}) # Adds a location for this vertex in the constraints

        vert.domain = [str(i) for i in range(1, numberOfColors+1)] # Creates the domain
        vertices.append(vert)

    print ("Created " + str(line) + " vertices")

    #NV+2 to NV+2+NE-1

    for line in range(0,numberOfEdges):
        vertLine = f.readline().split()
        index1 = int(vertLine[0])
        index2 = int(vertLine[1])

        constraints[index1][index2] = constraintsTemplate
        constraints[index2][index1] = constraintsTemplate

        drawEdge( vertices[index1], vertices[index2])
    print ("Created " + str(line) + " edges")

    f.close()

    # Draws the vertices in the GUI
    for vert in vertices:
        lastState.append(None)
        drawVertex(vert,False)

    # Custom fuction to draw updated state
    # Only redrawn vertices when they change
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

    #Calling the A*GAC
    aStarGAC(2,vertices, paintBoard, constraints=constraints)
    getWindow().getMouse()
