# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:53:04 2020

@author: Chi Lam
"""

#Import modules
import yfinance as yf


#Read in data
tickerSymbol = 'MSFT'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

tickerData.info

tickerData.calendar

recommendation = tickerData.recommendations
