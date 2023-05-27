from flask import Flask, render_template, request, redirect, url_for
from checktrend import check_trend_interest

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        trend = request.form['trend']
        trendValue = check_trend_interest(trend)

        return render_template('success.html', trend=trendValue)
    
    # Render the form page for GET requests
    return render_template('form.html')

if __name__ == '__main__':
    app.run()
