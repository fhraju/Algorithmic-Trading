# Here I will build a equal weight S&P500 index
import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

from secretskeys import IEX_CLOUD_API_TOKEN

# import list of stocks
stocks = pd.read_csv('StocksintheSP500Index.csv')

#Api call
symbol = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()

price = data['latestPrice']
marketcap = data['marketCap']

#adding our Stocks data to pandas dataframe
added_columns = ['Ticker', 'Stock Price', 'Market Capitalization', 'Number of Shares to Buy']
final_dataframe = pd.DataFrame(columns=added_columns)

final_dataframe.append(pd.Series[
    symbol,
    price,
    marketcap,
    'N/A',
])
print(final_dataframe)