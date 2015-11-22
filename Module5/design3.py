from threading import Thread

__author__ = 'simen'

from Module5.basics.mnist_basics import *
import theano
from theano import tensor as T
from theano.sandbox.rng_mrg import MRG_RandomStreams as RandomStreams
import numpy as np

# features in this design:
#
# Number of hidden layers: 3
# Number of nodes in hidden layers: 300, 350, 150
# Activation: rectified linear units
# Learning rate: 0.001
# Error func: Root mean squared propagation
#

class ANN:

    def __init__(self, newPredict):
        self.predictFunc = newPredict

    def blind_test(self,cases):
        preds = self.predictFunc(cases)
        predFormated = [0] * len(preds)
        for x in range(0,len(preds)):
            predFormated[x] = preds[x]

        return predFormated

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

ws = init_weights((784, 300), (300, 350), (350, 150), (150, 10))

noise_py_x = model(X, 0.2, 0.5, ws)
py_x = model(X, 0., 0., ws)

# Currently the output given the inputs and weights
y_x = T.argmax(py_x, axis=1)

cost = T.mean(T.nnet.categorical_crossentropy(noise_py_x, Y))
updates = RMSprop(cost, ws, learning_rate=0.001)

# train runs "update" on each run (for each image) with the inputs given
# update includes symbols to update each weight
train = theano.function(inputs=[X, Y], outputs=None, updates=updates, allow_input_downcast=True)
# predict use symbol y_x which is given by the model
predict = theano.function(inputs=[X], outputs=y_x, allow_input_downcast=True)

mNeuralNet = ANN(predict)

# ONE RUN OVER THE TRAINING SET, RUN IN A SEPARATE THREAD
def trainFunc():
    global cost
    for start, end in zip(range(0, len(trX), 900), range(900, len(trX), 900)):
        #print("trX[start:end] shape: ", trX[start:end].shape)
        #print("trY[start:end] shape: ", trY[start:end].shape)
        train(trX[start:end], trY[start:end])
    print (np.mean(np.argmax(teY, axis=1) == predict(teX)))

print("Start looping")
keep_running = True
thr = None
while keep_running:
    try:
        thr = Thread(target=trainFunc)
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
