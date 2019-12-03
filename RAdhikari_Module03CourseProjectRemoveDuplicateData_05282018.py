# -*- coding: utf-8 -*-
"""
Created on Sat May27 15:38:57 2018

@author: rajan
"""
import pandas as pd ## importing pandas library
SharkAttack=pd.read_csv('SharkAttackDataSets.csv', delimiter =',', encoding ='utf-8') # read the dataset
SharkAttack.duplicated(subset=None, keep='first')
SharkAttack.drop_duplicates(subset=None, inplace=True)
SharkAttack.to_csv('NewSADatasets.csv')


SharkAttack=pd.read_csv('SharkAttack.csv', delimiter =',', encoding ='utf-8') # read the dataset
SharkAttack.duplicated(subset=None, keep='first')
SharkAttack.drop_duplicates(subset=None, inplace=True)
SharkAttack.to_csv('Module03PythonCourseProject.csv')





