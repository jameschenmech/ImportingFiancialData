# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 12:43:56 2017

@author: James
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

nasdaq = pd.read_excel('listings.xlsx', sheetname='nasdaq', na_values='n/a').dropna()
nasdaq['market_cap_m']=nasdaq['Market Capitalization'].div(1e6)
nasdaq.drop('Market Capitalization', axis=1, inplace=True)


sns.countplot(x='Sector', data=nasdaq)#number of counts per catagory

plt.xticks(rotation=45)

plt.close()

sector_size = nasdaq.groupby('Sector').size()

order = sector_size.sort_values(ascending=False)

print(order.head())

order = order.index.tolist() #extract index as list

#plot as sorted data
sns.countplot(x='Sector', data = nasdaq, order=order)
plt.xticks(rotation=45)
plt.title('# Observations per Sector')
plt.show()         

#countplot with multiple categoris
recent_ipos = nasdaq[nasdaq['IPO Year'] > 2014]

recent_ipos['IPO Year'] = recent_ipos['IPO Year'].astype(int)

sns.countplot(x='Sector', hue = 'IPO Year', data=recent_ipos)
plt.xticks(rotation=90)
plt.show()
plt.close()

#compare catagorical stats with pointplot
nasdaq['IPO'] = nasdaq['IPO Year'].apply(lambda x:
                'After 2000' if x>2000 else 'Before 2000')
sns.pointplot(x='Sector', y='market_cap_m', hue='IPO', data=nasdaq)
plt.xticks(rotation=45)
plt.title('Mean Market Cap')
plt.show()
plt.close()

#countplot IPO stocks in each index over time
# Select IPOs after 2000
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

listings = listings[listings['IPO Year'] > 2000]

# Convert IPO Year to integer
listings['IPO Year'] = listings['IPO Year'].astype(int)

# Create a countplot
sns.countplot(x='IPO Year', hue='Exchange', data=listings)

# Rotate xticks and show result
plt.xticks(rotation=45)

# Show the plot
plt.legend(loc='upper left')
plt.ylim(0,200)
plt.show()
plt.close()

#calculate several metrics by sector and IPO year
# Exclude IPOs before 2000 and from the 'amex'
listings = listings[(listings['IPO Year'] > 2000) & (listings.Exchange != 'amex')]

# Convert IPO Year to integer
listings['IPO Year'] = listings['IPO Year'].astype(int)

# Exclude outliers
listings = listings[listings.market_cap_m < listings.market_cap_m.quantile(.95)]

# Create the pointplot
sns.pointplot(x='IPO Year', y='market_cap_m', hue='Exchange', data=listings)

# Rotate xticks
plt.xticks(rotation=45)

# Show the plot
plt.show()
plt.close()
