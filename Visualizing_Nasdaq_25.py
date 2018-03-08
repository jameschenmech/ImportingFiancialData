# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:33:39 2017

@author: James
"""

import pandas as pd
from pandas_datareader.data import DataReader
from datetime import date #Date & time functionality
import matplotlib.pyplot as plt

unstacked = pd.read_csv('nasdaq_25.csv')

#Need to be able to plot this correctly
unstacked.plot(subplots=True)

plt.tight_layout()
plt.show()

#unstacked.plot(subplots=True)
#
#plt.tight_layout()
#plt.show()

