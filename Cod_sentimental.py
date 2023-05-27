from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import joblib
from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")

Keyword = "trump"
Keyword_data = Keyword.replace(" ", "+")

pages = 3
url = 'https://nitter.net/search?f=tweets&q=' + Keyword_data

for i in range(pages):

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)
    time.sleep(15)

    tweet_final = []
    uname_final = []
    timesupremacy = []

    previous_height = 0
    while True:
        height = driver.execute_script("""
                function getActualHeight(){
                    return Math.max(
                        Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
                        Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
                        Math.max(document.body.clientHeight, document.documentElement.clientHeight)
                    );
                }
                return getActualHeight()
            """)

        driver.execute_script(f"window.scrollTo({previous_height},{previous_height + 300})")
        time.sleep(1)
        previous_height += 300

        if previous_height >= height:
            break

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    tweets = soup.findAll('div', {"class": "tweet-content media-body"})

    tweet_list = [x.text.encode('utf-8').decode('utf-8') for x in tweets]

    # print(tweet_list)


# In[39]:



loaded_model = pickle.load(open('sentiment_model.pkl', 'rb'))
vectorizer = TfidfVectorizer()
# Predict sentiment labels for the testing data
# new_text = ["don't like!", "This movie is ok."]
vectorizer = joblib.load('vector.pkl')
new_text_vectorized = vectorizer.transform(tweet_list)
predicted_sentiments = loaded_model.predict(new_text_vectorized)
predicted_sentiments = [1 if x == 4 else x for x in predicted_sentiments]
percentage = (predicted_sentiments.count(1) / len(predicted_sentiments)) * 100

print("Percentage of positive tweets: {:.2f}%".format(percentage))
# for text, sentiment in zip(new_text, predicted_sentiments):
#     print(f"Text: {text}\nPredicted Sentiment: {sentiment}\n")


'''
X_train_vectorized = vectorizer.fit_transform(X_train)
joblib.dump(vectorizer, 'vectorizer_check.pkl')
'''