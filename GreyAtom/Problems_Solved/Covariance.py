# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:23:09 2020

@author: Mrityunjay1.Pandey
"""

#Task 1 - Histogram
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path='C:\\Users\\mrityunjay1.pandey\\GreyAtom\\houseprices.csv'
# Code starts here
df=pd.read_csv(path)
plt.hist(df.SalePrice,bins=10)
plt.show()
# Code ends here

#Task 2 - Scatter plot
import matplotlib.pyplot as plt

# Code starts here
plt.scatter(df.SalePrice,df.GarageArea)
plt.xlabel("Sale Price")
plt.ylabel("Garage Area")
plt.show()
# Code ends here

#Task 3 - Plot the pie chart for number of GarageCars for all the houses in the dataset
import matplotlib.pyplot as plt
# Code starts here
garage=df.GarageCars.value_counts()
plt.pie(garage,textprops=dict(color="w"))
#plt.setp(autotexts, size=8, weight="bold")
plt.show()
# Code ends here

#Task 4 - Calculate arithmetic mean, median, mode for SalePrice and plot the same on the histogram
# Code starts here
mean=df.SalePrice.mean()
mode=df.SalePrice.mode()
median=df.SalePrice.median()

plt.hist(df.SalePrice,bins=40)
plt.plot([mode]*300, range(300), label='mode')
plt.plot([median]*300, range(300), label='median')
plt.plot([mean]*300, range(300), label='mean')
plt.show()
# Code ends here

#Task 5 - Calculate the range of SalePrice
# Code starts here

df.SalePrice
maximum=df.SalePrice.max()
minimum=df.SalePrice.min()
range_saleprice=maximum-minimum
print("Range of the Sales Price is {}".format(range_saleprice))
# Code ends here

#Task 6 - Calculate the MAD for SalePrice
# Code starts here

mean=df.SalePrice.mean()
distance=df.SalePrice-mean
mad=sum(abs(distance))/len(distance)
# Code ends here

#Task 7 - Calculate the Standard Deviation for SalePrice
# Code starts here
mean=df.SalePrice.mean()
sq_distance=(df.SalePrice-mean)**2
sd=np.sqrt(sum(sq_distance)/len(sq_distance))
print("Standard Deviation is {}".format(sd))

# Code ends here

#Task 8 - Calculate CV for GarageArea and LotArea and compare the same
# code starts here
#Calculating Mean of Garage Column
garage_mean=df.GarageArea.mean()
#Standarad Deviation of Garage Column
garage_std=df.GarageArea.std()
#Calculating Coefficient of Variation
garage_cv = (garage_std/garage_mean)*100
print("Coefficient of variation for Garage is {}".format(garage_cv))

#Calculating Mean of Lot Area Column
lot_mean=df.LotArea.mean()
#Calculating Standard Deviation of Lot Area Column
lot_std=df.LotArea.std()
#Calculating Coefficient of Variation
lot_cv=(lot_std/lot_mean)*100
print("Coefficient of variation for Lot Area is {}".format(lot_cv))


# Code ends here

#Task 9 -  Inter - Quartile Range (IQR)
# Code starts here
q1,q3=df.SalePrice.quantile([0.25,0.75])
iqr=q3-q1

print("IQR is :",iqr)

# Code ends here

#Task 10 - box plot
# Code starts here

df.boxplot(column="SalePrice")
# Code ends here

#Create a new dataframe with columns LotArea and SalePrice with the first 20 observations 
new=df[['LotArea','SalePrice']].head(20)
#Calculate the mean for LotArea and SalePrice
mean_lotarea=new.LotArea.mean()
mean_saleprice=new.SalePrice.mean()

#Calculate the difference between each observation and mean for LotArea and SalePrice,
diff_lotarea = new.LotArea-mean_lotarea
diff_saleprice = new.SalePrice-mean_saleprice

#Multiply diff_lotarea and diff_saleprice and calculate the sum, 
#store the value in variable summation
summation=(diff_lotarea*diff_saleprice).sum()

#Calculate covariance by dividing summation by the number of observation pairs,
# store the same in variable covariance and print the same.
covariance=summation/len(new)
print("Covariance is:",covariance)


plt.hist(df.GarageArea,bins=30)
#Plot a histogram for GarageArea and identify whether the data is skewed
import seaborn as sns
# Density Plot and Histogram of Garage Area
sns.distplot(df.GarageArea, hist=True, kde=True, 
             bins=20, color = 'darkblue', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})

#*********Pearson's Correlation Coefficient*********
#Calculate the covariance between two variables by using cov()
newdf = df[['LotArea','SalePrice']].copy()
covariance=newdf.cov().iloc[0][1]

#alculate the standard deviation of LotArea and SalePrice 
std_LotArea = newdf.LotArea.std()
std_SalePrice = newdf.SalePrice.std()

pearson =round(covariance/(std_LotArea*std_SalePrice),4)

print("Pearson coefficient is {}".format(pearson))

#*********Spearman Rank Correlation Coefficient*********

#calculating rank of all observations
newdf['d1'],newdf['d2']=newdf['LotArea'].rank(axis=0,method='min'),newdf['SalePrice'].rank(axis=0,method='min')
#Squared value of the difference between the ranks calculated above
newdf['d^2']=(newdf.d1-newdf.d2)**2
#Sum of d^2
d_square=newdf['d^2'].sum()

spearman = round(1-((6*d_square)/(len(newdf)*((len(newdf)**2)-1))),4)

print("Pearson coefficient is {} & Spearmans coefficient is {}".format(pearson,spearman))
