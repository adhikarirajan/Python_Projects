# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 22:57:20 2018

@author: rajan
"""

import pandas as pd
import numpy as np
import numpy.ma as ma
import sqlite3 as sqllite
import sys

PATH  = "C:\\Users\\rajan\\Desktop\\Rasmussen\\Summer_Term1\\QMB4400_DA_Optimization\\Module04\\CourseProject04\\"
FILE = 'noshowappointments.csv'

SQLDB = "QMB4400Project04.db"
Table1 = 'Neighbourhood_No_Shows_Yes'
Table2 = 'PatientId_No_Shows_Yes'


df= pd.read_csv(PATH + FILE ,encoding = 'ISO-8859-1')
df['PatientId'] = df['PatientId'].map('{:.0f}'.format)

connection = sqllite.connect(PATH + SQLDB)
print("Database created successfully.")


No_Show_Yes = df["No-show"].isin( ["Yes"] )

dfNew = df[ No_Show_Yes ].groupby( ["Neighbourhood"]).size()

df_PtID = df[ No_Show_Yes ].groupby( ["PatientId"]).size()


with connection:
    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS Neighbourhood_No_Shows_Yes")
    cur.execute("CREATE TABLE Neighbourhood_No_Shows_Yes(Neighbourhood TEXT, Count_Yes INT)") 
    
    cur.execute("DROP TABLE IF EXISTS PatientID_No_Shows_Yes")
    cur.execute("CREATE TABLE PatientId_No_Shows_Yes(PatientId INT, Count_Yes INT)") 
    
   
with connection:
    cur = connection.cursor()
    cur.execute("select name from sqlite_master")
    table_names = cur.fetchall()
    
#Reading No Show = Yes Data from the database which is grouped by Neighbourhood
with connection:
    for i in dfNew.index.tolist():
        x= dfNew[i]
        print(i, x)
        TBL_STRING = "INSERT INTO " + Table1 +" VALUES ("
        TBL_STRING = TBL_STRING + "'" + str(i) + "'" + "," + str(x) 
        TBL_STRING = TBL_STRING + ")"
        cur.execute(TBL_STRING)

with connection:
    cur = connection.cursor()
    cur.execute("Select * from " + Table1)
    rows =cur.fetchmany(100)
    print ("-------------------------------------")
    print ("Here is the Neighbourhood Data")
    print ("-------------------------------------")
    for row in rows:
        print(type(row), row)

#Reading No Show = Yes Data from the database which is grouped by Patient ID
with connection:
    for j in df_PtID.index.tolist():
        y= df_PtID[j]
        print(j, y)
        TBL_STRING = "INSERT INTO " + Table2 +" VALUES ("
        TBL_STRING = TBL_STRING + "'" + str(j) + "'" + "," + str(y) 
        TBL_STRING = TBL_STRING + ")"
        cur.execute(TBL_STRING)

with connection:
    cur = connection.cursor()
    cur.execute("Select * from " + Table2)
    rows =cur.fetchmany(100)
    print ("-------------------------------------")
    print ("Here is the PatientID Data")
    print ("-------------------------------------")
    for row in rows:
        print(type(row), row)

