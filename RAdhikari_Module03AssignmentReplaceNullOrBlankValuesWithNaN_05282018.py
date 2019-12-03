# -*- coding: utf-8 -*-
"""
Created on Mon May 28 10:54:19 2018

@author: rajan
"""

import pandas as pd
import numpy as np

Economy=pd.read_csv('paytm_com-ecommerce_sample.csv') # read the dataset
Eco=Economy.replace(np.nan, 'NaN', regex=True)
Eco.to_csv('WithNaN_paytm_com-ecommerce_sample.csv')

Eco2=Economy.dropna(subset =['brand'])
Eco2.to_csv('WithoutNaN_paytm_com-ecommerce_sample.csv')