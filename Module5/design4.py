from threading import Thread
from Module5.ann import ANN

__author__ = 'simen'

from Module5.basics.mnist_basics import *
import theano
from theano import tensor as T
from theano.sandbox.rng_mrg import MRG_RandomStreams as RandomStreams
import numpy as np


# features in this design:
#
# Number of hidden layers: 2
# Number of nodes in hidden layers: 600, 150
# Activation: rectified linear units
# Learning rate: 0.001
# Error func: Root mean squared propagation
#


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


mNeuralNet = ANN()

# neural net is represented by weights and activation function
mNeuralNet.init_weights((784, 600), (600, 150), (150, 10))
mNeuralNet.init_training_data(model=model, errorprop=RMSprop)

print("Start training!")
mNeuralNet.train(trX, trY, teX, teY)

print("Start tests!")
minor_demo(mNeuralNet)
