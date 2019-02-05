# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 11:21:42 2019

@author: Manish Jagnani
"""

import pandas as pd
import matplotlib.pyplot as plt 
from pandas.plotting import scatter_matrix

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
train_data_x = train_data.iloc[0:,0].values
train_y = train_data.iloc[0:,1].values
test_data_x = test_data.iloc[0:, 0].values
test_y = test_data.iloc[0:, 1].values

train_data.hist()
plt.show()

test_data.hist()
plt.show()

train_data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
plt.show()

test_data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
plt.show()

scatter_matrix(train_data)
plt.show()

scatter_matrix(test_data)
plt.show()