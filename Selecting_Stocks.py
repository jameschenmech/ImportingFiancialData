# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:14:54 2017

@author: James
"""
import pandas as pd
from pandas_datareader.data import DataReader
import matplotlib.pyplot as plt
from datetime import date #Date & time functionality

#selecting stocks and get data from Google Finance
nyse = pd.read_excel('listings.xlsx', sheetname='nyse', na_values='n/a')

nyse = nyse.sort_values('Market Capitalization', ascending=False)

nyse[['Stock Symbol', 'Company Name']].head(3)

largest_by_market_cap = nyse.iloc[0] # 1st Row

largest_by_market_cap['Stock Symbol'] #Select row label

#Alterantive more elegant way to get largest company
nyse = nyse.set_index('Stock Symbol')  #Stock ticker as index
nyse['Market Capitalization'].idxmax() #Index of max value

nyse['Sector'].unique()  #Unique values as numpy array

tech = nyse.loc[nyse.Sector == 'Technology']  #only select Technology stocks

nyse.loc[nyse.Sector == 'Technology', 'Market Capitalization'].idxmax()

ticker = nyse.loc[(nyse.Sector == 'Technology') & (nyse['IPO Year']==2017),
                  'Market Capitalization'].idxmax()

data = DataReader(ticker, 'google') #Start: 2010/1/1
data = data.loc[:,['Close', 'Volume']] 
#alternative data =  data[['Close','Volume']]

data.plot(title=ticker, secondary_y = 'Volume')
plt.tight_layout()
plt.show()

#select the top 5 listed consumer companies
xls = pd.ExcelFile('listings.xlsx') # pd.ExcelFile object
exchanges = xls.sheet_names #exhcange contails the sheet names
listings = [] #listings is an empty list

for exchange in exchanges:
    listing = pd.read_excel(xls, sheetname=exchange)
    listing['Exchange'] = exchange
    listings.append(listing) #Add DataFrame to list
combined_listings = pd.concat(listings) #create a DataFrame out of list

consumer_services = combined_listings.loc[combined_listings.Sector == 'Consumer Services']
#alternative
# Select companies in Consumer Services
consumer_services = combined_listings[combined_listings.Sector == 'Consumer Services']

# Sort consumer_services by market cap
consumer_services2 = consumer_services.sort_values('Market Capitalization', ascending=False)

# Display first 5 rows of designated columns
print(consumer_services2[['Company Name', 'Exchange', 'Market Capitalization']].head())


#Get the ticker of the largest comsumer services company
# Set the index of listings to Stock Symbol
listings = pd.DataFrame.copy(combined_listings)
listings = listings.set_index('Stock Symbol')

# Get ticker of the largest Consumer Services company
ticker = listings.loc[listings.Sector=='Consumer Services', 'Market Capitalization'].idxmax()

# Set the start date
start = date(2012,1,1)

# Import the stock data
data = DataReader(ticker,'google', start)

# Plot Close and Volume
data[['Close', 'Volume']].plot(secondary_y='Volume', title=ticker)

# Show the plot
plt.show()

#get the largest comsumer company listed after 1998
# Set Stock Symbol as the index
#listings = listings.set_index('Stock Symbol')

# Get ticker of the largest consumer services company listed after 1997
ticker = listings.loc[(listings.Sector == 'Consumer Services') & (listings['IPO Year'] > '1998'), 'Market Capitalization'].idxmax()

# Set the start date
start = date(1998,1,1)

# Import the stock data
data = DataReader(ticker, 'google', start)

# Plot Close and Volume
data[['Close', 'Volume']].plot(secondary_y='Volume',title=ticker)

# Show the plot
plt.show()