#Importing Necessary Packages
import pandas as pd
import requests as req
import numpy as np
import matplotlib.pyplot as plt

#Defining data location oath
path='C:/Users/mrityunjay1.pandey/GreyAtom/Day7/Session_4_Hackathon/Problems/2_Pandas/excel-comp-data.csv'
#Reading file to dataframe
df=pd.read_csv(path)

#Converting states to lower case
df.state=df.state.str.lower()

#Adding quarter values in total column
df['total']=df.iloc[:,-3:].sum(axis=1)

#Adding Months sum in new row
sumtot=df.iloc[:,-4:].sum(axis=0)
df_final=df.append([{'Jan':sumtot[0],'Feb':sumtot[1],'Mar':sumtot[2],'total':sumtot[3]}],ignore_index=True)

#####################Scrapeing Data from Website#####################
url='https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response=req.get(url)
#Extracting frist table from the scraped data
df1=pd.read_html(response.content)[0]

#Removing unwanted data
df1=df1.iloc[10:]
#Column name changed
df1  = pd.DataFrame(df1.values[1:], columns=df1.iloc[0])
#Ranming 3 column name to 'Abbrevation'
df1.rename(columns={df1.columns[2]:'Abbrevation'},inplace=True)
#Removing space from first column
df1['United States of America']=df1['United States of America'].apply(lambda x: x.replace(" ", "")).astype(object)
#Writing to CSV
df1.to_csv("scraped.csv")

#Reading CSV file from the location
path1='C:/Users/mrityunjay1.pandey/GreyAtom/Day7/Session_4_Hackathon/Problems/2_Pandas/scraped.csv'
scraped=pd.read_csv(path1)

#Convert to Lower case
scraped["United States of America"]=scraped["United States of America"].str.lower()
#Mappng to final output
df_final=pd.merge(df_final,scraped[["United States of America","Abbrevation"]],left_on = "state",right_on = "United States of America",how = "left")
#Dropping columns which are not needed
#df_final.drop('abbr',axis=1,inplace=True)
df_final.drop('United States of America',axis=1,inplace=True)
#Renaimng colun to be in sync with team
df_final.rename(columns={'Abbrevation':'Abbr'},inplace=True)


#Creating dictonary of mappng and Abberavtion
df1.set_index('United States of America')['Abbrevation'].to_dict()

df_final=pd.merge(df_final,scraped[["United States of America","Abbrevation"]],left_on = "state",right_on = "United States of America",how = "left")
df_final.drop('abbr',axis=1,inplace=True)
df_final.drop('United States of America',axis=1,inplace=True)
df_final.rename(columns={'Abbrevation':'Abbr'},inplace=True)


df_final.insert(6,'abbr',np.nan)

df_final[['Abbr','state']]

df_final_new=df_final.copy(deep=True)
#This ill work if we have single return of the condition
df_final.loc[df_final['state'].isin(['mississipi','tenessee']),'Abbr']=['MS','TN']

#Another method to achieve above 
df_final.loc[df_final['state']=='mississipi','Abbr']='MS'
df_final.loc[df_final['state']=='tenessee','Abbr']='TN'

df_sub=df_final.iloc[:,-5:].groupby(by='Abbr').sum()

df_sub.loc['Total',:]=df_sub.sum(axis=0)

formatted_df=df_sub.applymap(lambda x: "${:,.0f}".format(x))

final_table=df_sub

#Plotting Pie Chart
plt.figure(figsize=(10,6))
plt.pie(df_sub['total'][:-1],labels=df_sub['total'][:-1].index,autopct="%1.1f%%",shadow=True, startangle=90)
plt.show()