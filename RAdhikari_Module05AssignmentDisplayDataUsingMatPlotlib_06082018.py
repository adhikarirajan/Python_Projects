# -*- coding: utf-8 -*-
"""
Created on Fri Jun 08 19:28:18 2018

@author: rajan
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot  as plt
#%matplotlib inline

AutoMobile=pd.read_csv('Automobile_data.csv') # read the dataset

NewAuto=AutoMobile.fillna("Not-Available")
NewAuto['Car-Type']=NewAuto['Car-Type'].fillna('Not-Available')

NewAuto.loc[:, ['Car-Type']]
group_by_type=NewAuto.groupby(['Car-Type'])

print(group_by_type.size())

Car_Type = ['Not-Available', 'convertible', 'hardtop', 'hatchback', 'sedan' ,  'wagon' ]
Number_of_Cars =[32, 5, 7, 65, 78, 18]

plt.figure(figsize=(15,5))

plt.plot(Car_Type, Number_of_Cars)
plt.title('Types of Cars')
plt.ylabel('Number of Cars')
plt.xlabel('Types of Cars')
plt.legend([], loc=0)