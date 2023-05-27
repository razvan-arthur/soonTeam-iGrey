#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import joblib

examples = [
    "I love the equality",
    "I like you",
    "I am a person"
]
loaded_model = joblib.load('model.pkl')
vectorizer = TfidfVectorizer()

# Fit the vectorizer on your training data
vectorizer = joblib.load('vectorizer_check.pkl')

X_test = vectorizer.transform(examples)

# Make predictions
predictions = loaded_model.predict(X_test)


lista=[]
for i in predictions:
    if i == "positive":
        lista.append(1)
    if i == "neutral":
        lista.append(0.5)
    if i == "negative":
        lista.append(0)

indice = np.sum(lista)/len(lista)
print(indice)


# In[ ]:




