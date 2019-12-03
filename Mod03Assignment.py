# -*- coding: utf-8 -*-
"""
Created on Sun May 27 14:38:17 2018

@author: rajan
"""
import pandas as pd
#import numpy as np

NewDf=pd.read_csv('paytm_com-ecommerce_sample.csv') # read the dataset
#NewDataFile=np.loadtxt(r'paytm_com-ecommerce_sample.csv', dtype = str, delimiter =',', skiprows =1,usecols =(1, ))
#NewDf.replace( '', "NaN") # using Pandas
#ewData=NewDataFile.replace(np.nan, 'NaN', regex=True)
#NewDataFile =NewDataFile.fillna(' ')
#NewDf.brand=NewDf.brand.fillna(' ')
#NewDf=NewDf.fillna(' ')
#NewDf.isnull().sum()
#NewDf['brand'].isnull().sum()
#NewDf=NewDf.fillna('')
#BrandNew=NewDf.dropna()

#null_columns=NewDf.columns[NewDf.isnull().any()]
#NewDf[null_columns].isnull().sum()

print(NewDf[NewDf["brand"].isnull()][null_columns])
NewDf.to_csv('NaNpaytm_com-ecommerce_sample.csv')