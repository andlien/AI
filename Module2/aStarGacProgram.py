from Module1.aStarProgram import aStarAlgorithm
from Module2.state import State


def aStarGAC(moduleNr,
             variables,
             constraints,
             paintProgress,
             GAC_Initialize = None,
             GAC_Domain_Filter = None,
             GAC_Revise = None,
             GAC_Rerun = None,
             GAC_Generate_Successors=None):

    # If custom functions are not defined, go default
    if GAC_Revise is None:
        GAC_Revise = revise
    if GAC_Initialize is None:
        GAC_Initialize = mGACInit
    if GAC_Domain_Filter is None:
        GAC_Domain_Filter = domainFiltering
    if GAC_Rerun is None:
        GAC_Rerun = rerun
    if GAC_Generate_Successors is None:
        GAC_Generate_Successors = generateSuccesorStates

    # The function that generates neighbours/successors in A*
    # Generates states, and revises them as far as possible
    def AStar_generate_successors(currentState):
        mNewStates = GAC_Generate_Successors(currentState,moduleNr)
        returnStates = []

        for state in mNewStates:
            GAC_Rerun(state, constraints,GAC_Revise)
            if not state.isError():
                returnStates.append(state)

        return returnStates


    queue = GAC_Initialize(variables, constraints)
    GAC_Domain_Filter(queue,variables, constraints,GAC_Revise)
    currentState = State(variables,moduleNr)
    print(" ")
    print("Init done")

    if currentState.isGoal():
        print("Solution found. No need for A*")
        paintProgress(currentState)
        print("Total number of search nodes generated: ", 0)
        print("Total number of search nodes expanded: ", 0)
        print("Total number of search nodes on the path from the root to the solution state.: ", 0)
    elif currentState.isError():
        print("No solutiion found. Aborting")
    else:
        print("Done with init, but no solution yet. Running A*")
        currentState = aStarAlgorithm(AStar_generate_successors, aStarGetH, currentState, paintProgress)

    print("Total number of variables that are not assigned: ", currentState.getNumberOfVariablesNotAssigned(), "/", len(currentState.vertices))
    print("Total number of unsatisfied constraints in the solution: ", getNumberOfUnsatisfiedConstraints(currentState.vertices, constraints,GAC_Revise))
    print("")


def generateSuccesorStates(oldState,moduleNr):
    newStates = []

    bestValue = 10
    bestVariable = None

    #Find the variable with the lowest lenght of the domain that is not assumed. Domain must be larger then 1
    for vertex in oldState.vertices:
        if not vertex.isAssumed():
            if bestValue > len(vertex.domain):
                bestVariable = vertex
                bestValue = len(vertex.domain)

    #Create a new state for each element in the domain of the selected variable
    for color in bestVariable.domain:
        state = State(oldState.vertices,moduleNr)
        state.vertices[bestVariable.index].domain = [color]
        state.lastModifiedVertex = state.vertices[bestVariable.index]
        newStates.append(state)

    return newStates

def rerun(currentState, constraints,GAC_Revise):
    #Rerun
    queue = []
    for connectedVertex in constraints[currentState.lastModifiedVertex.index]:
        if connectedVertex not in queue and not currentState.vertices[connectedVertex].isAssumed():
            queue.append(currentState.vertices[connectedVertex])

    domainFiltering(queue,currentState.vertices, constraints,GAC_Revise)

#Heuristic function
# Returns the sum of the domain lenght of all the variables in the state
def aStarGetH(node):
    sum = 0
    for v in node.vertices:
        if not v.isAssumed():
            sum += len(v.domain)
    return sum



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
                    break

        if not domainChanged:
            vertex1.domain.remove(d1)
            revised = True

    return revised

#Initialize
def mGACInit(vertices, constraints):
    queue = []
    for vertex in constraints:
        for connectedVertex in vertex:
            if vertices[connectedVertex] not in queue:
                queue.append(vertices[connectedVertex])
    return queue

# Called after the A*GAC is finished
def getNumberOfUnsatisfiedConstraints(stateVertices, constraints, GAC_Revise):
    queue = mGACInit(stateVertices, constraints)
    counter = 0
    while len(queue) >= 1:
        todoReviseVertex = queue.pop(0)
        #queue.remove(todoReviseVertex)
        for const in constraints[todoReviseVertex.index]:
            neighbour = stateVertices[const]
            change = GAC_Revise(constraints, todoReviseVertex,neighbour)
            if change:
                counter = counter + 1

    return counter



#The Domain-Filtering Loop
def domainFiltering(queue, stateVertices, constraints, GAC_Revise):
    while len(queue) >= 1:
        todoReviseVertex = queue.pop(0)
        #queue.remove(todoReviseVertex)
        for const in constraints[todoReviseVertex.index]:
            neighbour = stateVertices[const]
            change = GAC_Revise(constraints, todoReviseVertex,neighbour)
            if change:
                for v in constraints[todoReviseVertex.index]:
                    if stateVertices[v] not in queue:
                        queue.append(stateVertices[v])
