from threading import Thread
from time import time
import theano
import numpy as np
from theano import tensor as T

__author__ = 'Anders'


class ANN:

    def __init__(self):
        self.predictFunc = None
        self.trainFunc = None
        self.weights = None
        self.current_best = 0.

    def init_weights(self, *args):
        self.weights = []
        for shape in args:
            self.weights.append(theano.shared(floatX(np.random.randn(*shape) * 0.01)))

    def init_training_data(self, model=None, errorprop=None):
        X = T.fmatrix()
        Y = T.fmatrix()

        noise_py_x = model(X, 0.2, 0.5, self.weights)
        py_x = model(X, 0., 0., self.weights)

        # Currently the output given the inputs and weights
        y_x = T.argmax(py_x, axis=1)

        cost = T.mean(T.nnet.categorical_crossentropy(noise_py_x, Y))
        updates = errorprop(cost, self.weights)

        # train runs "update" on each run (for each image) with the inputs given
        # update includes symbols to update each weight
        self.trainFunc = theano.function(inputs=[X, Y], outputs=None, updates=updates, allow_input_downcast=True)
        # predict use symbol y_x which is given by the model
        self.predictFunc = theano.function(inputs=[X], outputs=y_x, allow_input_downcast=True)

    def train(self,trX, trY, teX, teY):
        # ONE RUN OVER THE TRAINING SET, RUN IN A SEPARATE THREAD
        def trainFunc():
            for start, end in zip(range(0, len(trX), 900), range(900, len(trX), 900)):
                #print("trX[start:end] shape: ", trX[start:end].shape)
                #print("trY[start:end] shape: ", trY[start:end].shape)
                self.trainFunc(trX[start:end], trY[start:end])
            self.current_best = np.mean(np.argmax(teY, axis=1) == self.predictFunc(teX))
            print(self.current_best)

        def stopTrainingListener():
            input()
            global keep_running
            keep_running = False

        keep_running = True
        thr = None

        print("use (CTRL-C) keyboard interrupt on unix to stop training")
        print("press enter to stop with stopThr (windows)")
        startTime = time()
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

        print("After 20 runs we acquired a presision of", self.current_best, "on the training set")
        print("Time elapsed:", time() - startTime)
        
        return self.current_best

    def blind_test(self,cases):
        preds = self.predictFunc(cases)
        predFormated = [0] * len(preds)
        for x in range(0,len(preds)):
            predFormated[x] = preds[x]

        return predFormated

def floatX(X):
    return np.asarray(X, dtype=theano.config.floatX)