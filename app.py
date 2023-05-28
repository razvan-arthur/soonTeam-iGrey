from flask import Flask, render_template, request, redirect, url_for
from checktrend import check_trend_interest
from Predictie_Controversat import check_controversy
from Cod_sentimental import check_sentiment
from checkVolatility import check_volatility
from statistics import mean
from sklearn import preprocessing

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        values = []
        trend = request.form['trend']
        trendValue = check_trend_interest(trend)
        values.append(trendValue)
        controversy = request.form['controversy']
        controversyValue = check_controversy(controversy)
        values.append(controversyValue)
        sentiment = request.form['sentiment']
        sentimentValue = check_sentiment(sentiment)
        values.append(sentimentValue)
        volatility = request.form['volatility']
        print(volatility)
        print(volatility == "php")
        volatilityValue = 1
        if (volatility != "php"):
            volatilityValue = check_volatility(volatility)
        volatilityValue = (volatilityValue / 4.16)*2
        volatilityValue = 2- volatilityValue
        list_avg = mean(values)
        finalValue = list_avg*volatilityValue
        return render_template('success.html', trend=int(trendValue), controversy = int(controversyValue), sentiment=int(sentimentValue), volatility=volatilityValue, final=int(finalValue))
    
    # Render the form page for GET requests
    return render_template('form.html')

if __name__ == '__main__':
    app.run()
