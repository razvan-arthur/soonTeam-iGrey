from flask import Flask, render_template, request, redirect, url_for
from checktrend import check_trend_interest
from Predictie_Controversat import check_controversy
from Cod_sentimental import check_sentiment
from checkVolatility import check_volatility

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        trend = request.form['trend']
        trendValue = check_trend_interest(trend)
        controversy = request.form['controversy']
        controversyValue = check_controversy(controversy)
        sentiment = request.form['sentiment']
        sentimentValue = check_sentiment(sentiment)
        volatility = request.form['volatility']
        volatilityValue = check_volatility(volatility)

        return render_template('success.html', trend=trendValue, controversy = controversyValue, sentiment=sentimentValue, volatility=volatilityValue )
    
    # Render the form page for GET requests
    return render_template('form.html')

if __name__ == '__main__':
    app.run()
