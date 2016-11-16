__author__ = 'venky'

from sklearn import svm


def getmodel(input,label):

    model = svm.SVC()
    model.fit(input,label)

    return model

