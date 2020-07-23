# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:53:04 2020

@author: Chi Lam
"""

#Import modules
import yfinance as yf
from datetime import datetime
from time import mktime

#Read in data
tickerSymbol = 'MSFT'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')


#Data cleaning:
tickerData.info
tickerData.calendar
recommendation = tickerData.recommendations

tickerDf.reset_index(level=0, inplace = True) # Turn data frame index to column "Date"

del tickerDf['Stock Splits']


#Feature engineer
##Doji/ spinning top/ high wave


#Shaved bottom


#Shaved top


#Bullish marubozu candle


##Hammer candle


##Shooting star candle


##High wave candle


##Bullish engulfing pattern


##Bearish engulfing pattern


##Evening star reversal pattern


##Morning star reversal pattern


##One white solider pattern


##One black crow


