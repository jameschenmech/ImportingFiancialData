# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 15:54:52 2017

@author: James
"""

# Import DataReader
from pandas_datareader.data import DataReader
import pandas as pd
# Import date
from datetime import date

# Set start and end dates
start = date(2016,1,1)
end = date(2017,12,31)

# Set the ticker
tickers = ['AAPL','XOM']

# Set the data source
data_source = 'google'

# Import the stock prices
stock_prices=pd.DataFrame()

#for ticker in tickers: 
#    print(ticker)
stock_prices = DataReader(tickers, data_source, start, end)
#    stock_prices.append(stock_price)
    
# Display and inspect the result
#print(stock_prices.head())
#stock_prices.info()


#--
top_3_tickers = ['JPM', 'WFC', 'BAC']

# Set start date
start = date(2012,1,1)

# Import stock data
data = DataReader(top_3_tickers,'google',start)
data2 = data.to_frame()

# Unstack and inspect result
data2['Close'].unstack().info()