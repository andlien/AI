__author__ = 'Anders'
from Module1.aStarProgram import aStarAlgorithm
from Module2.state import State



# def aStarGAC(moduleNr,variables, constraints, GAC_init, GAC_domain_filter, GAC_gen_new_states, GAC_rerun, aStarH, paintProgress):
#     def AStar_generate_successors(currentState):
#         mNewStates = GAC_gen_new_states(currentState,constraints,moduleNr)
#         #return mNewStates
#         returnStates = []
#
#
#         for state in mNewStates:
#             GAC_rerun(state, constraints)
#             if not state.isError():
#                 #mNewStates.remove(state)
#                 returnStates.append(state)
#
#         return returnStates#mNewStates
#
#     queue = GAC_init(variables, constraints)
#     GAC_domain_filter(queue,variables, constraints)
#     currentState = State(variables)
#     aStarAlgorithm(AStar_generate_successors, aStarH, currentState, paintProgress)
#
#
# def aStarGAC(moduleNr,variables, constraints,paintProgress):
#     def AStar_generate_successors(currentState):
#         mNewStates = generateSuccesorStates(currentState,moduleNr)
#         returnStates = []
#
#         for state in mNewStates:
#             rerun(state, constraints, revise)
#             if not state.isError():
#                 #mNewStates.remove(state)
#                 returnStates.append(state)
#
#         return returnStates#mNewStates
#
#     queue = GACInitialize(variables, constraints)
#     domainFiltering(queue,variables, constraints,revise)
#     currentState = State(variables)
#     aStarAlgorithm(AStar_generate_successors, aStarGetH, currentState, paintProgress)

def aStarGAC(moduleNr,variables, constraints, paintProgress, GAC_Revise = None):

    if GAC_Revise is None:
        GAC_Revise = revise

    def AStar_generate_successors(currentState):
        mNewStates = generateSuccesorStates(currentState,moduleNr)
        returnStates = []

        for state in mNewStates:
            rerun(state, constraints,GAC_Revise)
            if not state.isError():
                returnStates.append(state)

        return returnStates


    queue = GACInitialize(variables, constraints)
    domainFiltering(queue,variables, constraints,GAC_Revise)
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


    for vertex in oldState.vertices:
        if not vertex.isAssumed():
            if bestValue > len(vertex.domain):
                bestVariable = vertex
                bestValue = len(vertex.domain)


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
            # print("Doamin to " +str(vertex1.index) +  str(vertex1.domain) + ". Removing: " + str(d1))
            vertex1.domain.remove(d1)
            # print("Doamin to " +str(vertex1.index)+  str(vertex1.domain))
            revised = True



    return revised

#Initialize
def GACInitialize(vertices, constraints):
    queue = []
    for vertex in constraints:
        for connectedVertex in vertex:
            if vertices[connectedVertex] not in queue:
                queue.append(vertices[connectedVertex])
    return queue

def getNumberOfUnsatisfiedConstraints(stateVertices, constraints, GAC_Revise):
    queue = GACInitialize(stateVertices, constraints)
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
