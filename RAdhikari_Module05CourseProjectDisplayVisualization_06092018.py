# -*- coding: utf-8 -*-
"""
Created on Sat Jun 09 16:46:12 2018

@author: rajan
"""

import pandas as pd ## importing pandas library
import matplotlib.pyplot as plt


SharkAttack3=pd.read_csv('NewSharkAttack.csv')

plt.plot(SharkAttack3)

plt.title('Shark Attack', fontsize =12)
plt.ylabel('Number of Attacks', fontsize =12)
plt.xlabel('Name of Countires', fontsize =12)
plt.figure(figsize=(15, 5))




# For the Barchart
#SharkAttack3.plot('Country','Case Number', kind='bar', figsize=(50,5))

# For the Line Chart
#SharkAttack3.plot('Country','Case Number', kind='line', figsize=(15,5))

# For the Pie Chart
#SharkAttack3.plot('Country','Case Number',  kind='pie', figsize=(5,5))