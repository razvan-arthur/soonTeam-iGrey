#!/usr/bin/env python
# coding: utf-8

# In[17]:


from sklearn import svm
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.model_selection import train_test_split
import timeit
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pickle
from sklearn.metrics import accuracy_score, classification_report


# In[14]:





# In[39]:



loaded_model = pickle.load(open('sentiment_model.pkl', 'rb'))
vectorizer = TfidfVectorizer()
# Predict sentiment labels for the testing data
new_text = ["don't like!", "This movie is ok."]
new_text_vectorized = vectorizer.transform(new_text)
predicted_sentiments = loaded_model.predict(new_text_vectorized)
for text, sentiment in zip(new_text, predicted_sentiments):
    print(f"Text: {text}\nPredicted Sentiment: {sentiment}\n")


# In[38]:





# In[43]:





# In[4]:





# In[ ]:




