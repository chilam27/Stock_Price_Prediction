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

1. Data Wrangling: I got stock price data of HSBC bank from a Python library called `yfinance` and created 18 additional indicators acted as variables based on the stock prices. All candlestick related knowledge that I used is based on Jerremy's ebook: ["EVERYTHING YOU NEED TO KNOW ABOUT CANDLESTICKS"](https://dashboard.reallifetrading.com/assets/pdf/candlesticks.pdf).
2. Exploratory Data Analysis (EDA): plotting three different plots showing: long-term trend, short-term trend, and current trend. I also created a candlestick chart using `mplfinance` library. Then, I implemented a simple trading plan only using moving averages and plotted it.
3. Model Building: first, I normalized the data and split them into train and test data set. Then, I built a stacked LSTM model and plot the prediction. Lastly, I did the same step as previously but try to predict the prices of the next 30 days and plot it. The performance metric I used for my model is the root mean square error (RMSE).

### [Data Wrangling](https://github.com/chilam27/Stock_Price_Prediction/blob/master/P04_DataWrangling.py)

- Through `yfinance` library, I got stock prices of ticker "HSBC" from May 12th, 1995 to July 27th, 2020.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f1.png">
</p>

- I turned the data frame index to a new column "Date".
- To prepare for candlesticks visualization, I created a function ("candle_stick") with the `mplfinance` library embedded. This function will return a maximum of two candlestick plots of the candlestick's pattern. For easy use, I made it so whatever the candlestick or pattern will be the candle(s) in the middle of the graph. Along with it will be ten extra days of data before and after the candlestick/ pattern happened.
- I created a list to get body sizes of every candle (the absolute value of the difference between the open and close price of the day). This became handy later on when I need to find the mean of body size.

Below are formulas that I used to create different candlesticks/ patterns and their plots:

_Please note that, in some way, candlestick can be seen as a form of art: meaning that there is no set in stone functions that define every candlesticks/ patterns. Functions I used for this project are very simple and straightforward._

- Doji candle: a candle without a body. Function: absolute value or the difference between the open and close price of the day equals zero.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f2.png">
</p>

- Shaved bottom: A candle without a lower wick. Function: the closing price equals the low price of the day.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f3.png">
</p>

- Shaved top: A candle without an upper wick. Function: the open price equals the high price of the day.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f4.png">
</p>

- Bullish marubozu candle: white shaved bottom and top candle with a size much larger than the average candle. Function: the difference between close and open price need to be positive and bigger than the average candle by 1.5 times, high equals close and low equals open price of the day.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f5.png">
</p>

- Bearish marubozu candle: black candle version of bullish marubozu candle. Function: the difference between close and open price need to be negative and bigger than the average candle by 1.5 times, high equals open and low equals close price of the day.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f6.png">
</p>

- Hammer candle:  the lower wick of the candle should be about two times the size of the candle body; the candle still has a body but no upper wick. Function: high equals open price of the day, the difference of the close and low price is bigger than the difference between close and open prices multiplies by 1.5 times.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f7.png">
</p>

- Shooting star candle: the inverted hammer candle. Function: low equals close price of the day, the difference between high and open price is bigger than the absolute value of the difference between open and close price multiplies by 1.5 times.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f8.png">
</p>

- One white soldier pattern: the open of a white candle has to be above the close of the previous day black candle and The close of the white candle has to be above the open of the previous day candle. Function: the difference between close and open price needs to be positive and bigger than the average candle by 1.5 times, open of the candle needs to be bigger than the close price of previous candle and close of the candle needs to be bigger than the open price of the previous candle.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f9.png">
</p>

- One black crow: the open of a black candle has to be below the close of the previous day and the close of the black candle has to be below the open of the previous day. Function: the difference between close and open price needs to be negative and its absolute value needs to be bigger than average candle by 1.5 times, open of the candle needs to be smaller than the close price of previous candle and close of the candle needs to be smaller than the open price of the previous candle.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f10.png">
</p>

