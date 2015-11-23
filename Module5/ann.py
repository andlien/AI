from threading import Thread
from time import time
import theano
import numpy as np
from theano import tensor as T

__author__ = 'Anders'


class ANN:

    def __init__(self):
        self.predictFunc = lambda x : []
        self.trainFunc = lambda x,y : None
        self.weights = []
        self.current_best = 0.

    def init_weights(self, *args):
        for shape in args:
            self.weights.append(theano.shared(floatX(np.random.randn(*shape) * 0.01)))

    def init_training_data(self, model=None, errorFunc=None, learningAlgorithm=None):
        assert not (model is None or errorFunc is None or learningAlgorithm is None)

        X = T.fmatrix()
        Y = T.fmatrix()

        noise_py_x = model(X, 0.2, 0.5, self.weights)
        py_x = model(X, 0., 0., self.weights)

        # Currently the output given the inputs and weights
        # y_x = T.argmax(py_x, axis=1)
        y_x = py_x

        error = T.mean(errorFunc(noise_py_x, Y))
        updates = learningAlgorithm(error, self.weights)

        # train runs "update" on each run (for each image) with the inputs given
        # update includes symbols to update each weight
        self.trainFunc = theano.function(inputs=[X, Y], outputs=None, updates=updates, allow_input_downcast=True)
        # predict use symbol y_x which is given by the model
        self.predictFunc = theano.function(inputs=[X], outputs=y_x, allow_input_downcast=True)

    def train(self,trX, trY, teX=None, teY=None):
        # ONE RUN OVER THE TRAINING SET, RUN IN A SEPARATE THREAD
        def threadTrainingFunc():
            for start, end in zip(range(0, len(trX), 1000), range(1000, len(trX), 1000)):
                #print("trX[start:end] shape: ", trX[start:end].shape)
                #print("trY[start:end] shape: ", trY[start:end].shape)
                self.trainFunc(trX[start:end], trY[start:end])
            if teX is not None and teY is not None:
                self.current_best = np.mean(np.argmax(teY, axis=1) == self.predictFunc(teX))
            print(self.current_best)

        def stopTrainingListener():
            input()
            self.keep_running = False
            return

        self.keep_running = True
        thr = None

        print("use (CTRL-C) keyboard interrupt on unix to stop training")
        print("press enter to stop with stopThr (windows)")
        startTime = time()

        progress = []

        # for i in range(40):
        while self.keep_running:
            stopThr = Thread(target=stopTrainingListener, daemon=True)
            stopThr.start()
            try:
                thr = Thread(target=threadTrainingFunc)
                thr.start()
                thr.join()
            except KeyboardInterrupt:
                # Interrupt happens on main-thread, not on training thread
                self.keep_running = False
                # Do not continue until trainFunc has finished!
                # Prevents inconsistent state?
                thr.join()

            progress.append(self.current_best)

        # print("After 40 runs we acquired a presision of", self.current_best, "on the mnist testing set")
        print("Time elapsed:", time() - startTime)
        
        return progress


    def blind_test(self,cases):
        preds = self.predictFunc(cases)
        return preds.tolist()

def floatX(X):
    return np.asarray(X, dtype=theano.config.floatX)