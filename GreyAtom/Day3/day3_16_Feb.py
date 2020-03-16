# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:38:04 2020

@author: Mrityunjay1.Pandey
"""

import pandas as pd
path='C:/Users/mrityunjay1.pandey/GreyAtom/Day3/gapminder_mj.csv'
df=pd.read_csv(path)

#Dropping row Region
df.drop("Region",1,inplace=True)
X=df.drop("life",1)
#Selecting output the model will have
y=df.life
#Importing sklearn for implementing model
from sklearn.model_selection import train_test_split as tts
X_Train,X_test,y_train,y_test=tts(X,y,random_state=35,test_size= 0.26)
#Importing KNN for regression
from sklearn.neighbors import KNeighborsRegressor
model = KNeighborsRegressor(n_neighbors=30)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
model.fit(X_Train,y_train)
y_pred=model.predict(X_test)
mean_absolute_error(y_test,y_pred)
r2_score(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