- Bullish engulfing pattern: the open of a white candle must be below the low of the previous black candle and the close of the white candle must be above the high of the previous candle. Function: the difference between close and open price needs to be positive, the open is smaller than the low price of the previous candle, the close is bigger than the high price of the previous candle, and the difference of close and open price of previous day needs to be negative.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f11.png">
</p>

- Bearish engulfing pattern: the open of a black candle must be above the high of the previous white candle and the close of the black candle must be below the low of the previous candle. Function: the difference between close and open price needs to be negative, the open is bigger than the low price of the previous candle, the close is smaller than the high price of the previous candle, and the difference of close and open price of previous day needs to be positive.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f12.png">
</p>

- Tweezer top: a white candle follows by a black one with an equally high price. Function: high equals the high price of the previous day, the difference of close and open price needs to be negative and the difference of close and open price of previous day candle needs to be positive.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f13.png">
</p>

- Tweezer bottom: a white candle follows by a black one with an equally high price. Function: high equals the high price of the previous day, the difference of close and open price needs to be positive and the difference of close and open price of previous day candle needs to be negative.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f14.png">
</p>

- Evening star reversal pattern: a white candle follows by two black candles. The low price of the previous day candle is bigger than the high of the second previous day candle. The high price is smaller than the open of previous day candle. Function: the difference of close and open of the second previous day candle needs to be positive, for the previous and current day needs to be negative. The low of previous day is smaller than high of second previous, high is smaller than open price of previous day.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f15.png">
</p>

- Morning star reversal pattern: a black candle follows by two white candles. The close price of the previous day candle is smaller than the low of the second previous day candle. The high price of the previous day is smaller than the open price. Function: the difference of close and open of the second previous day candle needs to be negative, for the previous and current day needs to be positive. Close of the previous day is smaller than low of second previous, high of the previous day is smaller than open price.

<p align="center">
  <img width="800" height="400" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f16.png">
</p>

- Next, I created two different exponential moving averages: the 20 exponential moving average (moves slower) and the 50 exponential moving average (moves faster).

- The last variable that I included in the data frame is "percent_change", which calculates the percentage of change of the closing price.


### [EDA](https://github.com/chilam27/Stock_Price_Prediction/blob/master/P04_EDA.py)

- To determine whether the stock is good to buy, the first thing I needed to do is to look at the overall trend (long-term) of the stock price history. The line graph below shows that the overall trend of this stock is sideways, which is not bad because at least it is not going down. The stock had its highest price in 2007 at around $55 and fell rapidly at the end of 2008 to around $12 (probably due to the Great Recession happened in that period). From there, its pattern is quite predictable. Based on the graph, assume that there is not an event that causes a severe change to the market (like the current pandemic), the stock is very likely to bounce back up to the $38 price mark. I would be very interested in this particular stock if I am a trader compare to an investor.

<p align="center">
  <img width="900" height="500" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f17.png">
</p>

- Next, we will look at a closer picture: a short-term trend. I defined the short-term here as data starting from January 2nd, 2020 to July 27th, 2020. The line graph below shows that there is a downward trend (or a bearish trend), though it did platten out at the end. Many traders will look at this graph and go "Welp, that's it for this stock." But since I already looked at the bigger picture (long-term trend), I knew with a certain degree of confidence what the stock is going to do next. In another word, I will act differently from those traders. If I predicted the stock will go back up, this is a perfect time to buy the stock when the price is low. If the plan works out, the return will be incredible.

<p align="center">
  <img width="900" height="500" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f18.png">
</p>

