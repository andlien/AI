from threading import Thread

__author__ = 'simen'

from Module5.basics.mnist_basics import *
import theano
from theano import tensor as T
from theano.sandbox.rng_mrg import MRG_RandomStreams as RandomStreams
import numpy as np
from Module5.ann import ANN

# features in this design:
#
# Number of hidden layers: 2
# Number of nodes in hidden layers: 600, 150
# Activation: rectified linear units
# Learning rate: 0.001
# Error func: Stockastic gradient desent with mini-batches
#

srng = RandomStreams()

def floatX(X):
    return np.asarray(X, dtype=theano.config.floatX)

def init_weights(*args):
    weights = []
    for shape in args:
        weights.append(theano.shared(floatX(np.random.randn(*shape) * 0.01)))
    return weights

def rectify(X):
    return T.maximum(X, 0.)

def softmax(X):
    e_x = T.exp(X - X.max(axis=1).dimshuffle(0, 'x'))
    return e_x / e_x.sum(axis=1).dimshuffle(0, 'x')

def MSGD(cost, params, learning_rate=0.001):
    # get gradients (differentiation over variables in params)
    grads = T.grad(cost=cost, wrt=params)
    updates = []
    for weight, derivative in zip(params, grads):
        updates.append((weight, weight - derivative * learning_rate))
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

# READ TRAINING DATA
trainingInput, trainingOutput = load_mnist()

trX = np.zeros((60000, 784), dtype=np.float32)
trY = np.zeros((60000, 10), dtype=np.float32)
for i in range(60000):
    flat = np.array(flatten_image(trainingInput[i]), dtype=np.float32)
    trX[i] = (flat - flat.min()) / (flat.max() - flat.min())

    index = int(trainingOutput[i][0])
    trY[i][index] += 1

trainingInput = None
trainingOutput = None

# READ TESTING DATA
testingInput, testingOutput = load_mnist(dataset="testing")

teX = np.zeros((10000, 784), dtype=np.float32)
teY = np.zeros((10000, 10), dtype=np.float32)
for i in range(10000):
    flat = np.array(flatten_image(testingInput[i]), dtype=np.float32)
    teX[i] = (flat - flat.min()) / (flat.max() - flat.min())

    index = int(testingOutput[i][0])
    teY[i][index] += 1

testingInput = None
testingOutput = None

# THEANO, I CHOOSE YOU!
X = T.fmatrix()
Y = T.fmatrix()

ws = init_weights((784, 600), (600, 150), (150, 10))

noise_py_x = model(X, 0.2, 0.5, ws)
py_x = model(X, 0., 0., ws)

# Currently the output given the inputs and weights
y_x = T.argmax(py_x, axis=1)

cost = T.mean(T.nnet.categorical_crossentropy(noise_py_x, Y))
updates = MSGD(cost, ws, learning_rate=0.001)

# train runs "update" on each run (for each image) with the inputs given
# update includes symbols to update each weight
train = theano.function(inputs=[X, Y], outputs=None, updates=updates, allow_input_downcast=True)
# predict use symbol y_x which is given by the model
predict = theano.function(inputs=[X], outputs=y_x, allow_input_downcast=True)

mNeuralNet = ANN(predict)

# ONE RUN OVER THE TRAINING SET, RUN IN A SEPARATE THREAD
def trainFunc():
    for start, end in zip(range(0, len(trX), 900), range(900, len(trX), 900)):
        #print("trX[start:end] shape: ", trX[start:end].shape)
        #print("trY[start:end] shape: ", trY[start:end].shape)
        train(trX[start:end], trY[start:end])
    print (np.mean(np.argmax(teY, axis=1) == predict(teX)))

def stopTrainingListener():
    input()
    global keep_running
    keep_running = False

print("Start looping")
keep_running = True
thr = None

print("use (CTRL-C) keyboard interrupt on unix to stop training")
print("press enter to stop with stopThr (windows)")
while keep_running:
    stopThr = Thread(target=stopTrainingListener)
    stopThr.start()
    try:
        thr = Thread(target=trainFunc, daemon=True)
        thr.start()
        thr.join()
    except KeyboardInterrupt:
        # Interrupt happens on main-thread, not on training thread
        keep_running = False
        # Do not continue until trainFunc has finished!
        # Prevents inconsistent state?
        thr.join()

print("Start tests!")
minor_demo(mNeuralNet)
