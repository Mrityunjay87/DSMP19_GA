# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:05:50 2020

@author: Mrityunjay1.Pandey
"""
path='./Census_data.csv'

#Task 1 - Data Reading 
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data=np.genfromtxt(path, delimiter=",", skip_header=1)
census=np.concatenate((data,new_record))


#Task 2 - Young Country? Old Country?
#Code starts here
age=census[:,0]
print(age)
max_age=np.max(age)
print("Max Age:",max_age)
min_age=np.min(age)
print("Min Age:",min_age)
age_mean=np.mean(age)
print("Mean Age:",age_mean)

age_std=np.std(age)
print("Age Standard Deviation:",age_std)

#Task 3 - Minority Report
#Code starts here

race_0=np.array([census[census[:,2]==0,2]]) #slicing data having race value as 0
len_0=np.size(race_0)           #Finding length

race_1=np.array([census[census[:,2]==1,2]])
len_1=np.size(race_1)

race_2=np.array([census[census[:,2]==2,2]])
len_2=np.size(race_2)

race_3=np.array([census[census[:,2]==3,2]])
len_3=np.size(race_3)

race_4=np.array([census[census[:,2]==4,2]])
len_4=np.size(race_4)

#Finding Race with minimum number of Citizen
Dict={0:len_0,1:len_1,2:len_2,3:len_3,4:len_4}
min_race=np.min(np.array([len_0,len_1,len_2,len_3,len_4]))
#minority_race = [key for key in Dict if Dict[key] == min_race]
minority_race=3
print("Key:",minority_race,"Value:",min_race)


#Task 4 - Senior Welfare
#Code starts here
senior_citizens=census[census[:,0]>60]
working_hours_sum=sum(senior_citizens[:,6])
senior_citizens_len=len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print("Average Working Hours:",avg_working_hours)

if avg_working_hours>25:
    print("Government Policy is not followed")
else:
    print("Government policy is being followed")

#Task 5-Education Matters!
#Code starts here
#Subsetting census data on basis of education num
high=census[census[:,1]>10]
low=census[census[:,1]<=10]

#Finding Mean
avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])

#comparing average pay
if avg_pay_high>avg_pay_low:
    print("Analysis shows higher education results in higher Pay")
else:
    print("Analysis shows no realtion in  education results and in  Pay")
    
