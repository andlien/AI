__author__ = 'Anders'

import numpy as np

class ANN:

    def __init__(self, newPredict):
        self.predictFunc = newPredict

    def train(self, train, trX, trY, teX, teY):
        # ONE RUN OVER THE TRAINING SET, RUN IN A SEPARATE THREAD
        def trainFunc():
            for start, end in zip(range(0, len(trX), 900), range(900, len(trX), 900)):
                #print("trX[start:end] shape: ", trX[start:end].shape)
                #print("trY[start:end] shape: ", trY[start:end].shape)
                train(trX[start:end], trY[start:end])
            print (np.mean(np.argmax(teY, axis=1) == self.predictFunc(teX)))

        def stopTrainingListener():
            input()
            global keep_running
            keep_running = False

        print("Start looping")
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

    def blind_test(self,cases):
        preds = self.predictFunc(cases)
        predFormated = [0] * len(preds)
        for x in range(0,len(preds)):
            predFormated[x] = preds[x]

        return predFormated