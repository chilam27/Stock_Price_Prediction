# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:30:54 2020

@author: Chi Lam
"""

#Import module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf
%matplotlib inline


#Read in data
df = pd.read_csv('stock_cleaned.csv')

df['Date'] =  pd.to_datetime(df['Date'])
df = df.set_index('Date')


#Stock history
##Long-term trend
plt.figure(figsize=(10,5))
plt.plot(df.Close, label = 'Closing Price', color = 'white')
plt.plot(df.exp20, label = 'Exponential Moving Average 20', color = 'blue')
plt.plot(df.exp105, label = 'Exponential Moving Average 105', color = 'orange')
plt.title("Figure n: HSBC stock's long-term trend", fontsize=15)
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.grid(color='grey', linestyle='--')
plt.style.use("dark_background")
plt.legend()


##Short-term trend: starting from 2020-01-02
df1 = df.iloc[5149:]

plt.figure(figsize=(10,5))
plt.plot(df1.Close, label = 'Closing Price', color = 'white')
plt.plot(df1.exp20, label = 'Exponential Moving Average 20', color = 'blue')
plt.plot(df1.exp105, label = 'Exponential Moving Average 105', color = 'green')
plt.title("Figure n: HSBC stock's short-term trend", fontsize=15)
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.grid(color='grey', linestyle='--')
plt.style.use("dark_background")
plt.legend()

##Current trend: stock price history for the last 30 days
###Line chart
df2 = df.iloc[-30:]

plt.figure(figsize=(10,5))
plt.plot(df2.Close, label = 'Closing Price', color = 'white')
plt.plot(df2.exp20, label = 'Exponential Moving Average 20', color = 'blue')
plt.plot(df2.exp105, label = 'Exponential Moving Average 105', color = 'green')
plt.title("Figure n: HSBC stock's current trend", fontsize=15)
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.grid(color='grey', linestyle='--')
plt.style.use("dark_background")
plt.legend()

###Candlestick chart
mpf.plot(df2, type = 'candle', title = 'Candlestick Pattern on Daily Chart of the Last 30 Days', ylabel='Price ($)', volume = True)
plt.style.use("dark_background")


#Candles check
df_candle = df.iloc[:,7:20]
df_candle.apply(pd.Series.value_counts)


#Implement a simple trading plan
price_buy = []
price_sell = []
flag = -1

for i in range(len(df)):
    if df.exp20[i] > df.exp105[i]:
        if flag != 1:
            price_buy.append(df.Close[i])
            price_sell.append(np.nan)
            flag = 1
        else:
            price_buy.append(np.nan)
            price_sell.append(np.nan)
            
    elif df.exp20[i] < df.exp105[i]:
        if flag != 0:
            price_buy.append(np.nan)
            price_sell.append(df.Close[i])
            flag = 0
        else:
            price_buy.append(np.nan)
            price_sell.append(np.nan)
            
    else:
        price_buy.append(np.nan)
        price_sell.append(np.nan)

df['buy_price'] = price_buy
df['sell_price'] = price_sell

##Plotting
plt.figure(figsize=(10,5))
plt.plot(df.Close, label = 'Closing Price', color = 'white', alpha = 0.35)
plt.plot(df.exp20, label = 'Exponential Moving Average 20', color = 'blue', alpha = 0.35)
plt.plot(df.exp105, label = 'Exponential Moving Average 105', color = 'orange', alpha = 0.35)
plt.plot(df.buy_price, label = 'buying price', marker = '^', color = 'green')
plt.plot(df.sell_price, label = 'selling price', marker = 'v', color = 'red')
plt.title("Figure n: HSBC stock's long-term trend", fontsize=15)
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.grid(color='grey', linestyle='--')
plt.style.use("dark_background")
plt.legend()

