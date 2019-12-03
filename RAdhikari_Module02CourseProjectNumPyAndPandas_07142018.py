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
# Getting only those records which has No-show = No

F6 =df.loc[df['No-show'] == 'Yes', 'PatientId':'No-show'] 
# Getting only those records which has No-show = Yes

No_Show_Count=df.groupby(["No-show"]).size() 
# Creating No-show dataframe

df['PatientId'] = df['PatientId'].map('{:.0f}'.format)
# Determining PatientId in the dataset.

Neighborhood_Count=F6.groupby(["Neighbourhood"]).size() 
# Creating Neighborhood dataframe with only No-show = Yes 

# Saving Outputs to .csv
F5.to_csv('No-Show-No.csv')
F6.to_csv('No-show-Yes.csv')
No_Show_Count.to_csv('No_Show_Count.csv')
Neighborhood_Count.to_csv('Neighborhood_Count-Yes.csv')
