# -*- coding: utf-8 -*-
"""
Created on Sun May 27 13:19:49 2018

@author: rajan
"""
import pandas as pd
originaFile = "SharkAttack.csv"
newFile = "Mod03CourseProject.csv"
df=pd.read_csv(originaFile, sep="\t or ,")
df.drop_duplicates(subset=None, inplace=True)
df.to_csv(newFile)

