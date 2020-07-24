# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:53:04 2020

@author: Chi Lam
"""

#Import modules
import numpy as np
import yfinance as yf


#Read in data
tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
df = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')


#Data cleaning:
tickerData.info
tickerData.calendar
recommendation = tickerData.recommendations

df.reset_index(level=0, inplace = True) # Turn data frame index to column "Date"

del df['Stock Splits']


#Feature engineer
##Doji/ spinning top/ high wave
doji = []
for i in range(df.shape[0]):
    diff1 = abs(df.Open[i] - df.Close[i])
    diff2 = (df.High[i] - df.Low[i]) * 0.1
    if diff1 <= diff2:
        candle = 1
    else:
        candle = 0
    doji.append(candle)

df['doji_candle'] = doji
df.doji_candle.value_counts()

#Shaved bottom
shaved_bottom = []
for i in range(df.shape[0]):
    if df.Close[i] <= (df.Low[i] + 0.1):
        candle = 1
    else:
        candle = 0
    shaved_bottom.append(candle)
    
df['shaved_bottom'] = shaved_bottom
df.shaved_bottom.value_counts()

#Shaved top
shaved_top = []
for i in range(df.shape[0]):
    if df.Open[i] >= (df.High[i] - 0.1):
        candle = 1
    else:
        candle = 0
    shaved_top.append(candle)
    
df['shaved_top'] = shaved_top
df.shaved_top.value_counts()

#Bullish marubozu candle
average_body = []
bull_marubozu = []
bear_marubozu = []
for i in range(df.shape[0]):
    body = abs(df.Open[i] - df.Close[i])
    average_body.append(body)

for i in range(df.shape[0]):
    body = df.Close[i] - df.Open[i]
    if body > 0 and df.High[i] <= (df.Close[i] + (df.High[i] - df.Low[i])*0.1) and df.Low[i] <= (df.Open[i] + (df.High[i] - df.Low[i])*0.1) and abs(body) >= np.mean(average_body) * 1.5:
        bull = 1
    else:
        bull = 0
    bull_marubozu.append(bull)
    
for i in range(df.shape[0]):
    body = df.Close[i] - df.Open[i]
    if body < 0 and df.High[i] <= (df.Open[i] + (df.High[i] - df.Low[i])*0.1) and df.Low[i] >= (df.Close[i] - (df.High[i] - df.Low[i])*0.1) and abs(body) >= np.mean(average_body)*1.5:
        bear = 1
    else:
        bear = 0
    bear_marubozu.append(bear)

df['bull_marubozu'] = bull_marubozu
df['bear_marubozu'] = bear_marubozu
df.bull_marubozu.value_counts()
df.bear_marubozu.value_counts()

##Hammer candle
hammer = []
for i in range(df.shape[0]):
    if df.High[i] <= (df.Open[i] + (df.High[i] - df.Low[i])*0.1) and (df.Close[i] - df.Low[i]) > (abs(df.Close[i] - df.Open[i])*1.5):
        candle = 1
    else:
        candle = 0
    hammer.append(candle)

df['hammer_candle'] = hammer
df.hammer_candle.value_counts()

##Shooting star candle
shooting_star = []
for i in range(df.shape[0]):
    if (df.Low[i] + (df.High[i] - df.Low[i])*0.1) >= df.Close[i] and (df.High[i] - df.Open[i]) > (abs(df.Open[i] - df.Close[i])*1.5):
        candle = 1
    else:
        candle = 0
    shooting_star.append(candle)

df['shooting_star'] = shooting_star
df.shooting_star.value_counts()

##One white solider pattern


##One black crow


##Bullish engulfing pattern


##Bearish engulfing pattern


##Evening star reversal pattern


##Morning star reversal pattern


