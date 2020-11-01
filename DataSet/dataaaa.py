# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:22:46 2020

@author: 9810_
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

common = pd.read_csv("Common_data.csv")
data = pd.read_csv("Fat_Supply_Quantity_Data.csv")


for x in range(len(data.columns)) :
    
 plt.subplot(4,6,x+1)
 #plt.figure(figsize=(1,1))
 plt.scatter(data.iloc[:,x], common.loc[:,'Deaths'])
 plt.xlabel(data.columns[x])
 
 
#plt.figure(figsize=(1000,1000))
plt.tight_layout()
plt.show()