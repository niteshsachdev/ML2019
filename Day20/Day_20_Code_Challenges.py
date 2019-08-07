"""
Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat")

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
"""

#Importing Libraries
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas
dataset = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",sep='\s')

#prepare the data to train the model
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, -1].values 
ten_per_labels_mean=(np.mean(labels)*0.1)

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

#train the algo
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(features_train,labels_train)

labels_pred=regression.predict(features_test)
from sklearn import metrics
print(np.sqrt(metrics.mean_squared_error(labels_test, labels_pred)))

from sklearn.linear_model import Ridge
lm_ridge= Ridge()
lm_ridge.fit(features_train, labels_train)
print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(features_test,labels_test)*100,2))




"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score
"""

#Importing Libraries
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas
dataset = pd.read_csv('kc_house_data.csv')
dataset.isnull().any(axis=0)
dataset['sqft_above'] = dataset['sqft_above'].fillna(dataset['sqft_above'].mean())
dataset.isnull().any(axis=0)
features=dataset.drop(['id','date','price'], axis=1)
labels=dataset.loc[:,'price'].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

#train the algo
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(features_train,labels_train)

labels_pred=regression.predict(features_test)
print("Model Linear accuracy : ",regression.score(features_test, labels_test))

from sklearn import metrics
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  

#using Lasso (L1)
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
lm_lasso= Lasso()
lm_ridge= Ridge()

lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)

print ("RSquare Value for Simple Regresssion TEST data is-") 
print (np.round (regression.score(features_test,labels_test)*100,2))

print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lm_lasso.score(features_test,labels_test)*100,2))

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(features_test,labels_test)*100,2))

