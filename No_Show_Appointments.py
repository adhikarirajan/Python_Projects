import pandas as pd
import numpy as np

df =pd.read_csv ('noshowappointments.csv') 
# Reading dataset with Pandas

MapCols= df.applymap(type) 
# identifying a pandas column in a list using applymap function 

print(df.iloc[:,0]) 
# Printing 1st Column data which is PatientID

print( df['No-show'].value_counts() ) # counting the No-show vlues

print( df.groupby(['No-show']).size() )

#df.set_index('PatientId', inplace=True)

F5 =df.loc[df['No-show'] == 'No', 'PatientId':'No-show'] 

print( F5.groupby(['No-show']).size() )
# Getting only those records which has No-show = No

F6 =df.loc[df['No-show'] == 'Yes', 'PatientId':'No-show'] 
# Getting only those records which has No-show = Yes

No_Show_Count=df.groupby(["Neighbourhood", "No-show"]).size() 

No_Show_Yes = df["No-show"].isin( ["Yes"] )

dfNew = df[ No_Show_Yes ].groupby( ["Neighbourhood","No-show"]).size()

F7 =df.loc[df['No-show'] == 'Yes', 'Neighbourhood':'No-show']
# Creating No-show dataframe

F7.to_csv('Neighbourhood_No_show_Yes.csv')

Nhood_No_Show_Count_Yes=F7.groupby(["No-show"]).size() 
PtID_No_Show_Count=F6.groupby([ "No-show"]).size() 

#df['PatientId'] = df['PatientId'].map('{:.0f}'.format)
#print( df )