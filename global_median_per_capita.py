# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:02:30 2017

@author: James
"""

#need to figure out hour to download form world bank income trend
#for 189 countries since year 2000

# Inspect the data
income_trend.info()

# Create barplot
sns.barplot(x='Year', y='Income per Capita', data=income_trend)

# Rotate xticks
plt.xticks(rotation=45)

# Show the plot
plt.show()

# Close the plot
plt.close()

# Create second barplot
sns.barplot(x='Year', y='Income per Capita', data=income_trend, estimator=np.median)

# Rotate xticks
plt.xticks(rotation=45)

# Show the plot
plt.show()