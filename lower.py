__author__ = 'venky'

import  re
import  string
import timeit

def lower(text):

    loweredText = []

    for i in range(len(text)):

        loweredText.append(text[i].lower())

    pun = removePunctuations(loweredText)
    return pun

def removePunctuations(data):

    #text =[]
    #exclude = set(string.punctuation)

    for i in range(len(data)):

        for c in string.punctuation:

            data[i] = data[i].replace(c," ")
        #text.append(data[i])

    return  data





'''
data = []

data.append("Rated This place is good alternate for the people who frequently go to hauz khas village for these types of joints. Food is good but service needs improvement. Like 2 0 Submit")
data.append("Seriously awful never again!!!! It was totally dead and i see why. They didn't have ranch and didn't seem to care about our needs at all. I know it's suppose to be some sort of gimmick but at least back it up with some good pizza !")

end = lower(data)

print end[0] '''
