# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:44:24 2020

@author: Mrityunjay1.Pandey
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
import random
warnings.filterwarnings("ignore")

electors_2009 = pd.read_csv("C:/Users/mrityunjay1.pandey/GreyAtom/Day6/LS2009Electors.csv")
candidate_2009 = pd.read_csv("C:/Users/mrityunjay1.pandey/GreyAtom/Day6/candidate09.csv")

#Sorting the pivot to get list of values
ts=candidate_2009.pivot_table(index='Party_Abbreviation').Total_Votes_Polled.sort_values(ascending=False)
#Assessing index and values of the series for converting to list
P_AB=ts.index.tolist()
P_Pol=ts.values.tolist()

#Converting list to array and splitting into multiple arrays.
arr_P_AB=np.array(P_AB)
arr_P_Pol=np.array(P_Pol)
split_arr_P_AB=np.split(arr_P_AB,33) #Spliiting the complete data set in 33 arrays of 11 values each
split_arr_P_Pol=np.split(arr_P_Pol,33) #Spliiting the complete data set in 33 arrays of 11 values each

#Creating a layout to plot figures
fig,a=plt.subplots(17,2)
fig.set_figheight(20)
fig.set_figwidth(15)
fig.tight_layout(pad=3)
k=0
for i in range(0,17):
    for j in [0,1]:
        if k<33:
            r = lambda: random.randint(0,255)
            a[i][j].bar(split_arr_P_AB[k],split_arr_P_Pol[k],color=('#%02X%02X%02X' % (r(),r(),r())))
            a[i][j].title.set_text('Vote Share having greater than {}'.format(split_arr_P_Pol[k][10]))
            k=k+1

plt.savefig('test.pdf')
