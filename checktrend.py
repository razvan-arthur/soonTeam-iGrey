from pytrends.request import TrendReq

def check_trend_interest(keyword):
    pytrends = TrendReq(hl='en-US', tz=360)

    pytrends.build_payload([keyword], cat=0, timeframe='today 5-y', geo='', gprop='')
    interest_over_time_df = pytrends.interest_over_time()

    if interest_over_time_df.empty:
        print(f"No data available for the keyword '{keyword}'.")
        return None

    current_interest = interest_over_time_df[keyword].iloc[-1]
    interest_percentage = (current_interest / 100) * 100

    return interest_percentage

