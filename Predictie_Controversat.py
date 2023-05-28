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
import os
import sys

username = sys.argv[1]
def write_result(value):
    with open('controversy-result.txt', 'w') as file:
        file.write(str(value))
def check_controversy(username):
    userList=[]
    userList.append(username)
    current_path = os.getcwd()
    chromedriver_path = current_path + "/chromedriver"
    cookies = ""  # no account cookies
    proxy_list = []
    twitter_handle = userList
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

    # indice = np.sum(lista) / len(lista)
    # print( indice)
    pred = 100 - (pos/len(predictions) * 100)
    write_result(pred)
    return pred

    # In[ ]:

check_controversy(username)


