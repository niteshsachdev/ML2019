"""
Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)
"""
import pandas as pd  
import numpy as np  
dataset = pd.read_csv("Auto_mpg.txt",sep='\s+', header=None)  
dataset.columns=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]
max_mpg=dataset[dataset['mpg']==max(dataset['mpg'])]
print(" {} has highest milage as {} ".format(list(max_mpg['car name']),int(max_mpg['mpg'])))
dataset=dataset.drop(['car name'],axis=1)
for i in dataset:
    #dataset[i] = dataset[i].replace('?',dataset[i].mode()[0])
    dataset[i] = dataset[i].replace('?',np.nan).astype(np.float64)
    dataset[i] = dataset[i].fillna(dataset[i].mean())
dataset.isnull().any(axis=0)

#using Decision Tree
features = dataset.drop(['mpg'], axis=1)  
labels = dataset['mpg'] 


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)
#df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
regressor.score(features_test, labels_test)


#using Random Forest

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test)  
regressor.score(features_test, labels_test)
print("So, RandomForest is best approach")


"""
Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.
"""

import pandas as pd  
import numpy as np  
dataset = pd.read_csv("PastHires.csv")  
features = dataset.iloc[:,:6].values
labels = dataset.loc[:,'Hired'].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 1] = labelencoder.fit_transform(features[:, 1])
features[:, 3] = labelencoder.fit_transform(features[:, 3])
features[:, 4] = labelencoder.fit_transform(features[:, 4])
features[:, 5] = labelencoder.fit_transform(features[:, 5])
labels=labelencoder.transform(labels)

from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features, labels)

labels_pred = classifier.predict(features) 
classifier.score(features, labels)

#using Random Forest

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier.fit(features, labels)  
labels_pred = classifier.predict(features)
classifier.score(features, labels)
#currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
x1=np.array([10,'Y',4,'BS','Y','N'])
#unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.
x2=np.array([10,'N',4,'MS','N','Y'])
x1=labelencoder.fit_transform(x1)
x2=labelencoder.fit_transform(x2)
x1_pred=classifier.predict(x1.reshape(1,-1))
x2_pred=classifier.predict(x2.reshape(1,-1))