# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:15:29 2017

@author: James
"""
import pandas as pd
import matplotlib.pyplot as plt

amex = pd.read_excel('listings.xlsx', sheetname='amex', na_values=['n/a'])

amex.info()

#amex = amex.Sector.nunique()

print(amex.apply(lambda x: x.nunique()))

print(amex.Sector.value_counts())

ipo_by_year = amex['IPO Year'].dropna().astype(int).value_counts()

print(ipo_by_year)

print(amex['IPO Year'].value_counts())

ipo_by_year.plot(kind='bar', title='IPOs per Year')

plt.xticks(rotation=45)
plt.show()
plt.close()

#companies by sector on all exchanges
listings = []
xls = pd.ExcelFile('listings.xlsx')
exchanges = xls.sheet_names

for exchange in exchanges:
    listing = pd.read_excel(xls, exchange, na_values='n/a')
    listing['exchange']=exchange
    listings.append(listing)
listings = pd.concat(listings)

# Iterate over exchanges then plot and show result
for exchange in exchanges:
    sectors = listings[listings['exchange']==exchange].Sector.value_counts()
    # Sort in descending order and plot
    sectors.sort_values(ascending=False).plot(kind='bar')
    # Show the plot
    plt.show()


#Technology IPOs by year on all exchanges
listing_data = pd.DataFrame.copy(listings)
# Select tech companies
tech_companies = listing_data[listing_data.Sector == 'Technology']

# Create ipo_years
ipo_years = tech_companies['IPO Year']

# Drop missing values and convert to int
ipo_years = ipo_years.dropna().astype(int)

# Count values, sort by year, and create a bar plot
ipo_years.value_counts().plot(kind='bar', title='Tech IPOs by Year')