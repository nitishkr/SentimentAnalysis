__author__ = 'venky'

from Stemming import  stem
from stopwords import removeStopWords
from lower import lower

from Lematize import lematization


def preprocess(text):

    loweredText = lower(text)

    afterStopWordsRemove = removeStopWords(loweredText)

    #afterStem = stem(afterStopWordsRemove)

    afterlem = lematization(afterStopWordsRemove)
    return afterlem;


'''
data = []

data.append("good,nice,bad,ugly,not,great,sizzle,delicious,inferior,awful,horrible,cheap,best,sour,amaze,disappoint,excellent,love,delicious,horrible,worst,never")
data.append("Seriously awful never Horrible!!!! It was totally dead and i see why. They didn't have ranch and didn't seem to care about our needs at all. I know it's suppose to be some sort of gimmick but at least back it up with some good pizza !")

end = preprocess(data)
print end[0]
print end[1]'''









