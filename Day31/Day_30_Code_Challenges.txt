Q1. Code Challenge

 Time Series using RNN with Keras
 This is Multivariate Time Series data.
 
 In this project, we will need to do Google stock prediction using time series. We will use Keras and Recurrent Neural Network(RNN).
 
 Donwnload the Google stock prices for past 5 years from https://www.nasdaq.com/symbol/goog/historical to a csv file Google2014to2019.csv

and import the basic libraries and read the data from the CSV file.

Take the average of the low and high of the Google stock for the day and volume of the stocks traded for the day as input features to predict the stock prices.

We will be creating the data that will go back to 50 business days in past for the prediction.

Also, we will take 30% of the latest data as our test dataset.

For RNN LSTM to predict the data we need to convert the input data.

Input data is in the form: [Volume of stocks traded, Average stock price] and we need to create a time series data.

The time series data for today should contain the [Volume of stocks traded, Average stock price] for past 50 days and the target variable will be Google’s stock price today and so on.


