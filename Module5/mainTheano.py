__author__ = 'Anders'

import Module5.basics.mnist_basics as mnist
import theano

def preprocessFeatureSets(feature_sets):
    theano.test()
    # for i in range(len(feature_sets)):
    #     feature_sets[i] = (feature_sets[i] - feature_sets[i].min())/(feature_sets[i].max() - feature_sets[i].min())
    #
    # print()

preprocessFeatureSets(mnist.load_mnist())


class MNN:
    def __init__(self):
        a = 0

    def blind_test(self, feature_sets):
        pass

