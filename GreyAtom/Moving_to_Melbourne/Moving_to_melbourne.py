# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:29:31 2020

@author: Mrityunjay1.Pandey

Below is the brief description about the data

Feature	Description
Rooms	Number of rooms
Type	Property type
Price	Price in dollars
Method	Property status
SellerG	Real Estate Agent
Distance	Distance from CBD
Postcode	Code of the area
Bathroom	Number of Bathrooms
Car	Number of carspots
Landsize	Land Size
BuildingArea	Building Size
YearBuilt	The year in which home was built
CouncilArea	Governing council for the area
Longtitude	The angular distance of a place east or west
Regionname	General Region (West, North West, North, Northeast …etc)
PropertyCount	Number of properties that exist in the suburb
"""
#Path of the File location
path='./Moving_to_melbourne.csv'

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.linear_model import Lasso,Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

df=pd.read_csv(path)
print("\t\t-:First 5 records of the DataFrame:-\n",df.head(5))

#Splitting daata in features (Independent Values) and Dependent values
X=df.drop(columns='Price') #Features
y=df.Price

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=6)

cor = X_train.corr()
print("Correlation of features are:",cor)

#Heatmap chart for correlation of the features
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,10))
cor = X_train.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()

#Task 2
regressor=LinearRegression()
regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test)

#RMSE
r2=r2_score(y_test,y_pred)
print("R Squared Score is:",r2)

#Task 3
lasso=Lasso()
lasso.fit(X_train,y_train)
lasso_pred=lasso.predict(X_test)
r2_lasso=r2_score(y_test,lasso_pred)
print("R Squared Error for Lasso Model is: ",r2_lasso)

#Task 4

ridge=Ridge()
ridge.fit(X_train,y_train)
ridge_pred=ridge.predict(X_test)
r2_ridge=r2_score(y_test,ridge_pred)
print("R Squared Error for Ridge Model is: ",r2_ridge)

#Task 5
regressor=LinearRegression()
score=cross_val_score(regressor,X_train,y_train,cv=10)
mean_score=np.mean(score)
print("Mean Score of Cross Validation Model is:",mean_score)

#Task 6
model=make_pipeline(PolynomialFeatures(2),LinearRegression())
model=make_pipeline()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
r2_poly=r2_score(y_test,y_pred)

print("R^2 score of Polynomial is:",r2_poly)