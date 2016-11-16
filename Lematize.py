__author__ = 'venky'

from nltk.stem import WordNetLemmatizer


def lematization(text):

    st = WordNetLemmatizer()
    modified = []

    for i in range(len(text)):

        vector = []

        for word in text[i].split():

            temp = st.lemmatize(word)
            vector.append(temp)

        modified.append(vector)




    return modified