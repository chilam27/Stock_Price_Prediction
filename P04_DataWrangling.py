# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:53:04 2020

@author: Chi Lam
"""

#Import modules
import numpy as np
import yfinance as yf
import mplfinance as fplt
import random
random.seed(1)


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
def candle_stick(var):
    ind = df.Date[df[var] == 1].index.tolist()
    df.set_index('Date')
    lis = random.sample(ind, 3)
    
    for i in range(2):        
        df1 = df.iloc[lis[i]-10:lis[i]+10,:5]
        df1 = df1.set_index('Date')
        fplt.plot(df1, type = 'candle', title = 'doji candle ' + str(i+1), ylabel='Price ($)')

##Doji/ spinning top/ high wave
doji = []
for i in range(df.shape[0]):
    diff1 = abs(df.Open[i] - df.Close[i])
    if diff1 == 0:
        candle = 1
    else:
        candle = 0
    doji.append(candle)

df['doji_candle'] = doji
df.doji_candle.value_counts()

candle_stick('doji_candle')
    
#Shaved bottom
shaved_bottom = []
for i in range(df.shape[0]):
    if df.Close[i] == df.Low[i]:
        candle = 1
    else:
        candle = 0
    shaved_bottom.append(candle)
    
df['shaved_bottom'] = shaved_bottom
df.shaved_bottom.value_counts()

candle_stick('shaved_bottom')

#Shaved top
shaved_top = []
for i in range(df.shape[0]):
    if df.Open[i] == df.High[i]:
        candle = 1
    else:
        candle = 0
    shaved_top.append(candle)
    
df['shaved_top'] = shaved_top
df.shaved_top.value_counts()

candle_stick('shaved_top')

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

candle_stick('bull_marubozu')
candle_stick('bear_marubozu')

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

candle_stick('hammer_candle')

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

candle_stick('shooting_star')

##One white solider pattern
white_solider = []
for i in range(df.shape[0]):
    body = df.Close[i] - df.Open[i]
    if body > 0 and abs(body) >= (np.mean(average_body)*1.5) and df.Open[i] > df.Close[i-1] and df.Close[i] > df.Open[i-1]:
        candle = 1
    else:
        candle = 0
    white_solider.append(candle)

df['white_solider'] = white_solider
df.white_solider.value_counts()

candle_stick('white_solider')

##One black crow
black_crow = []
for i in range(df.shape[0]):
    body = df.Close[i] - df.Open[i]
    if body < 0 and abs(body) >= (np.mean(average_body)*1.5) and df.Open[0] < df.Close[i-1] and df.Close[i] < df.Open[i-1]:
        candle = 1
    else:
        candle = 0
    black_crow.append(candle)

df['black_crow'] = black_crow
df.black_crow.value_counts()

candle_stick('black_crow')

##Bullish engulfing pattern
bull_engulf = []
for i in range(df.shape[0]):
    body = df.Close[i] - df.Open[i]
    try:
        if body > 0 and df.Open[0] < df.Low[i-1] and df.Close[i] > df.High[i-1] and (df.Close[i-1] - df.Open[i-1]) < 0:
            candle = 1
        else:
            candle = 0
    except:
        candle = 0
    bull_engulf.append(candle)

df['bull_engulf'] = bull_engulf
df.bull_engulf.value_counts()

candle_stick('bull_engulf')

##Bearish engulfing pattern
bear_engulf = []
for i in range(df.shape[0]):
    body = df.Close[i] - df.Open[i]
    try:
        if body < 0 and df.Open[i] > df.High[i-1] and df.Close[i] < df.Low[i-1] and (df.Close[i-1] - df.Open[i-1]) > 0:
            candle = 1
        else:
            candle = 0
    except:
        candle = 0
    bear_engulf.append(candle)

df['bear_engulf'] = bear_engulf
df.bear_engulf.value_counts()

candle_stick('bear_engulf')

#Tweezer top
tweezer_top = []
for i in range(df.shape[0]):
    try:
        if df.High[i-1] == df.High[i]:
            candle = 1
        else:
            candle = 0
    except:
        candle = 0
    tweezer_top.append(candle)
    
df['tweezer_top'] = tweezer_top
df.tweezer_top.value_counts()

candle_stick('tweezer_top')

#Tweezer bottom
tweezer_bottom = []
for i in range(df.shape[0]):
    try:
        if df.Low[i-1] == df.Low[i]:
            candle = 1
        else:
            candle = 0
    except:
        candle = 0
    tweezer_bottom.append(candle)
    
df['tweezer_bottom'] = tweezer_bottom
df.tweezer_bottom.value_counts()

candle_stick('tweezer_bottom')

##Evening star reversal pattern
evening_star = []
for i in range(df.shape[0]):
    try:
        body = df.Close[i-2] - df.Open[i-2]
        body1 = df.Close[i-1] - df.Open[i-1]
        body2 = df.Close[i] - df.Open[i]
        if body > 0 and body1 < 0 and body2 < 0 and df.Low[i-1] > df.High[i-2] and df.High[i] < df.Open[i-1]:
            candle = 1
        else:
            candle = 0
    except:
        candle = 0
    evening_star.append(candle)
    
df['evening_star'] = evening_star
df.evening_star.value_counts()

candle_stick('evening_star')

##Morning star reversal pattern
morning_star = []
for i in range(df.shape[0]):
    try:
        body = df.Close[i-2] - df.Open[i-2]
        body1 = df.Close[i-1] - df.Open[i-1]
        body2 = df.Close[i] - df.Open[i]
        if body < 0 and body1 > 0 and body2 > 0 and df.Close[i-1] < df.Low[i-2] and df.High[i-1] < df.Open[i]:
            candle = 1
        else:
            candle = 0
    except:
        candle = 0
    morning_star.append(candle)
    
df['morning_star'] = morning_star
df.morning_star.value_counts()

candle_stick('morning_star')

##Exponential Moving average
exp20 = df.Close.ewm(20).mean()
exp105 = df.Close.ewm(105).mean()

df['exp20'] = exp20
df['exp105'] = exp105


#Export to csv file
df.to_csv('stock_cleaned.csv', index=False)
