__author__ = 'venky'


from preprocessing import preprocess
from vectorization import getVector

from model import getmodel

def trainmodel():

    sentiment = []
    text = []
    with open("/home/venky/Sem1/Machine Learning/Project/Data/training.csv") as file:

        linedata = []

        for line in file:

            linedata = line.split("|")
            sentiment.append(linedata[0])
            text.append(linedata[1])

    label = []
    for i in range(len(sentiment)):

        if sentiment[i] == "positive":

            label.append(1)

        else:

            label.append(0)

    preprocessedText = preprocess(text)

    input = getVector(preprocessedText)

    model = getmodel(input,label)

    return model





