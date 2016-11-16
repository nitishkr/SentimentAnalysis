__author__ = 'venky'



from nltk.corpus import stopwords

def removeStopWords(text):

    #fix_encoding = lambda s: s.decode('utf8', 'ignore')
    cachedStopWords = stopwords.words("english")

    for i in range(len(text)):

        text[i] = ' '.join([word for word in text[i].split() if word not in cachedStopWords])

    return text

'''
data = []

data.append("Rated This place is good alternate for the people who frequently go to hauz khas village for these types of joints. Food is good but service needs improvement. Like 2 0 Submit")
data.append("Seriously awful never again!!!! It was totally dead and i see why. They didn't have ranch and didn't seem to care about our needs at all. I know it's suppose to be some sort of gimmick but at least back it up with some good pizza !")

end = removeStopWords(data)

print end[0]'''