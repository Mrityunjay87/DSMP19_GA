# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 09:32:30 2020

@author: Mrityunjay1.Pandey
"""

path='C:/Users/mrityunjay1.pandey/GreyAtom/Day5/KAG_conversion_data.csv'
import numpy as np
import csv
with open(path) as f:
    adm = csv.reader(f,delimiter=',')
    adm = list(adm)

# Remove the header
adm.remove(adm[0])

# Convert the data into a numpy array and store it in sales_data
sales_data=np.array(adm)

#How many unique ad campaigns (xyz_campaign_id) does this data contain ?
#And for how many times was each campaign run ?
print("This Data contains {} unique ad campaigns.{} ".format(len(np.unique(sales_data[:,1],return_counts=True))))

for i in np.unique(sales_data[:,1]):
    if 
