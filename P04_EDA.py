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
plt.title("Figure 17: HSBC stock's long-term trend", fontsize=15)
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
plt.title("Figure 18: HSBC stock's short-term trend", fontsize=15)
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.grid(color='grey', linestyle='--')
plt.style.use("dark_background")
plt.legend()

##Current trend: stock price history for the last 30 days
###Line chart
df2 = df.iloc[-30:]
df2.replace(0, np.nan, inplace = True)

for x in range (8,23):
    for y in range(df2.shape[0]):
        if df2.iloc[y,x] == 1:
            df2.iloc[y,x] = df2.Close[y]

plt.figure(figsize=(10,5))
plt.plot(df2.Close, label = 'Closing Price', color = 'white')
plt.plot(df2.exp20, label = 'Exponential Moving Average 20', color = 'blue')
plt.plot(df2.exp105, label = 'Exponential Moving Average 105', color = 'green')
plt.plot(df2.doji_candle, label = 'Doji candle', marker = 'o', color = 'maroon')
plt.plot(df2.shaved_bottom, label = 'Shaved bottom candle', marker = 'o', color = 'tomato')
plt.plot(df2.shaved_top, label = 'Shaved top candle', marker = 'o', color = 'sienna')
plt.plot(df2.bull_marubozu, label = 'Bull marubozu candle', marker = 'o', color = 'darkseagreen')
plt.plot(df2.bear_marubozu, label = 'Bear marubozu candle', marker = 'o', color = 'darkolivegreen')
plt.plot(df2.hammer_candle, label = 'Hammer candle', marker = 'o', color = 'yellow')
plt.plot(df2.shooting_star, label = 'Shooting star pattern', marker = 'o', color = 'gold')
plt.plot(df2.white_soldier, label = 'White soldier pattern', marker = 'o', color = 'darkgoldenrod')
plt.plot(df2.black_crow, label = 'Black crow pattern', marker = 'o', color = 'darkorange')
plt.plot(df2.bull_engulf, label = 'Bull engulfing pattern', marker = 'o', color = 'turquoise')
plt.plot(df2.bear_engulf, label = 'Bear engulfing pattern', marker = 'o', color = 'teal')
plt.plot(df2.tweezer_top, label = 'Tweezer top pattern', marker = 'o', color = 'deepskyblue')
plt.plot(df2.tweezer_bottom, label = 'Tweezer bottom pattern', marker = 'o', color = 'slategray')
plt.plot(df2.evening_star, label = 'Evening star reversal pattern', marker = 'o', color = 'pink')
plt.plot(df2.morning_star, label = 'Morning star reversal pattern', marker = 'o', color = 'purple')
plt.title("Figure 19: HSBC stock's current trend", fontsize=15)
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.grid(color='grey', linestyle='--')
plt.style.use("dark_background")
plt.legend(bbox_to_anchor=(1, 1))

###Candlestick chart
plt.figure(figsize=(10,5))
mpf.plot(df.iloc[-30:], type = 'candle', title = 'Candlestick Pattern on Daily Chart of the Last 30 Days', ylabel='Price ($)', volume = True)


#Candles check
df_candle = df.iloc[:,8:20]
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
plt.title("Figure 20: HSBC stock's long-term trend", fontsize=15)
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.grid(color='grey', linestyle='--')
plt.style.use("dark_background")
plt.legend()
