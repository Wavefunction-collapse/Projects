# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:49:57 2020

@author: Nikolai
"""


#Linear regression
import sklearn as sk
from sklearn.linear_model import LinearRegression
#numpy and pandas will be used for data manipulation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Quandl for historical oil prices
import quandl 

#Setting our API key
quandl.ApiConfig.api_key = "MMBxPa7_RWDGyZgXt-gG"
data = quandl.get("FRED/DCOILBRENTEU", start_date="2000-01-01", end_date="2020-05-01")
print(data.head()) #which data are you using

# Y-axis
plt.ylabel("Crude Oil Prices: Brent-Europe")

#size of our graph
data.Value.plot(figsize=(10,5))

#Prediction of the oil prices for 7 days and 22 days

data['MA7'] = data['Value'].shift(1).rolling(window=7).mean()
data['MA22']= data['Value'].shift(1).rolling(window=22).mean()

#dropping the NaN values
data = data.dropna()
#X-axis

X = data[['MA7', 'MA22']]

#Getting the head of the data

print(X.head())

y = data['Value']

print(y.head())

#Setting up the training set

training = 0.99999999
t = int(training*len(data))
X_train = X[:t]
y_train = y[:t]

X_test = X[t:]
y_test = y[t:]

# Generate the coefficient and constant for the regression
model = LinearRegression().fit(X_train,y_train)

predicted_price = model.predict(X_test)
predicted_price = pd.DataFrame(predicted_price, index=y_test.index, columns=['price'])
y_test.plot()
plt.legend(['Predicted Price','Actual Price'])
plt.ylabel("Crude Oil Prices: Brent - Europe")
plt.show()


