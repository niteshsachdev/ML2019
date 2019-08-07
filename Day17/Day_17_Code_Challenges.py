"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.
"""
#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#load dataset
dataset=pd.read_csv("Female_Stats.csv")
#seprate lables and features
features=dataset.iloc[:,1:].values
labels=dataset.iloc[:,0].values
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features, labels)
dataset.isnull().any(axis=0)   #for check any values is null or not
#statices library for checking p(probiblity) values
#if any features have more p value then it's less dependent feature on prediction
import statsmodels.api as sm
feature=sm.add_constant(features) # adding constant features 
# we do not use constant feature in sklearn because it internally manage constant but OLS does not
feature_opt=feature[:,[0,1,2]]
regressor_OLS=sm.OLS(endog=labels,exog=feature_opt).fit()
regressor_OLS.summary()
print("children height depend on both mom and dad")
# second part
#When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
print ("main coef : ",regressor.coef_)
child_avg=labels.mean()
dataset['mom_inc']=dataset['momheight']+1
features=dataset.iloc[:,2:]
Pred = regressor.predict(features)
child_dad_const_avg=Pred.mean()
#third part
dataset['dad_inc']=dataset['dadheight']+1
features=dataset.iloc[:,1::3]
Pred = regressor.predict(features)
child_mom_const_avg=np.mean(Pred)


"""
Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("bluegills.csv")
features = dataset.iloc[:,0:1].values
labels = dataset.iloc[:, 1:2].values
#    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
#quadratic means 4 degree

from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)

from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 4)
features_poly = poly_object.fit_transform(features)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)

# Visualising the Linear Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_1.predict(features), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Year')
plt.ylabel('Claims Paid')
plt.show()
# Visualising the Polynomial Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Year')
plt.ylabel('Claims Paid')
plt.show()



#What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.


from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)
print("length of fish at age 5 year is : ",lin_reg_2.predict(poly_object.transform(np.array(5).reshape(1,-1))))









"""
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("iq_size.csv")
features = dataset.iloc[:,1:].values
labels = dataset.iloc[:, 0:1].values
#by polynomial 
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)
x=[90,70,150]
print("IQ of x=[90,70,150] by polynomial :",lin_reg_2.predict(poly_object.transform(np.array(x).reshape(1,-1))))
#print(lin_reg_2.intercept_)  
#print (lin_reg_2.coef_)
#by linear

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 
x=[90,70,150]
print("IQ of x=[90,70,150] by linear : ",regressor.predict(np.array(x).reshape(1,-1)))
#print(regressor.intercept_)  
#print (regressor.coef_)
s1=lin_reg_2.score(features_poly,labels)
s2=regressor.score(features,labels)
if s1>s2:
    print("polynomial Feature is Good")
else:
    print("Linear is Good")
