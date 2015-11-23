from threading import Thread

__author__ = 'simen'


import theano
from Module6.readingDataFromFile import *
from theano import tensor as T
from theano.sandbox.rng_mrg import MRG_RandomStreams as RandomStreams
import numpy as np
from Module5.ann import *
#from Module4.main2048 import *


srng = RandomStreams()
def rectify(X):
    return T.maximum(X, 0.)

def softmax(X):
    e_x = T.exp(X - X.max(axis=1).dimshuffle(0, 'x'))
    return e_x / e_x.sum(axis=1).dimshuffle(0, 'x')

def RMSprop(cost, params, learning_rate=0.001, rho=0.9, epsilon=1e-6):
    # get gradients (differentiation over variables in params)
    grads = T.grad(cost=cost, wrt=params)
    updates = []
    for weight, derivative in zip(params, grads):
        # NoteToSelf: This line is evaluated only once!
        r = theano.shared(weight.get_value() * 0.)
        # The rest is evaluated by tensor each update by using symbol variables in the updates list
        new_r = rho * r + (1 - rho) * derivative ** 2
        gradient_scaling = T.sqrt(new_r + epsilon)
        derivative = learning_rate * derivative / gradient_scaling
        updates.append((r, new_r))
        updates.append((weight, weight - derivative))
    return updates

def dropout(X, p=0.):
    if p > 0:
        retain_prob = 1 - p
        X *= srng.binomial(X.shape, p=retain_prob, dtype=theano.config.floatX)
        X /= retain_prob
    return X

def model(X, p_drop_input, p_drop_hidden, weights):

    # Do forward propagation! (calculate outputs)
    h = dropout(X, p_drop_input)
    if len(weights) == 1:
        return softmax(T.dot(h, weights[0]))
    h = rectify(T.dot(h, weights[0]))

    for weight in weights[1:len(weights)-1]:
        h = dropout(h, p_drop_hidden)
        h = rectify(T.dot(h, weight))

    h = dropout(h, p_drop_hidden)
    return softmax(T.dot(h, weights[-1]))

# trX = np.zeros((100, 784), dtype=np.float32)
# trY = np.zeros((100, 10), dtype=np.float32)
# for i in range(100):
#     for x in range(28):
#         for y in range(28):
#              trX[i][x+y] = trainingInput[i][x][y] / 256.0
#
#     index = trainingOutput[i]
#     trY[i][index] = 1.0

