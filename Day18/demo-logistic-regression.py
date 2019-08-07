#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:26:04 2019

@author: ajoyfern
"""
import matplotlib.pyplot as plt
import numpy as np

HOURS = [0.50,0.75,1.00,	1.25,1.50,1.75,2.00,2.25,2.50,2.75,3.00,3.25,3.50,3.75,4.00,	4.25,4.50,4.75,5.00,5.50]
PASS = [0,0,	0,0,0,0,1,0,	1,0,1,0,1,0,	1,1,1,1,1,1]

plt.scatter(HOURS, PASS)

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(np.array(HOURS).reshape(-1,1), np.array(PASS).reshape(-1,1)) 


#Visualize the best fit line
import matplotlib.pyplot as plt

# Visualising the  results
plt.scatter(HOURS, PASS, color = 'red')
plt.plot(HOURS, regressor.predict(np.array(HOURS).reshape(-1,1)), color = 'blue')
plt.title('Study Hours and Exam Score')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score: Marks')
plt.show()


