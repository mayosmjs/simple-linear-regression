#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:05:47 2019

@author: Calvin
"""


#===========================================================================================================================
#========================================== PREDICTING WEIGHT GIVEN THE HEIGHT==============================================
#===========================================================================================================================
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split



height_weight = pd.read_csv("height_weight.csv")
male_df = height_weight[height_weight.Gender == 'Male'].iloc[:,[1,2]].values
male_df.shape


#Values
X = male_df[:,:1] #[HEIGHT] INDEPENDENT VALUE
y = male_df[:,1]  #DEPENDENT VALUE [WEIGHT]

#Tran
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 1/3,random_state = 0)

#Model slr
lm = linear_model.LinearRegression()
model = lm.fit(X_train,y_train)

#Predicting the test set
y_pred = model.predict(X_test) #predicted weights


# A. Visualize Training Set
plt.scatter(X_train,y_train,color = "red") #Real Values
plt.plot(X_train,model.predict(X_train),color = "blue") # Predictions
plt.title("Height vs Weight (Training Set)")
plt.ylabel("Weight")
plt.xlabel("Height")
plt.show()




# B. Visualise the test set
#The red dot are the real weights of people and the blue line is the predicted weight from our model
plt.scatter(X_test,y_test,color = "red")
plt.plot(X_train, model.predict(X_train),color = "blue")
plt.title("Height vs Weight (Test Set)")
plt.ylabel("Weight")
plt.xlabel("Height")
plt.show()
