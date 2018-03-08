# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:59:36 2017

@author: James
"""

from pandas_datareader.data import DataReader
from datetime import date #Date & time functionality
import matplotlib.pyplot as plt
import pandas as pd

start = date(2015, 1, 1)
end = date(2016, 12, 31)

ticker = 'GOOG'

data_source = 'google'

stock_data = DataReader(ticker, data_source, start, end)
(stock_data.info())


stock_data['Close'].plot(title=ticker)
plt.show()

#Economic data from the Federal Reserve, FRED
series_code = 'DGS10'  #10-year Treasury Rate

data_source = 'fred'  #FED Economic Data Service

start = date(1962, 1 ,1) #start date from earliest available, skip end date

data = DataReader(series_code, data_source, start)

data.info()

series_name = '10-year Treasury'

data = data.rename(columns={series_code: series_name}) 
#could also do data.columns = [series_name]

data.plot(title = series_name)
plt.show()

#Combine stock and economic data
start = date(2000, 1, 1)

series = 'DCOILWTICO' #West Texas Intermediate Oil Price

oil = DataReader(series, 'fred', start)

ticker = 'XOM' #Exxon Mobile Corporation

stock = DataReader(ticker, 'google', start)

data2 = pd.concat([stock[['Close']], oil], axis=1) #[['Close']] is DataFrame
                                                    #['Close'] is DataSeries
                                                    #axis=1 horizontal concat
data2.columns= ['Exxon', 'Oil Price'] #rename DataFrame columns

data2.plot()
plt.show()

#gold prices
# Set start date
start = date(1968, 1, 1)

series = 'GOLDAMGBD228NLBM'

# Import the data
gold_price = DataReader(series, 'fred', start=start)

# Inspect the price of gold
gold_price.info()

# Plot the price of gold
gold_price.plot(title='Gold Price')

# Show the plot
plt.show()

#unemployment rate and participation Rate
# Set the start date
start = date(1950, 1, 1)

# Define the series codes
series = ['UNRATE', 'CIVPART']

# Import the data
econ_data = DataReader(series, 'fred', start=start)

# Assign new column labels
econ_data.columns = ['Unemployment Rate', 'Participation Rate']

# Plot econ_data
econ_data.plot(subplots=True, title='Labor Market')

# Show the plot
plt.show()

#compare bond and stock performance
# Set the start date
start = date(2008, 1,1)

# Set the series code
series = ['BAMLHYH0A0HYM2TRIV', 'SP500']

# Import the data
data = DataReader(series, 'fred', start)

# Plot the results
data.plot(subplots=True, title='Performance Comparison')

# Show the plot
plt.show()

