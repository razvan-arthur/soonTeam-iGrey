#!/usr/bin/env python
# coding: utf-8

# In[8]:


# import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
from ReverseTwitterScraper import TwitterScraper
# import pandas as pd
# from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.neural_network import MLPClassifier
# from sklearn.metrics import accuracy_score
import joblib

chromedriver_path = "C:\soonTeam-iGrey"
cookies = ""  # no account cookies
proxy_list = []
twitter_handle = ["realDonaldTrump"]
scraper = TwitterScraper(twitter_handle, chromedriver_path, cookies, proxy_list)
data = scraper.getTweetsText()

tweetdata = []

for entry in data:
    tweets = entry['tweets']
    for tweet in tweets:
        tweetdata.append(tweet['text'])

loaded_model = joblib.load('model.pkl')
vectorizer = TfidfVectorizer()

# Fit the vectorizer on your training data
vectorizer = joblib.load('vectorizer_check.pkl')

X_test = vectorizer.transform(tweetdata)

# Make predictions
predictions = loaded_model.predict(X_test)
pos=0
cons=0
lista = []
for i in predictions:
    if i == "positive":
        pos+=1;
        lista.append(1)
    if i == "negative":
        lista.append(-1)
        cons+=1

indice = np.sum(lista) / len(lista)
print( indice)
if (cons!=0):
    pred= pos/cons
    print(  pred)

# In[ ]:




