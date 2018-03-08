# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 13:26:43 2018

@author: James
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:33:39 2017

@author: James
"""

import pandas as pd
from pandas_datareader.data import DataReader
from datetime import date #Date & time functionality


# =============================================================================
# #get data for top 25 stocks from nasdaq
# #suprisingly google only returns data from 2002 to present
# =============================================================================
nasdaq = pd.read_excel('../listings.xlsx', sheetname='nasdaq', na_values='n/a')

nasdaq.set_index('Stock Symbol', inplace = True)

top_25 = nasdaq['Market Capitalization'].nlargest(n=25).div(1e6)

tickers = top_25.index.tolist() #Convert index to list

panel = DataReader(tickers, 'google', start=date(1970,1 ,1))

data = panel.to_frame()
#Data is a multi-index.  Trying to save this as a csv will unstack the multi-index

unstacked = data['Close'].unstack() #from long to wide format

unstacked.to_csv('nasdaq_25.csv')

#Now we have the historical data for 25 top Nasdaq stocks
