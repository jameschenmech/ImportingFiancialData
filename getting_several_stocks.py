# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:33:39 2017

@author: James
"""

import pandas as pd
from pandas_datareader.data import DataReader
from datetime import date #Date & time functionality
import matplotlib.pyplot as plt

nasdaq = pd.read_excel('listings.xlsx', sheetname='nasdaq', na_values='n/a')

nasdaq.set_index('Stock Symbol', inplace = True)

top_5 = nasdaq['Market Capitalization'].nlargest(n=5).div(1e6)

tickers = top_5.index.tolist() #Convert index to list

panel = DataReader(tickers, 'google', start=date(2015,1 ,1))

data = panel.to_frame()

unstacked = data['Close'].unstack() #from long to wide format

unstacked.plot(subplots=True)

plt.tight_layout()
plt.show()

#get data for the 3 largest financial companies
# Set Stock Symbol as the index
xls = pd.ExcelFile('listings.xlsx')
exchanges = xls.sheet_names

listings = []
for exchange in exchanges:
    listing = pd.read_excel(xls, sheetname=exchange)
    listings.append(listing)

listings = pd.concat(listings)

listings = listings.set_index('Stock Symbol')

# Get ticker of 3 largest finance companies
top_3_companies = listings.loc[listings.Sector=='Finance', 'Market Capitalization'].nlargest(n=3)

# Convert index to list
top_3_tickers = top_3_companies.index.tolist()

# Set start date
start = date(2012,1,1)

# Import stock data
data = DataReader(top_3_tickers,'google',start)
data2 = data.to_frame()

# Unstack and inspect result
data2['Close'].unstack().info()