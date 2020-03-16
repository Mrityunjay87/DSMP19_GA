# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:48:31 2020

@author: Mrityunjay1.Pandey
"""

import pandas as pd
path='C:/Users/mrityunjay1.pandey/GreyAtom/Day3/gapminder_mj.csv'
df=pd.read_csv(path)

df.drop(["Region"],1,inplace = True)
X = df.drop(["GDP"],1)
y = df["GDP"]
from sklearn.model_selection import train_test_split as tts, KFold, GridSearchCV, StratifiedKFold
X_train, X_test, y_train, y_test = tts(X,y,random_state = 42, test_size= 0.26)
from sklearn.neighbors import KNeighborsRegressor
model1 = KNeighborsRegressor(n_neighbors = 3, metric="euclidean")
model2 = KNeighborsRegressor(n_neighbors = 5, metric="euclidean")
model3 = KNeighborsRegressor(n_neighbors = 7, metric="euclidean")
model4 = KNeighborsRegressor(n_neighbors = 9, metric="euclidean")
model5 = KNeighborsRegressor(n_neighbors = 11, metric="euclidean")

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

models = [model1,model2,model3,model4,model5]
maes=[]
for x in models:
    x.fit(X_train,y_train)
    y_pred = x.predict(X_test)
    maes.append(mean_absolute_error(y_test,y_pred))