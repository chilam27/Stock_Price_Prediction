# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:42:07 2020

@author: Chi Lam
"""

#Import module
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from sklearn.metrics import mean_squared_error
import datetime
import matplotlib.pyplot as plt
%matplotlib inline

tf.__version__

#Read in data
df = pd.read_csv('stock_cleaned.csv')
df['Date'] =  pd.to_datetime(df['Date'])


#Data normalization
norm = MinMaxScaler(feature_range=(0,1))
df_close = norm.fit_transform(np.array(df.Close).reshape(-1,1))

df_close.shape


#Splitting test and train data set
train_size = int(len(df_close)*0.7)
train, test = df_close[0:train_size,:], df_close[train_size:,:]


#Convert data array into matrix
def to_matrix(data, time_step = 1):
    x_data, y_data = [], []
    for i in range(len(data) - time_step - 1):
        a = data[i:(i + time_step), 0]
        x_data.append(a)
        y_data.append(data[i + time_step, 0])
    return np.array(x_data), np.array(y_data)

time_step = 100
X_train, y_train = to_matrix(train, time_step)
X_test, y_test = to_matrix(test, time_step)


#Building a stacked LSTM model
##Reshape input for model
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

##Create model
model = Sequential()
model.add(LSTM(50, return_sequences = True, input_shape = (100,1)))
model.add(LSTM(50, return_sequences = True))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer = 'adam')

model.summary()

model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs = 100, batch_size= 64, verbose = 1)


#Prediction
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)


#Check performance
train_predict = norm.inverse_transform(train_predict)
test_predict = norm.inverse_transform(test_predict)

mean_squared_error(y_train, train_predict)**(1/2)
mean_squared_error(y_test, test_predict)**(1/2)


##Plotting
###Shift train predictions for plotting
trainPredictPlot = np.empty_like(df_close)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[time_step:len(train_predict) + time_step, :] = train_predict

###Shift test predictions for plotting
testPredictPlot = np.empty_like(df_close)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(train_predict) + (time_step * 2) + 1:len(df_close) - 1, :] = test_predict

####Plot baseline and predictions
train_flatten = trainPredictPlot.flatten()
test_flatten = testPredictPlot.flatten()
df_predict = pd.DataFrame({'Date': df.Date, 
                           'train_predict': train_flatten, 
                           'test_predict': test_flatten})
df_predict = df_predict.set_index('Date')

df_1 = df.set_index(df['Date'])

plt.figure(figsize=(10,5))
plt.plot(df_1.Close, label = 'Actual Price')
plt.plot(df_predict.train_predict, label = 'Prediction of Train Data Set')
plt.plot(df_predict.test_predict, label = 'Prediction of Test Data Set')
plt.title('Figure 22: line graph of the actual price comparison with the train and test data set predictions', fontsize=15)
plt.ylabel('Prices ($)')
plt.xlabel('Year')
plt.legend()
plt.grid(color='grey', linestyle='--')
plt.style.use("dark_background")
plt.show()

plt.figure(figsize=(10,5))
plt.plot(df_1.Close[-10:], label = 'Actual Price')
plt.plot(df_predict.test_predict[-10:], label = 'Prediction of Test Data Set')
plt.title('Figure 23: line graph of the actual price comparison with the train and test data set predictions of the last 10 days', fontsize=15)
plt.ylabel('Prices ($)')
plt.xlabel('Year')
plt.legend()
plt.grid(color='grey', linestyle='--')
plt.style.use("dark_background")
plt.show()


#Predict the price of next 30 days
x_input = test[(len(test)-100):].reshape(1,-1)
x_input.shape

temp_input = list(x_input)
temp_input = temp_input[0].tolist()

lst_output=[]
x = 0
while(x < 30):
    if(len(temp_input) > 100):
        x_input = np.array(temp_input[1:])
        print("{} day input {}".format(x,x_input))
        x_input = x_input.reshape(1,-1)
        x_input = x_input.reshape((1, time_step, 1))
        yhat = model.predict(x_input, verbose=0)
        print("{} day output {}".format(x,yhat))
        temp_input.extend(yhat[0].tolist())
        temp_input = temp_input[1:]
        lst_output.extend(yhat.tolist())
        x = x + 1
    else:
        x_input = x_input.reshape((1, time_step,1))
        yhat = model.predict(x_input, verbose=0)
        print(yhat[0])
        temp_input.extend(yhat[0].tolist())
        print(len(temp_input))
        lst_output.extend(yhat.tolist())
        x = x + 1

print(lst_output)


##Plotting
day_pred = [df.Date[len(df.Date)-1] + datetime.timedelta(days=1)]
for i in range(29):
    time = day_pred[-1] + datetime.timedelta(days=1)
    day_pred.append(time)

plt.figure(figsize=(10,5))
plt.plot(df_1.Close[len(df_close)-100:], label = 'Actual Price')
plt.plot(day_pred,norm.inverse_transform(lst_output), label = 'Prediction the Next 30 Days')
plt.title('Figure 24: line graph of the actual price with the next 30 days predictions', fontsize=15)
plt.ylabel('Prices ($)')
plt.xlabel('Year')
plt.legend()
plt.grid(color='grey', linestyle='--')
plt.style.use("dark_background")
plt.show()
