__author__ = 'venky'

from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer



def stem(text):

    modified = []
    #st = LancasterStemmer()
    #st = SnowballStemmer()
    st = PorterStemmer()

    for i in range(len(text)):

        vector = []

        for word in text[i].split():

            temp = st.stem(word)
            vector.append(temp)

        modified.append(vector)


    return modified