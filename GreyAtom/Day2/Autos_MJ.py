# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:30:40 2020

@author: Mrityunjay1.Pandey
"""

#--------------------Part 1--------------------
#Read the autos.csv CSV file into pandas, and assign it to the variable name autos.
#Try without specifying any encoding (which will default to UTF-8)
#If you get an encoding error,try the next two most popular encodings (Latin-1
# and Windows-1252) until you are able to read the file without error. 
#Create a new cell with just the variable autos and run this cell. 
#A neat feature of jupyter notebook is its ability to render the first few and 
#last few values of any pandas object.Use the DataFrame.info() and DataFrame.head() 
#methods to print information about the autos dataframe, as well as the first few rows.

#-----------Solution Of Part 1----------------

#Importing pandas package
import pandas as pd

#Defining path of the data file to be read from
autos_path='C:/Users/mrityunjay1.pandey/GreyAtom/Day2/autos.csv'

#Reading file without specifying any encoding
#autos=pd.read_csv(autos_path)
#running above line gives below error 
#"UnicodeDecodeError: 'utf-8' codec can't decode byte 0xdc in position 23: invalid continuation byte

#Reading data with encodng specified, both encoding Windows-1252 & Latin-1 works fine.
#autos_win=pd.read_csv(autos_path,encoding='Windows-1252')
autos=pd.read_csv(autos_path,encoding='latin-1')

#Getting information about the dataframe
autos.info()
#getting first 5 rows of the dataframe
autos.head()

#--------------------Part 2--------------------
#Use the DataFrame.columns attribute to print an array of the existing column names.
#Copy that array and make the following edits to columns names: 
#    yearOfRegistration to registration_year 
#    monthOfRegistration to registration_month 
#    notRepairedDamage to unrepaired_damage 
#    dateCreated to ad_created 
#The rest of the columnn names from camelcase to snakecase.
#Assign the modified column names back to the DataFrame.columns attribute. 
#Use DataFrame.head() to look at the current state of the autos dataframe.


#-----------Solution Of Part 2----------------


#Getting column names of the dataframe
list_columns=list(autos.columns)
#Renaming columns as asked in the excersise
autos.rename(columns={
        "yearOfRegistration":"registration_year",
        "monthOfRegistration":"registration_month",
        "notRepairedDamage":"unrepaired_damage",
        "dateCreated":"ad_created"},inplace=True)

#Attempt 1
#Function to convert column names in Snake Case
def to_snake_case(str):
    return ''.join(['_'+i.lower() if i.isupper()  
               else i for i in str]).lstrip('_') 
         
#Applying for loop and passing string in the function
j=0
for i in list_columns:
    list_columns[j]=to_snake_case(list_columns[j])
    j=j+1
#assigning modified name to column names
autos.columns=list_columns
##Attempt 2
##Function to convert column names in Snake Case
#def to_snake_case2(list_str):
#    j=0
#    for i in list_str:
#        
#       list_str[j]= ''.join(['_'+i.lower() if i.isupper()  
#               else i for i in list_str[j]]).lstrip('_')
#       j=j+1
#    return list_str
##Getting column names of the dataframe
#list_columns=list(autos.columns)
##Call to function
#to_snake_case2(list_columns)

#Use DataFrame.describe() to look at descriptive statistics for all columns

#--------------------Part 3--------------------

#Use DataFrame.describe() to look at descriptive statistics for all columns.
#Write a markdown cell noting: Any columns that have mostly one value that are candidates to be dropped 
#Any columns that need more investigation.
#Any examples of numeric data stored as text that needs to be cleaned.
#If you need to investigate any columns more, do so and write up any additional things you found.
#You likely found that the price and odometer columns are numeric values stored as text.
#For each column: Remove any non-numeric characters. Convert the column to a numeric dtype. 
#Use DataFrame.rename() to rename the column to odometer_km.

#--------------------Solution to Part 3--------------------
#To describe dataframe
autos.describe()
#DataType correction
#date_crawled             50000 non-null object Should be DateTime Object
#price                    50000 non-null object Should be integer
#odometer                 50000 non-null object Should be integer
#date_created             50000 non-null object Should be Date Time 
#last_seen                50000 non-null object Should be Date

#Replacing special symbols "$ & ," from Price
autos.price=autos.price.str.replace(",","").str.replace("$","").astype(int)

#Renaming odometer column to odomete_KM for better understanding and removing "," & "KM" from odometer data.
#Converting type of odometer_km from object to float
autos.rename(columns={"odometer":"odometer_km"},inplace=True)
autos.odometer_km=autos.odometer_km.str.replace(",","").str.replace("km","").astype(float)

#Conveting date_crawled to datetime
autos.date_crawled=pd.to_datetime(autos.date_crawled)

#Conveting date_created to datetime
autos.date_created=pd.to_datetime(autos.date_created)

#Conveting last_seen to datetime
autos.last_seen=pd.to_datetime(autos.last_seen)

#Identifying columns to drop.
#Since nr_of_pictures has values 0 for all records hence no influnnce in the model, thus candidate for dropping.
autos.drop(["nr_of_pictures"],1,inplace=True)
#seller column has 2 values with 49999 records having same and 1 of different hence no influnce on the model.Thus candidate for dropping.
autos.drop(["seller"],1,inplace=True)
#Offer_type has similar type of value for all records except 1 thus candidate of dropping.
autos.drop(["offer_type"],1,inplace=True)

#--------------------Part 4--------------------

#For each of the odometer_km and price columns: 
#Use the techniques above to explore the data If you find there are outliers, remove them and write a markdown paragraph explaining your decision. 
#After you have removed the outliers, make some observations about the remaining values.

#--------------------Solution of Part 4--------------------
#=============Analysis of odometer_km data=================
autos[autos["odometer_km"]<125000].odometer_km.value_counts()
#Out[82]: 
#100000.0    2169
#90000.0     1757
#80000.0     1436
#70000.0     1230
#60000.0     1164
#50000.0     1027
#5000.0       967
#40000.0      819
#30000.0      789
#20000.0      784
#10000.0      264
#Name: odometer_km, dtype: int64

autos[autos["odometer_km"]<125000].odometer_km.value_counts().sum()
#Out[84]: 12406

autos[autos["odometer_km"]>125000].odometer_km.value_counts().sum()
#Out[85]: 32424

autos[autos["odometer_km"]==125000].odometer_km.value_counts().sum()
#Out[86]: 5170
#=================================================================

#=============Analysis of price data=================
autos.price.value_counts()
#Out[89]: 
#0        1421
#500       781
#1500      734
#2500      643
#1000      639
#
#20790       1
#8970        1
#846         1
#2895        1
#33980       1
#Above analysis says there are data in price columns with values 0 and few with single entries.

autos[autos.price==0].price.value_counts().sum()
#Out[92]: 1421

#There are 1421 records having price as 0.Since this is an advertisement for selling cars, 
#there should not be any advertisement of used car having price as 0. Thus droping these records
autos.drop(autos[autos.price==0].index,0,inplace=True)
#Sorting dataframe on price column in descending
autos.sort_values("price",ascending=False,inplace=True)

#droping top 7 rows of price having outliers.
autos.drop(autos.price.head(7).index,0,inplace=True)

#Plotting scatterplot still shows 2 outliers in price.droping those 2 as well.
import matplotlib.pyplot as plt
plt.scatter(autos.price,autos.price)
autos.drop(autos.price.head(2).index,0,inplace=True)

#Further analysis shows price range is still skewed thus dropping columns having price as 1
autos.drop(autos[autos.price==1].price.index,0,inplace=True)

#Further analysis reveals there are still outliers for odometer_km & price.
plt.scatter(autos.price,autos.odometer_km)
#Since these are used cars with more odometer_KM the price of car should not increase.
#Removing 5 outliers from price more than 600000
autos.drop(autos[autos.price>600000].index,0,inplace=True)

#Defining bin using qcut
pd.qcut(autos['price'], q=7).value_counts().plot(kind="hist")

#--------------------Part 5--------------------
#Use the workflow we just described to calculate the distribution of values in the date_crawled,
#ad_created, and last_seen columns (all string columns) as percentages.
#To include missing values in the distribution and to use percentages instead of counts, 
#chain the Series.value_counts(normalize=True, dropna=False) method.
#To rank by date in ascending order (earliest to latest), chain the Series.sort_index() method. 
#Write a markdown cell after each column exploration to explain your observations.
# Use Series.describe() to understand the distribution of registration_year.

#--------------------Solution of Part 5--------------------

#Converting data in date_crawled from yyyy-mm-dd hh:mm:ss to yyyy-mm-dd
autos.date_crawled=pd.to_datetime(autos.date_crawled,format='%d/%m/%y').dt.strftime('%d-%m-%Y')
#Converting data in date_created from yyyy-mm-dd hh:mm:ss to yyyy-mm-dd
autos.date_created=pd.to_datetime(autos.date_created,format='%d/%m/%y').dt.strftime('%d-%m-%Y')
#Converting data in last_seen from yyyy-mm-dd hh:mm:ss to yyyy-mm-dd
autos.last_seen=pd.to_datetime(autos.last_seen,format='%d/%m/%y').dt.strftime('%d-%m-%Y')

#Checking ads created(date_created) in the month of the year
pd.to_datetime(autos.date_created,format='%d-%m-%Y').dt.strftime('%m-%Y').value_counts()
#Out[215]: 
#03-2016    40543
#04-2016     7787
#02-2016       61
#01-2016       12
#12-2015        2
#09-2015        1
#11-2015        1
#08-2015        1
#06-2015        1

#Checking date_crawled in the month of the year
pd.to_datetime(autos.date_crawled,format='%d-%m-%Y').dt.strftime('%m-%Y').value_counts()
#Out[210]: 
#03    40571
#04     7838

#Checking last_seen in the month of the year
pd.to_datetime(autos.last_seen,format='%d-%m-%Y').dt.strftime('%m-%Y').value_counts()

#Checking percenatge of date_crawled
autos.date_crawled.value_counts(normalize=True,dropna=False)
#Out[222]: 
#03-04-2016    0.038588
#20-03-2016    0.037803
#21-03-2016    0.037307
#12-03-2016    0.036956
#14-03-2016    0.036625
#04-04-2016    0.036481
#07-03-2016    0.036047
#02-04-2016    0.035489
#28-03-2016    0.034849
#19-03-2016    0.034746
#15-03-2016    0.034270
#29-03-2016    0.034126
#30-03-2016    0.033733
#01-04-2016    0.033733
#08-03-2016    0.033279
#09-03-2016    0.033052
#22-03-2016    0.032928
#11-03-2016    0.032597
#23-03-2016    0.032267
#26-03-2016    0.032246
#10-03-2016    0.032205
#31-03-2016    0.031812
#17-03-2016    0.031626
#25-03-2016    0.031564
#27-03-2016    0.031131
#16-03-2016    0.029519
#24-03-2016    0.029395
#05-03-2016    0.025367
#13-03-2016    0.015658
#06-03-2016    0.014068
#05-04-2016    0.013076
#18-03-2016    0.012911
#06-04-2016    0.003161
#07-04-2016    0.001384

#Working with DateTime
import datetime as dt
autos['age_of_vehicle_months']=(dt.datetime.now().year-autos.year_of_registration)*12 + autos.month_of_registration

#After calculating age of vehicle it looks like their are vehicles having negative age, which can't be the case.
#dropping such records.

autos.drop(autos[autos.age_of_vehicle_months<0].age_of_vehicle_months.index,0,inplace=True)

#Month of registration values has 0 which can't be the case, replacing all 0 with 1 for start of the year.
autos.month_of_registration=autos.month_of_registration.replace(0,1)

#???????????Confused?????????How to conver month.

#autos['age_in_month']=pd.to_datetime((autos.month_of_registration.astype(str)+"-"+autos.year_of_registration.astype(str)),format='%m-%Y').dt.strftime('%m-%Y')

#--------------------Part 6--------------------
#Decide which the highest and lowest acceptable values are for the registration_year column.
#Write a markdown cell explaining your decision and why.
#Remove the values outside those upper and lower bounds and calculate the distribution of the remaining values using Series.value_counts(normalize=True).
#Write a markdown cell explaining your observations

#-------------Solution of Part 6----------------

#Analysis shows there are 9 records having age of vehicle more than 100 Yrs.Which doesn't seem to be correct.Removing these records.
autos[autos.age_of_vehicle_months/12>100]

autos.drop(autos[autos.age_of_vehicle_months/12>100].age_of_vehicle_months.index,0,inplace=True)
#Binning the age of vehicles it suggest 60% of vehicles are of age 14 to 27 Years.35% of 1 to 14 years
pd.cut(autos['age_of_vehicle_months'],bins=7).value_counts(normalize=True)
#Out[67]: 
#(173.857, 331.714]    0.594523
#(14.895, 173.857]     0.354779
#(331.714, 489.571]    0.040570
#(489.571, 647.429]    0.007399
#(647.429, 805.286]    0.002315
#(963.143, 1121.0]     0.000227
#(805.286, 963.143]    0.000186
#Name: age_of_vehicle_months, dtype: float64

#Increasing the bin size to 15 shows to 5 distribution of age of cars. 34% of age 13-19,27% of age 19-25,
#21% of age 7 to 13,9% of age 1 to 7 & 5% of age 25-32
pd.cut(autos['age_of_vehicle_months'],bins=15).value_counts(normalize=True)
#Out[75]: 
#(163.333, 237.0]       0.341366
#(237.0, 310.667]       0.274341
#(89.667, 163.333]      0.218539
#(14.895, 89.667]       0.093128
#(310.667, 384.333]     0.050036

#in Summary 97% of the cars are in age group 1-32

#--------------------Part 7--------------------
#Explore the unique values in the brand column, and decide on which brands you want to aggregate by.
#You might want to select the top 20, or you might want to select those that have over a certain percentage of the total values (e.g. > 5%).
#Remember that Series.value_counts() produces a series with index labels, so you can use Series.index attribute to access the labels, should you wish. 
#Write a short paragraph describing the brand data, and explaining which brands you've chosen to aggregate on.
#Create an empty dictionary to hold your aggregate data.
#Loop over your selected brands, and assign the mean price to the dictionary, with the brand name as the key. 
#Print your dictionary of aggregate data, and write a paragraph analyzing the results.

#-------------Solution of Part 7----------------

#Unique values in brand
pd.unique(autos.brand)
#
autos.brand.value_counts()
#Out[88]: 
#volkswagen        10303
#bmw                5253
#opel               5245
#mercedes_benz      4634
#audi               4155
#ford               3375
#renault            2316
#peugeot            1426
#fiat               1260
#seat                916
#skoda               778
#nissan              740
#mazda               739
#smart               694
#citroen             683
#toyota              611
#hyundai             482
#sonstige_autos      459
#volvo               437
#mini                418
#mitsubishi          394
#honda               387
#kia                 345
#alfa_romeo          320
#porsche             285
#suzuki              285
#chevrolet           274
#chrysler            169
#dacia               129
#daihatsu            122
#jeep                107
#subaru              101
#land_rover           99
#saab                 79
#daewoo               76
#jaguar               74
#trabant              66
#rover                65
#lancia               55
#lada                 29
#Name: brand, dtype: int64

#Taking percentage share of brands in the data
autos.brand.value_counts(normalize=True)*100
#volkswagen        21.293789
#bmw               10.856670
#opel              10.840136
#mercedes_benz      9.577348
#audi               8.587372
#ford               6.975302
#renault            4.786607
#peugeot            2.947194
#fiat               2.604113
#seat               1.893149
#skoda              1.607936
#nissan             1.529400
#mazda              1.527333
#smart              1.434329
#citroen            1.411595
#toyota             1.262788
#hyundai            0.996177
#sonstige_autos     0.948641
#volvo              0.903172
#mini               0.863904
#mitsubishi         0.814302
#honda              0.799835
#kia                0.713031
#alfa_romeo         0.661362
#porsche            0.589026
#suzuki             0.589026
#chevrolet          0.566291
#chrysler           0.349282
#dacia              0.266612
#daihatsu           0.252144
#jeep               0.221143
#subaru             0.208742
#land_rover         0.204609
#saab               0.163274
#daewoo             0.157073
#jaguar             0.152940
#trabant            0.136406
#rover              0.134339
#lancia             0.113672
#lada               0.059936
#creating Brand List for getting aggregate data
brand_list=['volkswagen', 'bmw', 'opel', 'mercedes_benz', 'audi', 'ford', 'renault',
       'peugeot', 'fiat', 'seat', 'skoda', 'nissan', 'mazda', 'smart',
       'citroen']
#Empty dictnory initialisation for storing mean price
mean_price_per_brand={}

for i in brand_list:
    #price_mean=autos[autos["brand"]==i].price.mean()
    #temp={i:price_mean}
    mean_price_per_brand.update({i:autos[autos["brand"]==i].price.mean()})

print("::::::::Price of brands::::::::\n",mean_price_per_brand)

#--------------------Part 8--------------------

#Use the loop method from the last screen to calculate the mean mileage and mean price for
#each of the top brands, storing the results in a dictionary.
#Convert both dictionaries to series objects, using the series constructor.
#Create a dataframe from the first series object using the dataframe constructor.
#Assign the other series as a new column in this dataframe.
#Pretty print the dataframe, and write a paragraph analyzing the aggregate data.

#-------------Solution of Part 8----------------