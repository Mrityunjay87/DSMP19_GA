# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:10:17 2020

@author: Mrityunjay1.Pandey
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 09:42:43 2020

@author: Mrityunjay1.Pandey
"""
import pandas as pd

#Function Defination
test1="sample text"
def splitword(data):
    temp={}
    data.lower()
    split_data=data.split()
    for i in range(0,len(split_data)):
        temp.update({split_data[i]:len(split_data[i])})
        output=pd.DataFrame(temp.items(),columns=['word','count'])
    return output

#Call to Function
test=splitword(test1)
#Converting into dataframe



#Longest even word length
data1 = 'One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'
data2 = 'photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading.'
data3 = 'testing very9 important'

test=splitword(data1)

def q01_longest_even_word(sentence):
    test=splitword(sentence)
    if (test['count']%2==0).any():
        output=test.word[test[test['count']%2==0]['count'].idxmax()]
    else:
        output=0
    return output
    

#Question 3
import numpy as np
import math
   
def q01_get_minimum_unique_square(x,y):
        #Counter for output increment
        count=0
        #Arranging input paramters of function for the list
        num=np.arange(x,y+1)
        #Looping through till length of variable
        for i in num:
            #Condition check for squareroot if difference is 0
            if (np.sqrt(i) - math.floor(np.sqrt(i))==0):
                count+=1
        return count
 
print("There are total of {} perfect square numbers".format(q01_get_minimum_unique_square(4,10)))

def palindrome(num):
    #Incrementing to find next from given input
    num=str(num+1)
    #Looping untill True
    while True:
        if (num==num[::-1]):
            num=int(num)
            break
        else:
            num=str(int(num)+1)
    return num


print(palindrome(1331))

#Method 1
def a_scramble(str_1, str_2):
    mod_str_1=list((str_1.replace(" ", "").lower()))
    mod_str_2=list(str_2.lower())
    return all(item in mod_str_1 for item in mod_str_2 )

#Method2
def a_scramble(str_1, str_2):
    mod_str_1=list((str_1.replace(" ", "").lower()))
    mod_str_2=list(str_2.lower())
    return (set(mod_str_2).issubset(set(mod_str_1)))

#Method 3
def a_scramble(str_1, str_2):
    mod_str_1=set((str_1.replace(" ", "").lower()))
    mod_str_2=set(str_2.lower())
    return (mod_str_2.issubset(mod_str_1))  
