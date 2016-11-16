__author__ = 'venky'


from preprocessing import preprocess
from vectorization import getVector

def gettestvector():

    testdata = []

    with open("/home/venky/Sem1/Machine Learning/Project/Data/testing") as file:


        for line in file:

            testdata.append(line)


    preprocessedText = preprocess(testdata)

    testinput = getVector(preprocessedText)


    return testinput

