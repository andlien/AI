__author__ = 'simen'


from basics.mnist_basics import *
import theano
from theano import tensor as T
from theano.sandbox.rng_mrg import MRG_RandomStreams as RandomStreams
import numpy as np


srng = RandomStreams()

def floatX(X):
    return np.asarray(X, dtype=theano.config.floatX)

def init_weights(shape):
    return theano.shared(floatX(np.random.randn(*shape) * 0.01))

def rectify(X):
    return T.maximum(X, 0.)

def softmax(X):
    e_x = T.exp(X - X.max(axis=1).dimshuffle(0, 'x'))
    return e_x / e_x.sum(axis=1).dimshuffle(0, 'x')

def RMSprop(cost, params, lr=0.001, rho=0.9, epsilon=1e-6):
    grads = T.grad(cost=cost, wrt=params)
    updates = []
    for p, g in zip(params, grads):
        acc = theano.shared(p.get_value() * 0.)
        acc_new = rho * acc + (1 - rho) * g ** 2
        gradient_scaling = T.sqrt(acc_new + epsilon)
        g = g / gradient_scaling
        updates.append((acc, acc_new))
        updates.append((p, p - lr * g))
    return updates

def dropout(X, p=0.):
    if p > 0:
        retain_prob = 1 - p
        X *= srng.binomial(X.shape, p=retain_prob, dtype=theano.config.floatX)
        X /= retain_prob
    return X

def model(X, w_h, w_h2, w_o, p_drop_input, p_drop_hidden):
    X = dropout(X, p_drop_input)
    h = rectify(T.dot(X, w_h))

    h = dropout(h, p_drop_hidden)
    h2 = rectify(T.dot(h, w_h2))

    h2 = dropout(h2, p_drop_hidden)
    py_x = softmax(T.dot(h2, w_o))
    return h, h2, py_x
trainingInput,trainingOutput = load_mnist()


#
# trX = np.zeros((100, 784), dtype=np.float32)
# trY = np.zeros((100, 10), dtype=np.float32)
# for i in range(100):
#     for x in range(28):
#         for y in range(28):
#              trX[i][x+y] = trainingInput[i][x][y] / 256.0
#
#     index = trainingOutput[i]
#     trY[i][index] = 1.0

trainingInput, trainingOutput = gen_flat_cases()

trX = np.zeros((6000, 784), dtype=np.float32)
trY = np.zeros((6000, 10), dtype=np.float32)
for i in range(6000):
    trX[i] = np.array(trainingInput[i])
            #trX[i][x+y] = trainingInput[i][y][x]
    #print(str(trX[i]))

    index = int(trainingOutput[i])
    # trY[i][0] = index
    trY[i][index] += 1
    #print(index)



testingInput, testingOutput = gen_flat_cases(type="testing")

teX = np.zeros((10000, 784), dtype=np.float32)
teY = np.zeros((10000, 10), dtype=np.float32)
for i in range(10000):
    teX[i] = np.array(testingInput[i])
            #trX[i][x+y] = trainingInput[i][y][x]
    #print(str(trX[i]))

    index = int(testingOutput[i])
    # trY[i][0] = index
    teY[i][index] += 1
    #print(index)


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

X = T.fmatrix()
Y = T.fmatrix()

w_h = init_weights((784, 600))
w_h2 = init_weights((600, 150))
w_o = init_weights((150, 10))

noise_h, noise_h2, noise_py_x = model(X, w_h, w_h2, w_o, 0.2, 0.5)
h, h2, py_x = model(X, w_h, w_h2, w_o, 0., 0.)
y_x = T.argmax(py_x, axis=1)

cost = T.mean(T.nnet.categorical_crossentropy(noise_py_x, Y))
params = [w_h, w_h2, w_o]
updates = RMSprop(cost, params, lr=0.001)

train = theano.function(inputs=[X, Y], outputs=cost, updates=updates, allow_input_downcast=True)
predict = theano.function(inputs=[X], outputs=y_x, allow_input_downcast=True)

# for i in range(1):
#     #for start, end in zip(range(0, len(trX), 784), range(784, len(trX), 784)):
#     for s in range(0,100):
#         cost = train(np.array([trX[s]]), np.array([trY[s]]))
#         #print(str(np.array([trY[s]])))
#         #print(predict(teX))
#         print ( np.mean(np.argmax(trY, axis=1) == predict(trX)))
#     #print(i)


for i in range(200):
    for start, end in zip(range(0, len(trX), 900), range(900, len(trX), 900)):
        #print("trX[start:end] shape: ", trX[start:end].shape)
        #print("trY[start:end] shape: ", trY[start:end].shape)
        cost = train(trX[start:end], trY[start:end])
    print (np.mean(np.argmax(teY, axis=1) == predict(teX)))