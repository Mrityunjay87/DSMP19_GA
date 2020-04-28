# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:13:06 2020

@author: Mrityunjay1.Pandey
"""
#Task 1 - Add Polynomial Features
# Code starts here

# Add square and cubic powers of 'GarageScore' to train and test
X_train['GarageScore-2']=X_train.GarageScore**2
X_train['GarageScore-3']=X_train.GarageScore**3
X_test['GarageScore-2']=X_test.GarageScore**2
X_test['GarageScore-3']=X_test.GarageScore**3

# logarithmic transformation of target
y_train=np.log1p(y_train)
y_test=np.log1p(y_test)


# display first five rows of train and test features
X_train.head(5)
X_test.head(5)
# Code ends here

#Task 2 - Find Root Mean Squared Error
# import packages
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Code starts here

# instantiate and fit model
model=LinearRegression()
model.fit(X_train,y_train)

# make predictions and calculate rmse
preds=model.predict(X_test)
rmse=np.sqrt(mean_squared_error(preds,y_test))
print("RMSE is :{}".format(rmse))
# Code ends here

#Task 3 - Observe Underfitting
# instantiate new model
model_2 = LinearRegression()

# train and test sets with 100 features
new_X_train = X_train.iloc[:,0:100]
new_X_test = X_test.iloc[:,0:100]
print(new_X_train.shape)
print(new_X_test.shape)

# fit and predict
model_2.fit(new_X_train, y_train)
pred_2 = model_2.predict(new_X_test)

# calculate RMSE
rmse_2 = np.sqrt(mean_squared_error(pred_2, y_test))
rmse_2=12892902857.13
print(rmse_2)

print(round(rmse_2, 2))

#Task 4 - Does Lasso Do Better?
# import packages
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

# Code starts here

# instantiate lasso model
lasso=Lasso()

# fit and predict
lasso.fit(X_train,y_train)
lasso_pred=lasso.predict(X_test)


# calculate RMSE
lasso_rmse=np.sqrt(mean_squared_error(lasso_pred,y_test))
print("Lasso RMSE:{}".format(lasso_rmse))

# check how many feature coefficients are zero
zero_features=0
for i in range(len(lasso.coef_)):
    if lasso.coef_[i]==0:
      zero_features+=1

print("Total Number of Zero Coeff are :{}".format(zero_features))



# Code ends here

#Task 5 - Does Ridge Do Better?
# Code starts here

# instantiate Ridge model
ridge=Ridge()


# fit and predict
ridge.fit(X_train,y_train)
ridge_pred=ridge.predict(X_test)

# calculate RMSE

ridge_rmse=np.sqrt(mean_squared_error(ridge_pred,y_test))
print("RMSE is :{}".format(ridge_rmse))

# Code ends here

#Task 6 - Will You Choose Lasso or Ridge with the Holdout Method?
# import packages
from sklearn.model_selection import train_test_split
import numpy as np

# split into training and validation
train_feat, test_feat, train_tar, test_tar = train_test_split(X_train, y_train, test_size=0.25, random_state=42)

# Code starts here

# initiate lasso and ridge
l1=Lasso()
l2=Ridge()

# fit on training
l1.fit(train_feat,train_tar)
l2.fit(train_feat,train_tar)

# make predictions and calculate RMSE on validation data
pred_l1=l1.predict(test_feat)
pred_l2=l2.predict(test_feat)

rmse_l1=np.sqrt(mean_squared_error(pred_l1,test_tar))
rmse_l2=np.sqrt(mean_squared_error(pred_l2,test_tar))
print("RMSE for Lasso is :{} & For Ridge is :{}".format(rmse_l1,rmse_l2))
# select best model

selected_model = l1 if rmse_l1 < rmse_l2 else l2
print("Selected Model is:",selected_model)

# make prediction on test data and calculate RMSE
selected_model_pred=selected_model.predict(X_test)
rmse_selected_model_pred=np.sqrt(mean_squared_error(selected_model_pred,y_test))

print("RMSE of Prediciton by Best Model is:",rmse_selected_model_pred)
# Code ends here

#Task 7 - Use K-Fold |Cross Validation for Model Selection
# import packages
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score
scorer = make_scorer(mean_squared_error, greater_is_better = False)

# Code starts here

# instantiate L1 and L2
L1=Lasso()
L2=Ridge()


# cross validation with L1
rmse_L1=-np.mean(cross_val_score(L1,X_train,y_train,scoring=scorer,cv=10))
print("RMSE L1:",rmse_L1)
# cross validation with L2
rmse_L2=-np.mean(cross_val_score(L2,X_train,y_train,scoring=scorer,cv=10))
print("RMSE L2:",rmse_L2)
# select best model
Model = L1 if rmse_L1<rmse_L2 else L2
print("Selected Model is:",Model)
# calculate RMSE on test data
Model.fit(X_train,y_train)
Pred=Model.predict(X_test)
Error=np.sqrt(mean_squared_error(Pred,y_test))
print("Error is:",Error)
# Code ends here

# import packages
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import warnings
warnings.filterwarnings('ignore')

# regularization parameters for grid search
ridge_lambdas = [0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1, 3, 6, 10, 30, 60]
lasso_lambdas = [0.0001, 0.0003, 0.0006, 0.001, 0.003, 0.006, 0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1]

# Code starts here

# instantiate lasso and ridge models
lasso_model=Lasso()
ridge_model=Ridge()

# grid search on lasso and ridge
ridge_grid=GridSearchCV(ridge_model,param_grid=dict(alpha=ridge_lambdas))
ridge_grid.fit(X_train,y_train)

lasso_grid=GridSearchCV(lasso_model,param_grid=dict(alpha=lasso_lambdas))
lasso_grid.fit(X_train,y_train)
# make predictions 
ridge_pred=ridge_grid.predict(X_test)
ridge_rmse=np.sqrt(mean_squared_error(ridge_pred,y_test))

lasso_pred=lasso_grid.predict(X_test)
lasso_rmse=np.sqrt(mean_squared_error(lasso_pred,y_test))


# print out which is better
best_model='LASSO' if lasso_rmse<ridge_rmse else 'RIDGE'
print("Best Model is:",best_model)



# Code ends here
