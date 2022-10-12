import numpy as np
import pandas as pd
import yfinance as yf
import pandas_datareader.data as dreader
import pandas_ta as ta
import matplotlib.pyplot as plt
from datetime import date

plt.style.use('fivethirtyeight')
yf.pdr_override()

# Extracting Data
stock_symbole = ['TATAMOTORS.NS']
start_date = date(2022,5,5)
end_date = date.today()

def getMyPortfolio(stocks = stock_symbole, start = start_date, end = end_date):
    data = dreader.get_data_yahoo(stocks , data_source='yahoo' , start=start ,end=end )
    return data

data = getMyPortfolio()

# implementing the startegy

