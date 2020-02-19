a# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

x   =[17,13,12,15,16,14,16,16,18,19]
y  = [94,73,59,80,93,85,66,79,77,91]


df = pd.DataFrame({'X':x,'Y':y})

xmean = np.mean(df['X'])
ymean = np.mean(df['Y'])

df['xsq'] = np.square(df['X'])
df['ysq'] = np.square(df['Y'])
df['xy'] = df['X']*df['Y']


beta =(len(df)*df['xy'].sum()-df['X'].sum()*df['Y'].sum())/(len(df)*sum(df['xsq'])-np.square((sum(df['X']))))

alpha = ymean - beta*xmean


from sklearn.linear_model import LinearRegression

lm = LinearRegression()

X = np.c_[df["X"]]
Y = np.c_[df["Y"]]

model = lm.fit(X,Y)

print(model.intercept_)
print(model.coef_)


print(model.predict([[15,12]])) 
