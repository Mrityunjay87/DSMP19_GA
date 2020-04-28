# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:09:32 2020

@author: Mrityunjay1.Pandey
"""
path='./Hypo.csv'

import pandas as pd
from statsmodels.stats.weightstats import ztest
data=pd.read_csv(path)

# =============================================================================
# z_statistic, p_value = ztest(df.SalePrice,value=175000)
# print("Z-statistics = ",z_statistic)
# print("p-value for 2 tailed = ",p_value)
# 
# 
# z_statistic, p_value = ztest(df.SalePrice,value=175000,alternative='larger')
# print("Z-statistics = ",z_statistic)
# print("p-value 1 tailed larger = ",p_value)
# 
# z_statistic, p_value = ztest(df.SalePrice,value=175000,alternative='smaller')
# print("Z-statistics = ",z_statistic)
# print("p-value 1 tailed smaller = ",p_value)
# =============================================================================

z_statistic, p_value = ztest(data['Lot.Area'],value=1200,alternative='smaller')
print("Z-statistics = ",z_statistic)
print("p-value for 2 tailed = ",p_value)

if p_value<0.05:
    inference='Reject'
else:
    inference='Accept'

print("With the calculation above you can {} null hypothisis".format(inference))