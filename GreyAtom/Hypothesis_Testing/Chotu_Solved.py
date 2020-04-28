# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:31:44 2020

@author: Smita.Triathi
"""

#===========Solution to Map===========

#This is function defintation for passing function and list as input then applying map on it.
def mapl(f,l):
    result=map(f, l)
    return list(result)
    

def square(i):
    return i*i


l=[4,5,3,4]
result=mapl(square,l)


#Question 1:Write a function that list as input and returns the element that repeats.

test1=['Smita','MJ','Smita']
test2=[1,2,3,4,5,6,6,2]

def find_duplicate(l):
    new_list = sorted(set(l))
    dup_list =[]
    for i in range(len(new_list)):
        if (l.count(new_list[i]) > 1 ):
            dup_list.append(new_list[i])
    return dup_list

print("The Duplicates in the list:\n{} & {} \nare : {} & {} respectively".format(test1,test2,find_duplicate(test1),find_duplicate(test2)))


from itertools import permutations 
  
# Question 2:Get all permutations of given string 
perm =list(permutations('SMITA'))

def all_possible_permutations(s):
    from itertools import permutations
    perm=permutations(s)
    for i in list(perm): 
         print(''.join(i))
         
         
#Sum of Tuple         
def n_tuple_sum(num,l):
    permutations(num,4)
    temp=list(permutations(num,4))
    temp2=[]
    for i in range(0,len(temp)):
        if sum(temp[i])==l:
            temp2.append(temp[i])
    return temp2
    
    
    
#Counting Dictonary    
from itertools import groupby

def count_dict(s):
    s=s.lower()
    groups = groupby(s)
    result = [(label, sum(1 for _ in group)) for label, group in groups]
    return "".join("{}{}".format(label, count) for label, count in result)
