# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 23:46:25 2017

@author: James
"""
from pandas_datareader.data import DataReader
from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

ty10 = DataReader('DGS10', 'fred', date(1962, 1, 1))

ty10.dropna(inplace=True)

ty10.plot(title='10-year Treasury')
plt.tight_layout()
plt.show()

#using seaborn with Kernal Desnsity Estimate

sns.distplot(ty10)

ax = sns.distplot(ty10)

ax.axvline(ty10['DGS10'].median(), color = 'blue', ls='-.')

plt.close()
#visualizing international income distributions
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
# Print the summary statistics for income
print(income.describe())

# Plot a rugplot
sns.distplot(income['Income per Capita'], bins=50, kde=False, rug=True)

# Show the plot
plt.show()
plt.close()
# Plot a basic histogram of income per capita
sns.distplot(income['Income per Capita'])

# Show the plot
plt.show()
plt.close()

#Growth rates in Brazil, China and the US
# Load the file into growth
growth = pd.read_csv('income_growth.csv', parse_dates=['DATE']).set_index('DATE')

# Inspect the summary statistics for the growth rates
growth.describe()

# Iterate over the three columns
for column in growth.columns:
    sns.distplot(growth[column], hist=False, label=column)
    
# Show the plot
#spyder is cropping my plot.  work around is to set the ylim on plt
plt.ylim(0,25)
plt.show()
plt.close()

#Highligting values in the distribution
# Create inc_per_capita
inc_per_capita = income['Income per Capita']

# Filter out incomes above the 95th percentile
inc_per_capita = inc_per_capita[inc_per_capita< inc_per_capita.quantile(0.95)]

# Plot histogram and assign to ax
ax = sns.distplot(inc_per_capita)

# Highlight mean
ax.axvline(inc_per_capita.mean(), color='b')

# Highlight median
ax.axvline(inc_per_capita.median(), color='g')

# Show the plot
plt.show()
plt.close()