from board import *



def createDemo():
	setDimensions(6,6)
	createBoard()
	createStart(1,0)
	createGoal(5,5)
	createObstacle(3,2,2,2)
	createObstacle(0,3,1,3)
	createObstacle(2,0,4,2)
	createObstacle(2,5,2,1)
 
def createExample0():
	setDimensions(10,10)
	createBoard()
	createStart(0,0)
	createGoal(9,9)
	createObstacle(2,3,5,5)
	createObstacle(8,8,2,1)


def createExample1():
	setDimensions(20,20)
	createBoard()
	createStart(19,3)
	createGoal(2,18)
	createObstacle(5,5,10,10)
	createObstacle(1,2,4,1)

def createExample2():
	setDimensions(20,20)
	createBoard()
	createStart(0,0)
	createGoal(19,19)
	createObstacle(17,10,2,1)
	createObstacle(14,4,5,2)
	createObstacle(3,16,10,2)
	createObstacle(13,7,5,3)
	createObstacle(15,15,3,3)

def createExample3():
	setDimensions(10,10)
	createBoard()
	createStart(0,0)
	createGoal(9,5)
	createObstacle(3,0,2,7)
	createObstacle(6,0,4,4)
	createObstacle(6,6,2,4)

def createExample4():
	setDimensions(10,10)
	createBoard()
	createStart(0,0)
	createGoal(9,9)
	createObstacle(3,0,2,7)
	createObstacle(6,0,4,4)
	createObstacle(6,6,2,4)

def createExample5():
	setDimensions(20,20)
	createBoard()
	createStart(0,0)
	createGoal(19,13)
	createObstacle(4,0,4,16)
	createObstacle(12,4,2,16)
	createObstacle(16,8,4,4)
