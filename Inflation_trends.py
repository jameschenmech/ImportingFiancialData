# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:14:35 2017

@author: James
"""
#need to imppor inflationa data from FRED for China, India and US
# Inspect the inflation data

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

inflation.info()

# Create inflation_by_country
inflation_by_country = inflation.groupby('Country')

# Iterate over inflation_by_country and plot the inflation time series per country
for country, data in inflation_by_country:
    # Plot the data
    data.plot(title=country)
    # Show the plot
    plt.show()
    plt.close()
    
# Create boxplot
sns.boxplot(x='Country', y='Inflation', data=inflation)

# Show the plot
plt.show()

# Close the plot
plt.close()

# Create swarmplot
sns.swarmplot(x='Country', y='Inflation', data=inflation)

# Show the plot
plt.show()
plt.close()