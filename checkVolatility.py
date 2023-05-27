from pytrends.request import TrendReq
import numpy as np
import pandas as pd

data = pd.read_csv("./data/all_stocks_5yr.csv")


def calculateDailyReturns(stock_dataframe):
    dailyReturns = []  # list for a single stock's dataframe
    for i in range(1, stock_dataframe["date"].size):
        todayClose = stock_dataframe.loc[i].at["close"]
        yesterdayClose = stock_dataframe.loc[i - 1].at["close"]
        dailyReturn = ((todayClose - yesterdayClose) / yesterdayClose) * 100
        dailyReturns.append(dailyReturn)
    return dailyReturns


def check_volatility(keyword):
    pytrends = TrendReq(hl='en-US', tz=360)

    pytrends.build_payload([keyword], cat=0, timeframe='today 5-y', geo='', gprop='')

    name2id = {}
    id2name = {}
    stock_names = data["Name"].unique()
    for i in range(len(stock_names)):
        stock_name = stock_names[i]
        id2name[i] = stock_name
        name2id[stock_name] = i

    stock_dataframes = {}

    for stock in stock_names:
        stock_df = data[data['Name'] == stock].copy()
        stock_df.reset_index(drop=True, inplace=True)
        stock_dataframes[stock] = stock_df

    dailyReturnsAll = []  # list of lists, each list contains a certain stock's daily return values
    for i in range(len(stock_dataframes)):
        stock_name = id2name[i]
        dailyReturnsAll.append(calculateDailyReturns(stock_dataframes[stock_name]))

    dailyReturnsMean = []  # a list of length == dailyReturnsAll == number of stocks
    for i in range(len(stock_dataframes)):
        mean = np.mean(dailyReturnsAll[i])
        dailyReturnsMean.append(mean)
    # print(dailyReturnsMean)

    deviations = []  # a list of lists again, identical in shape to dailyReturnsAll
    for i in range(len(stock_dataframes) - 1):  # for each stock dataframe
        temporary_sublist = []
        for j in range(len(stock_dataframes[id2name[i]]) - 1):  # j goes up to each dataframe's number of entries
            value = dailyReturnsAll[i][j] - dailyReturnsMean[i]
            temporary_sublist.append(value)
        deviations.append(temporary_sublist)

    squaredDeviations = []
    for i in range(len(deviations)):
        temporary_sublist2 = []
        for j in range(len(deviations[i])):
            value = np.square(deviations[i][j])
            temporary_sublist2.append(value)
        squaredDeviations.append(temporary_sublist2)

    variances = []

    for stock_deviations in deviations:
        variance = np.var(stock_deviations)
        variances.append(variance)

    volatilities = []
    for variance in variances:
        volatilities.append(np.sqrt(variance))

    volatility = volatilities[name2id[keyword]]

    return volatility