- Since I knew what I should do with the stock, then the next challenge is to figure out where to enter the trade. Based on the course I took from Jerremy, I need to look for an indicator. A specific candlestick/ pattern that indicates the stock will go up (or go bullish). I created even a smaller picture, a line graph of stock price history for the last 30 days, to look out for details. Since I couldn't add markers on to the candlestick graph, I labelled it in the line graph below with a different colors' marker to spot the special candlestick/ pattern. In the line graph, there were a couple of candlesticks/ patterns appeared in the last 30 days: shaved bottom candles, white soldier pattern, bull engulfing pattern, and evening star reversal pattern. Beside the fact that those candlessticks/ patterns did not affect the trend much, there wasn't any indicator coming up in the past week, I should be patient and wait for now.

<p align="center">
  <img width="900" height="500" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f19.png">
</p>

- This last step is additional visualization that can be improved later on: I created a simple trading plan and graph it on the line graph. This plan only involves two exponential moving averages: if the 20 exponential moving average is above the 50, buy the stock; sell the stock if it is reversed. I used the interceptions of those two lines as indicators of where I should buy/ sell the stock.

<p align="center">
  <img width="900" height="500" src="https://github.com/chilam27/Stock_Price_Prediction/blob/master/readme_image/f20.png">
</p>

### [Model Building](https://github.com/chilam27/Stock_Price_Prediction/blob/master/P04_ModelBuilding.py)

For this part of my project, I wanted to give the credit to Krish Natik for his "[Stock Price Prediction And Forecasting Using Stacked LSTM- Deep Learning](https://www.youtube.com/watch?v=H6du_pfuznE)" video on YouTube that helped me to understand the importance of each step in building a stacked LSTM algorithm. I also used the same structure as his in the video.

- For the LSTM algorithm, the only variable that I will be using is the "Close" price. Because the algorithm is very sensitive to the scale of the data, the first thing I needed to do is to scale the data into numbers between 0 and 1 using `MinMaxScalar`.
- To split the "Close" price data into train and test set, because this is a time series data, I will split the first 70% of the data to use it as my training data set and use the last 30% as my testing sata set.
- Next, I implemented a function that performs data preprocessing and converting data array into matrix to the train and test data set with time step of 100.
- Before building the model, I shaped my "X_train" and "X_test" data set because the LSTM model requires the input data to be reshaped to a three dimension as following: samples, time steps, features.
- Then comes the model building. As for this stacked LSTM model (an extension of LSTM model with multiple hiddern layers), I used the "Sequential" model with an addtional of four layers:

```python
model = Sequential()
model.add(LSTM(50, return_sequences = True, input_shape = (100,1)))
model.add(LSTM(50, return_sequences = True))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer = 'adam')
```


### Overall Model Performance

- After I applied the input data set into the model, I took the prediction from the model and reshaped it back to the original form and find the RMSE of the test and train data set. 

.                     | Train Data Set   | Test Data Set
:--------------------:|:----------------:|:--------------------------------:
Root Mean Square Error| 32.3823361526875 | 34.503165661139754

## Conclusion



## Author

* **Chi Lam**, _student_ at Michigan State University - [chilam27](https://github.com/chilam27)

## Acknowledgments

[Ganegedara, T. (2020, January 1). (Tutorial) LSTM in Python: Stock Market Predictions.](https://www.datacamp.com/community/tutorials/lstm-python-stock-market)

[Kharkar, R. (2020, January 27). How to Get Stock Data Using Python.](https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75)

[Newsome, J. (n.d.). EVERYTHING YOU NEED TO KNOW ABOUT CANDLESTICKS [PDF].](https://dashboard.reallifetrading.com/assets/pdf/candlesticks.pdf)

[Singh, A. (2020, May 07). Stock Price Prediction Using Machine Learning: Deep Learning.](https://www.analyticsvidhya.com/blog/2018/10/predicting-stock-price-machine-learningnd-deep-learning-techniques-python/)

[Solanki, S. (2020, May 10). Candlestick Chart in Python (mplfinance, plotly, bokeh) by Sunny Solanki.](https://coderzcolumn.com/tutorials/data-science/candlestick-chart-in-python-mplfinance-plotly-bokeh)
