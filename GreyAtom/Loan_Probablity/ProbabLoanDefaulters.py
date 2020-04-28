# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:15:15 2020

@author: Mrityunjay1.Pandey
"""
path='./ProbabLoanDefaulters.csv'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(path)
#probability p(A),in variable p_a ,for the event that fico credit score is greater than 700.
p_a=len(df[df.fico>700])/len(df)

#probabilityp(B) for the event that purpose == 'debt_consolidation'
p_b=len(df[df.purpose== 'debt_consolidation'])/len(df)

#Calculate the purpose == 'debt_consolidation' and store it in dataframe df1.
df1=df[df.purpose== 'debt_consolidation']

#Calculate the probablityp(B|A) for the event purpose == 'debt_consolidation' given 
#'fico' credit score is greater than 700 and store it in variable p_a_b.

p_a_b=(len(df1[df1.fico>700])/len(df1))/p_a

#check the independency p_a_b==p_a:

result=p_a_b==p_a
print("Dependency Check result is:",result)

#probability p(A) for the event that paid.back.loan == Yes
prob_lp=len(df[df['paid.back.loan']=='Yes'])/len(df)

# probability p(B) for the event that credit.policy == Yes
prob_cs=len(df[df['credit.policy']=='Yes'])/len(df)

#Taking DataFrame where ['paid.back.loan'] == 'Yes'

new_df=df[df['paid.back.loan'] == 'Yes']

#probablityp(B|A) for the event paid.back.loan == 'Yes' given credit.policy == 'Yes'
prob_pd_cs=len(new_df[new_df['credit.policy'] == 'Yes'])/len(new_df)

#Calculating conditional probability 

bayes=(prob_pd_cs*prob_lp)/prob_cs

print("Bayes Value is:",bayes)

#Visualize the bar plot for the feature purpose
df.purpose.value_counts().plot(kind='bar')
#Creating new data frame with paid back loan as No
df1=df[df['paid.back.loan'] == 'No']

#Visualize the bar plot for the feature purpose of df1
df1.purpose.value_counts().plot(kind='bar')
plt.show()


# median for installment
inst_median=df.installment.median()

# mean for installment
inst_mean=df.installment.mean()

#histogram for installment
plt.hist(df.installment)
plt.axvline(inst_mean, color='k', linestyle='dashed', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(inst_mean*1.1,max_ylim*0.9,'Mean: {:.2f}'.format(inst_mean))
plt.axvline(inst_median, color='k', linestyle='dashed', linewidth=1)
plt.text(inst_median*0.7,max_ylim*0.7,'\nMedian: {:.2f}'.format(inst_median))
plt.show()

#histogram for log annual income
plt.hist(df['log.annual.inc'])
plt.show()