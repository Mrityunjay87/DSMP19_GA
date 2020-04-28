# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:16:50 2020

@author: Mrityunjay1.Pandey
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path='C:/Users/mrityunjay1.pandey/GreyAtom/Report_Reco_Project/report_reco.csv'
# Code starts here
#Reading File
df=pd.read_csv(path)
#Converting states in Lower Case
df.state=df.state.str.lower()
#New column creation for storing total amount
df['total']=df['Jan']+df['Feb']+df['Mar']
#Storing sum of amount of all users in the Month of Jan,Feb & March
sum_row=df.Jan.sum()+df.Feb.sum()+df.Mar.sum()
Grand_Total=df.total.sum()
#Adding Months sum in new row
sumtot=df.iloc[:,-4:].sum(axis=0)
df_final=df.append([{'Jan':sumtot[0],'Feb':sumtot[1],'Mar':sumtot[2],'total':sumtot[3]}],ignore_index=True)
# Code ends here
url='https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
import requests as req
response=req.get(url)