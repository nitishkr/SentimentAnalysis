
# coding: utf-8

# In[108]:

import nltk
import urllib
from __future__ import division

import csv
from string import punctuation
files=['negative.txt','positive.txt','obama_tweets.txt']
path='http://www.unc.edu/~ncaren/haphazard/'
for file_name in files:
    urllib.urlretrieve(path+file_name,file_name)
tweets = open("empire.csv").read()

tweets_list = tweets.split('\n')



pos_sent = open("positive.txt").read()
positive_words=pos_sent.split('\n')
positive_counts=[]

neg_sent = open('negative.txt').read()
negative_words=neg_sent.split('\n')
negative_counts=[]
positive =[]
negative =[]
label=[]
pt=[]
ptr=[]

tweets_list = tweets_list[2:]
tweets_list = tweets_list[:-3]
for tweet in tweets_list:
    positive_counter=0
    negative_counter=0
    
    
    tweet_processed=tweet.lower()
    x = tweet_processed.find("rated")
    tweet_processed = tweet_processed[x+9:]
    x = tweet_processed.rfind("like")
    tweet_processed = tweet_processed[:x]
    y = tweet_processed.find("empire restaurant: dear")
    tweet_processed = tweet_processed[:y]
    print y,tweet_processed
   
    for p in list(punctuation):
        tweet_processed=tweet_processed.replace(p,'')
    
    tweet_processed=tweet_processed.strip()
    tweet_processed=' '.join(tweet_processed.split())
    words=tweet_processed.split(' ')
    
    word_count=len(words)
    pos_word=""
    neg_word=""
    for word in words:
        if word in positive_words:
            positive_counter=positive_counter+1
            pos_word=pos_word+", "+word
        elif word in negative_words:
            negative_counter=negative_counter+1
            neg_word=neg_word+", "+word
    positive.append(pos_word)
    negative.append(neg_word)
    positive_counts.append(positive_counter/word_count)
    negative_counts.append(negative_counter/word_count)
    pt.append(tweet_processed)
    if (positive_counter>negative_counter):
        label.append("positive")
        x = "positive"
    else: 
        label.append("negative")
        x = "negative"
    ptr = ptr +[(tweet_processed,x)]
print len(positive_counts)

#output=zip(tweets_list,positive_counts,negative_counts,positive,negative)
testfile = zip(pt,label)
writer = csv.writer(open('data.csv', 'wb'))
writer.writerows(testfile)







# In[66]:


pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive')]
pos_tweets = pos_tweets+[("heelo",'billo')]
print pos_tweets


# In[109]:

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative')]

len(tweet)
tweets = []
for (words, sentiment) in ptr:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    tweets.append((words_filtered, sentiment))


# In[72]:

print tweets


# In[6]:

test_tweets = [
    (['feel', 'happy', 'this', 'morning'], 'positive'),
    (['larry', 'friend'], 'positive'),
    (['not', 'like', 'that', 'man'], 'negative'),
    (['house', 'not', 'great'], 'negative'),
    (['your', 'song', 'annoying'], 'negative')]


# In[110]:

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


# In[111]:

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words


# In[112]:

word_features = get_word_features(get_words_in_tweets(tweets))


# In[113]:

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


# In[114]:

training_set = nltk.classify.apply_features(extract_features, tweets)


# In[115]:

training_set


# In[116]:

classifier = nltk.NaiveBayesClassifier.train(training_set)


# In[16]:

print classifier.show_most_informative_features(32)


# In[205]:

tweet = "iftaar feast at koramangala now we discovered this today starting from empire hotel upwards there were food stalls serving biryani by biryani house sufi restuarant empire and other restuarants too there were a few live counters next to chungwah restuarant serving seekh kababs samosas kababs and haleem you cant compare the ambience to mosque road iftaar food since thats on much larger scale but for those who are this side of town and do not want to go through a mela atmosphere jam packed ambience should visit this street and enjoy the iftaar meal empire restaurant thank you ms shivangi enjoy it as long as it lasts and make the best of it"

sentiment=[]
text=[]
with open ("testing") as file:
    linedata=[]
    for line in file:
        text.append(line[0])

cor = 0
fal = 0
for i in range(len(sentiment)):
    if classifier.classify(extract_features(text[i].split()))  in sentiment[i]: 
        cor = cor+1
    else:
        fal = fal+1


# In[207]:

print text


# In[32]:




# In[34]:

twitter_samples.strings('negative_tweets.json')


# In[105]:

abc = "i would always suggest empire only if you want to satisfy your midnight hunger or for a quick bite after a post drinking session it was on a lazy friday afternoon i planned to visit empire lunch buffet i was surprised to see many a items not there in the menu years back they had salads papads gobimanchuri soup fish curry mutton curry and many more for rs99 current price of the buffet is rs169 to speak about the a la carte they have moderate pricing but there are lot of other restaurants in bangalore who serve good food at the same price — with amarnath sutar"
abc ="blah no more empire hopping after late night parties or hangouts this place is very famous and almost everyone who visits bangalore will get to know about this place they are in high demand for their late night delivery i like their empire special chicken kebabs very bad hospitality if you are visiting the restaurant i think i neednt tell anything about their location empire itself is known to be a landmark in koramangala empire restaurant dear mrmathew thank you for your valued feed back we are going through all the feedback that we get from our patrons to make sure they are more than satisfied at all times it is the feedback like yours that helps us in betterment and refinement i will look into the service part and improve on it please do visit us again for us to serve you better thanking you junaiz k coo gm 9945888855 empire group of "
abc ="blah  no more empire hopping after late night parties or hangouts this place is very famous and almost everyone who visits bangalore will get to know about this place they are in high demand for their late night delivery i like their empire special chicken kebabs very bad hospitality if you are visiting the restaurant i think i neednt tell anything about their location empire itself is known to be a landmark in koramangala empire restaurant dear mrmathew thank you for your valued feed back  we are going through all the feedback that we get from our patrons to make sure they are more than satisfied at all times it is the feedback like yours that helps us in betterment and refinement i will look into the service part and improve on it please do visit us again for us to serve you better thanking you junaiz k coo  gm 9945888855 empire group of hotels"
print abc.rfind("empire restaurant dear")


# In[106]:

print abc[:427]


# In[ ]:



