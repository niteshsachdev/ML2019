"""
Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
dataset=pd.read_csv("Foodtruck.csv")
features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,-1].values
#dataset.isnull().any(axis=0)
#plt.boxplot(dataset.values)
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 
labels_pred = regressor.predict(features_test) 
df = pd.DataFrame({'Actual': labels_test, 'Predicted': labels_pred})  
#print(df)
pop=float(input("Enter the Population of city "))
pop=np.array(pop).reshape(1,-1)
print("Pridicted Profit : ",regressor.predict(pop))



"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""


import pandas as pd
import numpy as np
dataset=pd.read_csv("Bahubali2_vs_Dangal.csv")
features=dataset.iloc[:,:1].values
labels=dataset.iloc[:,1:].values
#dataset.isnull().any(axis=0)
#plt.boxplot(dataset.values)
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels)
print(regressor.intercept_)  
print (regressor.coef_)
print(regressor.predict(np.array(10).reshape(1,-1)))