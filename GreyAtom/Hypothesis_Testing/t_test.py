# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 23:14:01 2020

@author: Mrityunjay1.Pandey
"""

path='./Hypo.csv'

import pandas as pd
import scipy

data=pd.read_csv(path)

family=data[data['Sale.Condition']=='Family'].SalePrice
alloca=data[data['Sale.Condition']=='Alloca'].SalePrice

t_stat, p_value = scipy.stats.mstats.ttest_ind(family,alloca)

print("T Stastics is {} and p value is {} ".format(t_stat,p_value))

if p_value<0.05:
    inference='Reject'
else:
    inference='Accept'

print("With the calculation above you can {} null hypothisis".format(inference))