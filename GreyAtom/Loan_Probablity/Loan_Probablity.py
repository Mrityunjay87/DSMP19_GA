# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 22:07:11 2020

@author: Mrityunjay1.Pandey
"""
path="./Loan_Probablity.csv"

import pandas as pd
import numpy as np
df=pd.read_csv(path)

print("Total Number of approved Loans are {} out of {}".format(df[df['Loan_Status']=='Y'].Loan_Status.value_counts()[0],len(df)))

total =len(df)
yes = len(df[df['Loan_Status']=='Y'])

p_of_A=yes/total

print("Probablity of loan Approval is {}".format(p_of_A))

#Which area is the house located in?

p_of_urban=len(df[df.Property_Area=='Urban'])/total

p_of_semiurban=len(df[df.Property_Area=='Semiurban'])/total

p_of_or=len(df[df['Property_Area'].isin(['Semiurban','Urban'])])/total

pofor=p_of_urban+p_of_semiurban

print("Probablty of houses in Urban is {},Semiurban is {} & in either of the area is {}".format(p_of_urban,p_of_semiurban,pofor))

#Does gender affect the probability of getting a loan?


# Convert to NumPy arrays
g=np.array(df.Gender)
l=np.array(df.Loan_Status)

# creating pivot table 
table=pd.crosstab(g,l)
print("Pivot table of Gender and Loan Approval:\n",table)

# Total male applicants
print("Total Male Applicants are:",table.iloc[1,:].sum())

# Total female applicants
print("Total female applicants",table.iloc[0,:].sum())

# Total male applicants whose loan applications were accepted
print("Total male applicants whose loan applications were accepted are:",table['Y'][1])

# Total female applicants whose loan applications were accepted
print("Total female applicants whose loan applications were accepted are:",table['Y'][0])

# Probability of loan approval when applicant is male
p_of_ymale=table['Y'][1]/table.iloc[1,:].sum()
print("Probability of loan approval when applicant is male:{}".format(p_of_ymale))

# Probability of loan approval when applicant is female
p_of_yfemale=table['Y'][0]/table.iloc[0,:].sum()
print("Probability of loan approval when applicant is female:{}".format(p_of_yfemale))

if p_of_ymale!=p_of_yfemale:
    print("The above results shows Gender Does affect Loan Approval Status")
else:
    print("The above results shows Gender Does Not affect Loan Approval Status")
