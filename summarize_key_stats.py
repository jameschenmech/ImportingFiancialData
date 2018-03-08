# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:16:34 2017

@author: James
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xls = pd.ExcelFile('listings.xlsx')

exchanges = xls.sheet_names

listings = []

for exchange in exchanges:
    listing = pd.read_excel(xls, sheetname=exchange, na_values='n/a')
    listings.append(listing)
listings = pd.concat(listings)    

nasdaq = pd.read_excel(xls, sheetname='nasdaq', na_values='n/a')

market_cap = nasdaq['Market Capitalization'].div(1e6)

print(market_cap.mean())

print(market_cap.median())

print(market_cap.mode())

print(market_cap.var())

print(market_cap.std())

#list the poorest and richest countries worldwide
# Import the data
income = pd.read_csv('per_capita_income.csv')

# Inspect the result
income.info()

# Sort the data by income
income = income.sort_values('Income per Capita', ascending=False)

# Display the first and last five rows
print(income.head())
print(income.tail())

# Calculate the mean
print(income['Income per Capita'].mean())

# Calculate the median
print(income['Income per Capita'].median())

# Create the new column
income['Income per Capita (,000)'] = income['Income per Capita']//(1000)

# Calculate the mode of the new column using // for floor division
#floor division rounds down to whole numbers
income['Income per Capita (,000)'].mode()//(1000)

#distribution of data with quantiles
median = market_cap.quantile(0.5)

median == market_cap.median()

market_cap.describe(percentiles = np.arange(0.1, 0.91, 0.1))

#Global incomes: Dispersion
# Calculate mean
mean = income['Income per Capita'].mean()

# Calculate standard deviation
std = income['Income per Capita'].std()

# Calculate and print lower and upper bounds
bounds = [mean-std, std+mean]
print(bounds)

# Calculate and print first and third quartiles
quantiles = income['Income per Capita'].quantile([0.25, 0.75])
print(quantiles)

# Calculate and print IQR
iqr = quantiles[0.75] - quantiles[0.25]
print(iqr)

#deciles of the global income distribution
# Generate range of deciles
quantiles = np.arange(0.1,0.91,0.1)

# Print them
print(quantiles)

# Calculate deciles for 'Income per Capita'
deciles = income['Income per Capita'].quantile(quantiles)

# Print them
print(deciles)

# Plot deciles as a bar chart
deciles.plot(kind='bar', title='Global Income per Capita - Deciles')

# Make sure to use the tight layout!
plt.tight_layout()

# Show the plot
plt.show()