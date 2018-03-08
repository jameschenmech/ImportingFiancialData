# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:12:38 2017

@author: James
"""

import pandas as pd

amex = pd.read_csv('amex-listings.csv', na_values='n/a', parse_dates=['Last Update'])

amex.info()

print(amex.head())

#mulitiple sheets import form Excel
listings = pd.read_excel('listings.xlsx', sheetname=['amex', 'nasdaq'],
                         na_values='n/a')

listings['nasdaq'].info()
type(listings) #listing is a dict with key:DataFrame

xls = pd.ExcelFile('listings.xlsx') # pd.ExcelFile object
exchange = xls.sheet_names #exhcange contails the sheet names

nyse = pd.read_excel(xls, sheetname=exchange[2], na_values='n/a')
all_data = pd.read_excel(xls, sheetname=exchange, na_values='n/a') #all data is a list
all_data_df = pd.concat(all_data) #create a DataFrame out of a list

#concatenate two data frames
#add a reference column to each index first (aka broadcasting)
amex['Exchange'] = 'AMEX'
nyse['Exchange'] = 'NYSE'
listings2 = pd.concat([amex,nyse])
print(listings2.head())

#combining three data frames
exchanges = xls.sheet_names

listings3 = [] #empty list

for exchange in exchanges:
    listing = pd.read_excel(xls, sheetname=exchange)
    listing['Exchange'] = exchange
    listings3.append(listing) #Add DataFrame to list
combined_listings = pd.concat(listings3) #create a DataFrame out of list
