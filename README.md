# Stock_Price_Prediction

Predicting HSBC Bank stock prices to make better buying/ selling decisions using an artificial recurrent neural network (RNN) architecture: _Long short-term memory (LSTM)_. In addition to using past prices for prediction, I applied some stock technical analysis that I learned to see if it can outperform the deep learning model.

## Table of Contents

* [Backgorund and Motivation](#backgorund-and-motivation)
* [Prerequisites](#prerequisites)
* [Project Outline](#project-outline)
  * [Data Wrangling](#data-wrangling)
  * [Exploratory Data Analysis](#eda)
  * [Model Building](#model-building)
  * [Overall Model Performance](#overall-model-performance)
* [Conclusion](#conclusion)
* [Author](#author)
* [Acknowledgments](#acknowledgments)

## Backgorund and Motivation

> "The greatest risks are never the ones you can see and measure, but the ones you can't see and therefore can never measure. The ones that seem so far outside the boundary of normal probability that you can't imagine they could happend in your lifetime--even though, of course, they do happen, more often than you care to realize" - Joe Nocera

Recently, I took an interest in learning about the stock market and how day trading works. That was very odd of me considering countless times I heard people say that you will end up losing money when trading the market. But funny how a random guy on YouTube convinced me by saying something along the line of losing trades and losing trades but with risk management are two different things, one will make you lose money and the other will make you a better trader. Then, the YouTube channel that I used to learn about the topic and bet my future financial decision on is called [_Real Life Trading_](https://www.youtube.com/channel/UCux4_ZudBYgiZBPDvxVdhVQ) by the guy mentioned above, Jerremy Alexandar Newsome. Although the channel seems gimmicky at first, Jerremy did an excellent job of simplifying how the market and all of its basic (at least for the introduction course I am taking). Getting further into the material, I started to learn about different indicators that predict the stock movement and the meaning of those indicators. I was surprised to hear that, as a trader using mostly technical analysis to trade stock as Jerremy himself, those indicators that he taught me are things he considered the most when making his stock decisions.

As an aspiring data scientist, I saw that stock technical analysis is simply using past data to predict future outcomes. Since many of the supervised learning algorithms function the same way, I decided to see if I could apply one of the algorithms to a history of stock prices and predict what the future prices will be. I chose to apply the _Long short-term memory (LSTM)_ algorithm to predict the stock prices. My goal for this project is to see how accurate can a machine predict the stock market and therefore answers the question of whether I can depend on the prediction to make my trading decision. Here are two things I would like to learn our of this project:

1. Create technical analysis indicators on Python
2. Learn how an artificial recurrent neural network (RNN), specifically LSTM, works

_Disclaimer: I am no way shape or form an expert in trading the stock market and would not recommend anyone to use this model to base their trading/ investing decision._

## Prerequisites

Python Version: 3.7.4

TensorFlow Version: 1.14.0

Packages: numpy, yfinance, mplfinance, random, pandas, matplotlib, seaborn, sklearn, tensorflow, datetime.

## Project Outline

1. Data Wrangling: I got stock price data of HSBC bank from a Python library called `yfinance` and created 18 additional indicators acted as variables based on the stock prices.

2. Exploratory Data Analysis (EDA): plotting three different plots showing: long-term trend, short-term trend, and current trend. I also created a candlestick chart using `mplfinance` library. Then, I implemented a simple trading plan only using moving averages and plotted it.

3. Model Building: first, I normalized the data and split them into train and test data set. Then, I built a stacked LSTM model and plot the prediction. Lastly, I did the same step as previously but try to predict the prices of the next 30 days and plot it. The performance metric I used for my model is the mean squared error.

### [Data Wrangling](https://github.com/chilam27/Stock_Price_Prediction/blob/master/P04_DataWrangling.py)



### [EDA](https://github.com/chilam27/Stock_Price_Prediction/blob/master/P04_EDA.py)



### [Model Building](https://github.com/chilam27/Stock_Price_Prediction/blob/master/P04_ModelBuilding.py)



### Overall Model Performance



## Conclusion



## Author

* **Chi Lam**, _student_ at Michigan State University - [chilam27](https://github.com/chilam27)

## Acknowledgments

[Ganegedara, T. (2020, January 1). (Tutorial) LSTM in Python: Stock Market Predictions.](https://www.datacamp.com/community/tutorials/lstm-python-stock-market)

[Kharkar, R. (2020, January 27). How to Get Stock Data Using Python.](https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75)

[Newsome, J. (n.d.). EVERYTHING YOU NEED TO KNOW ABOUT CANDLESTICKS [PDF].](https://dashboard.reallifetrading.com/assets/pdf/candlesticks.pdf)

[Singh, A. (2020, May 07). Stock Price Prediction Using Machine Learning: Deep Learning.](https://www.analyticsvidhya.com/blog/2018/10/predicting-stock-price-machine-learningnd-deep-learning-techniques-python/)

[Solanki, S. (2020, May 10). Candlestick Chart in Python (mplfinance, plotly, bokeh) by Sunny Solanki.](https://coderzcolumn.com/tutorials/data-science/candlestick-chart-in-python-mplfinance-plotly-bokeh)
