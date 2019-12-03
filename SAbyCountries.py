# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 23:48:22 2018

@author: rajan
"""

import pandas as pd ## importing pandas library
SharkAttack=pd.read_csv('SharkAttack.csv')  # read the dataset                  
SharkAttackbyCounties=SharkAttack.groupby(['Country']).count()    
print(SharkAttackbyCounties.info)  