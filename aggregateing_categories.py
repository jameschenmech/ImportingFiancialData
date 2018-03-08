# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:54:28 2017

@author: James
"""

import pandas as pd
import matplotlib.pyplot as plt

nasdaq = pd.read_excel('listings.xlsx', sheetname='nasdaq', na_values='n/a').dropna()
print(nasdaq.info())

nasdaq['market_cap_m'] = nasdaq['Market Capitalization'].div(1e6)

nasdaq = nasdaq.drop('Market Capitalization', axis=1) #drop column

nasdaq_by_sector = nasdaq.groupby('Sector') #groupby object, like a dictionary

for sector, data in nasdaq_by_sector:
    print(sector, data.market_cap_m.mean())
    
#alternative to for loop to get summary data
mcap_by_sector = nasdaq_by_sector.market_cap_m.mean() #returns a panda series

title = 'NASDAQ = Avg. Market Cap by Sector'

mcap_by_sector.plot(kind='barh', title=title)
plt.xlabel('USD mn')
plt.show()
plt.close()
print(nasdaq_by_sector.mean())

#nyse median capitalization by sector
nyse = pd.read_excel('listings.xlsx', sheetname='nyse', na_values='n/a').dropna()
print(nyse.info())


# Create market_cap_m
nyse['market_cap_m'] = nyse['Market Capitalization'].div(1e6)

# Drop market cap column
nyse = nyse.drop('Market Capitalization', axis=1)

# Group nyse by sector
mcap_by_sector = nyse.groupby('Sector')

# Calculate median
median_mcap_by_sector = mcap_by_sector.market_cap_m.median()

# Plot and show as horizontal bar chart
median_mcap_by_sector.plot(kind='barh', title='NYSE - Median Market Capitalization')

# Add the label
plt.xlabel('USD mn')

# Show the plot
plt.show()
plt.close()

#madian market capitalization by IPO year
listings = []
xls = pd.ExcelFile('listings.xlsx')
records = xls.sheet_names

for record in records:
    listing = pd.read_excel(xls, sheetname=record, na_values='n/a')
    listings.append(listing)
listings = pd.concat(listings)

print(listings.info())

# Show listings head
print(listings.head())

# Create market_cap_m
listings['market_cap_m'] = listings['Market Capitalization'].div(1e6)

# Select companies with IPO after 1985
listings = listings[listings['IPO Year'] > 1985]

# Drop missing values and convert to integers
listings['IPO Year'] = listings['IPO Year'].dropna().astype(int)

# Calculate the median market cap by IPO Year and sort the index
ipo_by_year = listings.groupby('IPO Year').market_cap_m.median().sort_index()

# Plot results as a bar chart
ipo_by_year.plot(kind='bar')

# Show the plot
plt.show()
plt.close()


#all summary statistics
nasdaq = pd.read_excel('listings.xlsx', sheetname='nasdaq', na_values='n/a').dropna()
print(nasdaq.info())

# Inspect NASDAQ data
nasdaq.info()

# Create market_cap_m
nasdaq['market_cap_m'] = nasdaq['Market Capitalization'].div(1e6)

# Drop the Market Capitalization column
nasdaq.drop('Market Capitalization', axis=1, inplace=True)

# Group nasdaq by Sector
nasdaq_by_sector = nasdaq.groupby('Sector')

# Create summary statistics by sector
summary = nasdaq_by_sector.describe()

# Print the summary
print(summary)

# Unstack 
summary = summary.unstack()

# Print the summary again
print(summary)