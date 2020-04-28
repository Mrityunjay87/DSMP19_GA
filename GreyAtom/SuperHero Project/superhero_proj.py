# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:22:12 2020

@author: Mrityunjay1.Pandey
"""

import statistics
#from matplotlib import cm as cm

path='C:/Users/mrityunjay1.pandey/GreyAtom/SuperHero Project/superhero.csv'

#Task 1 - Data loading
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)
#Replacing '-' in Gender Column
data.Gender.replace('-','Agender',inplace=True)
#Getting Value counts in Gender of data
gender_count=data.Gender.value_counts()
#Plotting bar chart
plt.bar(gender_count.index,gender_count.values)
#Setting Title
plt.title("Superheros Distrubtion according to Gender",fontsize=23)
#Setting x & y label
plt.xlabel("Gender",fontsize=23)
plt.ylabel("Count",fontsize=23)
plt.show()
#Code starts here 



#Task 2 - Heroes Alignment
#Code starts here
alignment=data.Alignment.value_counts()
#Plotting Pie chart 
plt.pie(alignment,labels=alignment.index,autopct="%1.1f%%",shadow=True, startangle=0)
#Setting plot title
plt.title("Character Alignment")
plt.show()

#With the plot it is eveident there would not be any difference even if the 'neutral' would have taken one side

#Task 3 - Combat Correlation

#Data slicing for 2 columns, strength and Combat
sc_df=data[['Strength','Combat']]

#Finding Co-variance between strength and Combat.
sc_covariance=np.cov(sc_df.Strength,sc_df.Combat)[0][1]

#standard deviation of column Strength 
sc_strength=round(statistics.stdev(sc_df.Strength),2)

#Standard deviation of column Combat
sc_combat=round(statistics.stdev(sc_df.Combat),2)

#he pearson's correlation coefficient between Strength & Combat
sc_pearson=sc_covariance/(sc_strength*sc_combat)

#Data slicing for 2 columns, Intelligence and Combat
ic_df=data[['Intelligence','Combat']]

#Finding Co-variance between Intelligence and Combat.
ic_covariance=np.cov(ic_df.Intelligence,ic_df.Combat)[0][1]

#standard deviation of column Intelligence 
ic_intelligence=round(statistics.stdev(ic_df.Intelligence),2)

#Standard deviation of column Combat
ic_combat=round(statistics.stdev(ic_df.Combat),2)

#he pearson's correlation coefficient between Strength & Combat
ic_pearson=ic_covariance/(ic_intelligence*ic_combat)

#Task3
#Getting value of quantile=0.99
total_high=np.quantile(data.Total,0.99)
#Subseting the dataframe 'data' based on column Total's value greater than 'total_high'
super_best=data[data.Total>total_high]
#Createing a list of the names from 'Name' associated with 'super_best' dataframe 
super_best_names=super_best.Name.to_list()
#Printing the list to see the top superheroes/villains
print("Top superheroes/villains are \n",super_best_names)

#Task4
fig,(ax_1,ax_2,ax_3)=plt.subplots(nrows=1,ncols=3,tight_layout=True)

# =============================================================================
# import seaborn as sns
# 
# sns.boxplot(x=data.Intelligence,ax=ax_1,orient='v')
# sns.boxplot(x=data.Speed,ax=ax_2,orient='v')
# sns.boxplot(x=data.Power,ax=ax_3,orient='v')
# =============================================================================
ax_1.boxplot(x=data.Intelligence)
ax_1.set_title('Intelligence')
ax_2.boxplot(x=data.Speed)
ax_2.set_title('Speed')
ax_3.boxplot(x=data.Power)
ax_3.set_title('Power')
plt.show()


