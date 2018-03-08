# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:05:27 2017

@author: James
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

nasdaq = pd.read_excel('listings.xlsx', sheetname='nasdaq', na_values='n/a')

nasdaq['market_cap_m'] = nasdaq['Market Capitalization'].div(1e6)

nasdaq = nasdaq[nasdaq.market_cap_m > 0] #active companies only

outliers = nasdaq.market_cap_m.quantile(0.9) #outlier threshold

nasdaq = nasdaq[nasdaq.market_cap_m < outliers] # Remove outliers

#box plot
sns.boxplot(x='Sector', y='market_cap_m', data=nasdaq)

plt.xticks(rotation=75)
plt.show()
plt.close()

#swarmplot
sns.swarmplot(x='Sector', y='market_cap_m', data=nasdaq)

plt.xticks(rotation=75)
plt.show()
plt.close()