def trainNet():
    trainingInput, trainingOutput,testingInput, testingOutput = getTrainingData()

    lengthOfList = len(trainingInput[0])

    trX = np.zeros((len(trainingInput), lengthOfList), dtype=np.float32)
    trY = np.zeros((len(trainingInput), 4), dtype=np.float32)
    for i in range(len(trainingInput)):
        trX[i] = np.array((trainingInput[i]), dtype=np.float32)

        #print(trainingOutput[i])
        index = int(trainingOutput[i])
        # trY[i][0] = index
        trY[i][index] += 1
        #print(index)

    trainingInput = None
    trainingOutput = None


    teX = np.zeros((len(testingInput), lengthOfList), dtype=np.float32)
    teY = np.zeros((len(testingInput), 4), dtype=np.float32)
    for i in range(len(testingInput)):
        teX[i] = np.array((testingInput[i]), dtype=np.float32)

        index = int(testingOutput[i])
        # trY[i][0] = index
        teY[i][index] += 1
        #print(index)


    testingInput = None
    testingOutput = None

    # testingInput, testingOutput = load_mnist(dataset="testing")
    #
    # teX = np.zeros((10000, 784), dtype=np.float32)
    # teY = np.zeros((10000, 10), dtype=np.float32)
    # for i in range(10000):
    #     flat = np.array(flatten_image(testingInput[i]), dtype=np.float32)
    #     teX[i] = (flat - flat.min()) / (flat.max() - flat.min())
    #             #trX[i][x+y] = trainingInput[i][y][x]
    #     #print(str(trX[i]))
    #
    #     index = int(testingOutput[i][0])
    #     # trY[i][0] = index
    #     teY[i][index] += 1
    #     #print(index)
    #
    # testingInput = None
    # testingOutput = None

    # testinInput,testingOutput = load_mnist("testing")
    #
    # print("testinInput shape: ", testinInput.shape)
    # print("testingOutput shape: ", testingOutput.shape)
    #
    # teX = np.zeros((100, 784), dtype=np.float32)
    # teY = np.zeros((100, 1), dtype=np.float32)
    # for i in range(100):
    #     for x in range(28):
    #         for y in range(28):
    #              teX[i][x+y] = trainingInput[i][x][y]
    #
    #     index = trainingOutput[i]
    #     teY[i][0] = index
    #
    #
    # print("X shape: ", trX.shape)
    # print("Y shape: ", trY.shape)

    # X = T.fmatrix()
    # Y = T.fmatrix()
    #
    # w_h = init_weights((lengthOfList, 100))
    # w_h2 = init_weights((100, 200))
    # w_o = init_weights((200, 4))
    #
    # noise_h, noise_h2, noise_py_x = model(X, w_h, w_h2, w_o, 0.2, 0.5)
    # h, h2, py_x = model(X, w_h, w_h2, w_o, 0., 0.)
    # y_x = py_x
    # #y_x = T.argmax(py_x, axis=1)
    #
    # cost = T.mean(T.nnet.categorical_crossentropy(noise_py_x, Y))
    # params = [w_h, w_h2, w_o]
    # updates = RMSprop(cost, params, lr=0.001)
    #
    # train = theano.function(inputs=[X, Y], outputs=cost, updates=updates, allow_input_downcast=True)
    # predict = theano.function(inputs=[X], outputs=y_x, allow_input_downcast=True)

    print("Data read")
    mNeuralNet = ANN()

    # neural net is represented by weights and activation function

    #mNeuralNet.init_weights((lengthOfList, 50), (50, 100),(100, 200), (200, 4)) #1. plass
    #mNeuralNet.init_weights((lengthOfList, 250), (250, 550),(550, 550),(550, 200), (200, 4)) #2. plass
    #mNeuralNet.init_weights((lengthOfList, 100), (100, 200),(200, 400), (400, 4)) #3. plass
    #mNeuralNet.init_weights((lengthOfList, 14), (14, 4)) #3. plass
    # mNeuralNet.init_weights((lengthOfList, 400), (400, 200),(200, 50), (50, 4)) #3. plass

    mNeuralNet.init_weights((lengthOfList, 50), (50, 20),(20, 15),(15, 7), (7, 4)) #3. plass

   # mNeuralNet.init_weights((lengthOfList, 50), (50, 4)) #3. plass




    # Totalt runs:  150
    #     32  -  2 %
    #     64  -  10 %
    #     128  -  46 %
    #     256  -  37 %
    #     512  -  3 %
    mNeuralNet.init_training_data(model=model, errorprop=RMSprop)
    mNeuralNet.trainWithoutTest(trX, trY)


    # class theNet:
    #
    #     def setPrediction(self, newPredict):
    #         self.predictFunc = newPredict
    #
    #     def blind_test(self,cases):
    #         preds = self.predictFunc(cases)
    #         predFormated = [0] * len(preds)
    #         for x in range(0,len(preds)):
    #             predFormated[x] = preds[x]
    #
    #         return predFormated
    #
    #
    # sveisann = theNet()
    # sveisann.setPrediction(predict)

    # for i in range(1):
    #     #for start, end in zip(range(0, len(trX), 784), range(784, len(trX), 784)):
    #     for s in range(0,100):
    #         cost = train(np.array([trX[s]]), np.array([trY[s]]))
    #         #print(str(np.array([trY[s]])))
    #         #print(predict(teX))
    #         print ( np.mean(np.argmax(trY, axis=1) == predict(trX)))
    #     #print(i)

    # iterations = 0
    #
    # def trainFunc():
    #     global cost
    #     global iterations
    #     for start, end in zip(range(0, len(trX), 128), range(128, len(trX), 128)):
    #         #print("trX[start:end] shape: ", trX[start:end].shape)
    #         #print("trY[start:end] shape: ", trY[start:end].shape)
    #         cost = train(trX[start:end], trY[start:end])
    #     #print (np.mean(np.argmax(teY, axis=1) == predict(teX)))
    #         #print("Hei")
    #     #print(np.array([[2,1,0,6,5,4,10,9,8,14,13,12,1,0]]).shape)
    #     #print(predict(np.array([[1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0]])))
    #     #iterations +=1
    #
    # print("Start looping")
    # keep_running = True
    # thr = None
    #
    # numberOfIterations = 50
    # for tall in range(numberOfIterations):
    #     trainFunc()
    #     print(tall, "/",numberOfIterations)

    # while keep_running:
    #     try:
    #         thr = Thread(target=trainFunc)
    #         thr.start()
    #         thr.join()
    #     except KeyboardInterrupt:
    #         # Interrupt happens on main-thread
    #         keep_running = False
    #         # Do not continue untill trainFunc has finished!
    #         # Prevents inconsistent state?
    #         thr.join()



    return mNeuralNet.predictFunc


#trainNet()