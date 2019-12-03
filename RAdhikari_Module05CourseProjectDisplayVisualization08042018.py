# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 12:40:53 2018

@author: rajan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


PATH  = "C:\\Users\\rajan\\Desktop\\Rasmussen\\Summer_Term1\\QMB4400_DA_Optimization\\Module05\\Mod05CourseProject\\"
FILE = 'noshowappointments.csv'



df= pd.read_csv(PATH + FILE ,encoding = 'ISO-8859-1')
#df['PatientId'] = df['PatientId'].map('{:.0f}'.format)


New_Df = df[ ["Neighbourhood", "No-show"] ]

No_Show_Yes = df["No-show"].isin( ["Yes"] )

dfNew = df[ No_Show_Yes ].groupby( ["Neighbourhood"]).size()

dfNew.rename(columns ={'Index': 'Neighbourhood', '0' : 'Count'}, inplace=True)

dfNew.to_csv('NewDataset.csv')

df1=pd.read_csv('NewDataset.csv')

df1.columns= ['Neighbourhood', 'Count_Yes']

index = np.arange( df1.shape[0] )
count = df1.loc[:,"Count_Yes"].values
names = df1.loc[:,"Neighbourhood"].values


plt.figure(figsize=(20,10))
plt.bar( index, count )
plt.xticks( index, names, rotation="vertical" )
plt.title('Neighbourhood with No Show = YES')
plt.ylabel('Count_Yes')
plt.xlabel('Neighborhood Name')
plt.tight_layout()
plt.margins(0.1)
plt.show()

'''
plt.figure(figsize=(10,20))
plt.barh( index, count )
plt.yticks( index, names )
plt.title('Neighborhood No Show')
plt.xlabel('Neighbourhood_Name')
plt.ylabel('No_Show_Yes_count ')
plt.tight_layout()
plt.margins(0.1)
plt.show()

plt.figure(figsize=(25,10))
#print( type( names ))
#print( names )
#print( df1 )
df1["Names"] = names.tolist()
#print( df )
df1.set_index("Names",drop=True,inplace=True)
#print( df1 )
df1.loc[:,"Count_Yes"].plot(kind="bar")
plt.show()
'''