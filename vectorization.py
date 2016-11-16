__author__ = 'venky'


import  csv


def getVector(text):


    features = list(csv.reader(open("/home/venky/Sem1/Machine Learning/Project/featurewords.txt")))


    '''featurevector =[]

    for i in range(len(features)):

        featurevector.append(features[0][i])'''

    featurevector =[]

    for i in range(23):

        featurevector.append(features[0][i])

    inputvector  = []

    for i in range(len(text)):

        vector = []

        for j in range(len(featurevector)):

            if featurevector[j] in text[i]:

                vector.append(1)

            else:

                vector.append(0)

        inputvector.append(vector)

    return inputvector





