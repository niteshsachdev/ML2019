
# Code Challenge 

# Find the mean, median, mode, and range for the following list of values:
# 13, 18, 13, 14, 13, 16, 14, 21, 13


#Answer : Mean = 15, Median = 14 , Mode = 13 , Range = 21 - 13 = 8



"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""


import numpy as np
sep_num = input("Enter 9 space separated numbers: ").split(" ")
numpy_array = np.array( sep_num ,int)
print ( np.reshape( numpy_array, (3,3) ) )


"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""

import numpy as np
from collections import Counter
random_array= np.random.randint( 5, 15, 40 )
frequency_counter = Counter( random_array )
frequent_value = frequency_counter.most_common()[0][0]
print ( "The most Frequent Number is",frequent_value )

"""
Code Challenge
  Name: 
    E-commerce Data Exploration
  Filename: 
    ecommerce.py
  Problem Statement:
      To create an array of random e-commerce data of total amount spent per transaction. 
      Segment this incomes data into 50 buckets (number of bars) and plot it as a histogram.
      Find the mean and median of this data using NumPy package.
      Add outliers 
          
  Hint:
      Execute the code snippet below.
      import numpy as np
      import matplotlib.pyplot as plt
      incomes = np.random.normal(100.0, 20.0, 10000)
      print (incomes)
 
    outlier is an observation that lies an abnormal distance from other values 
    
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 1000)
print (incomes)

plt.title("Before adding outliers")
plt.hist(incomes, bins=50)
plt.show()

mean = np.mean(incomes)
median= np.median(incomes)

outliers = np.random.randint(295,310,50)
incomes_outliers = np.append(incomes,outliers)

plt.title("After adding outliers")
plt.hist(incomes_outliers, bins=50)
plt.show()

mean_outliers = np.mean(incomes_outliers)
median_outliers = np.median(incomes_outliers)
print("Mean before adding outliers in incomes :"+str(round(mean,2)))
print("Median before adding outliers in incomes :"+str(round(median,2)))
print("Mean after adding outliers in incomes :"+str(round(mean_outliers,2)))
print("Median after adding outliers in incomes :"+str(round(median_outliers,2)))


"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""

import numpy as np
import matplotlib.pyplot as plt
num = np.random.normal(150, 20, 1000)
print(round(np.std(num)))
plt.hist(num, bins=100)
plt.show()


