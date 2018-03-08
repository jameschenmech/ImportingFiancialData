# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 11:52:32 2017

@author: James
"""

import pandas as pd
import matplotlib.pyplot as plt

nasdaq = pd.read_excel('listings.xlsx', sheetname='nasdaq', na_values='n/a')

nasdaq['market_cap_m'] = nasdaq['Market Capitalization'].div(1e6)

by_sector = nasdaq.groupby('Sector')

by_sector.market_cap_m.agg(['size', 'mean']).sort_values('size') #several aggregations by category
#servel aggregations plus new labels
by_sector.market_cap_m.agg({'#Obs':'size', 'Average':'mean'})

#different statistics by column
by_sector.agg({'market_cap_m':'size', 'IPO Year':'median'})

#aggregate by two categories
by_sector_year = nasdaq.groupby(['Sector', 'IPO Year'])

print(by_sector_year.market_cap_m.mean())

#select from multiindex()
mcap_sector_year = by_sector_year.market_cap_m.mean()

print(mcap_sector_year.loc[['Basic Industries', 'Transportation']])

#company value by exchange and sector
listings = []
xls = pd.ExcelFile('listings.xlsx')
exchanges = xls.sheet_names

for exchange in exchanges:
    listing = pd.read_excel(xls, sheetname=exchange, na_values='n/a').dropna()
    listing['Exchange'] = exchange
    listings.append(listing)
listings = pd.concat(listings)
listings['market_cap_m'] = listings['Market Capitalization'].div(1e6)
listings.drop('Market Capitalization', axis=1, inplace=True)

# Group listings by Sector and Exchange
by_sector_exchange = listings.groupby(['Sector', 'Exchange'])

# Calculate the median market cap
mcap_by_sector_exchange = by_sector_exchange.market_cap_m.median()

# Display the head of the result
print(mcap_by_sector_exchange.head())

# Unstack mcap_by_sector_exchange
mcap_unstacked = mcap_by_sector_exchange.unstack()

# Plot as a bar chart
mcap_unstacked.plot(kind='bar', title='Median Market Capitalization by Exchange')

# Set the x label
plt.xlabel('USD mn')

# Show the plot
plt.show()
plt.close()

#calculate several metrics by sector and exchange
# Subset market_cap_m of by_sector_exchange
bse_mcm = by_sector_exchange['market_cap_m']

# Calculate mean, median, and std in summary
summary = bse_mcm.agg({'Average': 'mean', 'Median': 'median', 'Standard Deviation': 'std'})

# Print the summary
print(summary)
