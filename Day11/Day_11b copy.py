"""
"Data science" is just about as broad of a term as they come. 
It may be easiest to describe what it is by listing its more concrete components:
    
Data Exploration & Analysis (EDA):

    Included here: Pandas; NumPy; SciPy; 
    
Data visualization: 
    A pretty self-explanatory name. 
    Taking data and turning it into something colorful.

    Included here: Matplotlib; Seaborn; Datashader; others.

Classical Machine Learning: 
    Conceptually, we could define this as any supervised or unsupervised learning 
    task that is not deep learning. 
    Scikit-learn is far-and-away the go-to tool for implementing classification, 
    regression, clustering, and dimensionality reduction, 

    Included here: Scikit-Learn, StatsModels.


Deep learning. 
    This is a subset of machine learning that is seeing a renaissance, 
    and is commonly implemented with Keras, among other libraries. 
    It has seen monumental improvements over the last ~5 years, such as AlexNet in 2012, 
    which was the first design to incorporate consecutive convolutional layers.

    Included here: Keras, TensorFlow, and a whole host of others.


Reinforcement Learning
    

Data storage and big data frameworks. 
    Big data is best defined as data that is either literally too large to 
    reside on a single machine, 
    or can’t be processed in the absence of a distributed environment. 
    The Python bindings to Apache technologies play heavily here.

    Apache Spark; Apache Hadoop; HDFS; Dask; h5py/pytables.


Odds and ends. 
    Includes subtopics such as Natural Language Processing, 
    and Image Manipulation with libraries such as OpenCV.

    Included here: nltk; Spacy; OpenCV/cv2; scikit-image; Cython.

Deployment of Machine Learning Models
    AWS
    Dockers
    API
    Web ( HTML, CSS and JS )


"""


"""
Introduce the concept of Scalar, Vectors and Tensors 
(Scalar_Vector_Tensor)

Scalar = When we want to store 1 piece of information ( value ) for a given physical quantity.
E.g. = Temperature and Pressure

Scalar has one component
Scalar is tensor of rank zero

Vector = When we want to store 2 piece of information ( value and direction ) 
for a given physical quantity.
E.g. = Position, Force and Velocity

v = v1*x + v2*y + v3z
[v1 v2 v3 ] as an array 

or 
as an columnar
[ v1 ]
[ v2 ]
[ v3 ]


Vector has three component
Vector is a Tensor of rank one, one basis vector per component

Tensor = When we want to store 3 piece of information 
( value and direction and plane ) for a given physical quantity.
E.g. = stress , forces in side an object    
[v11  v12  v13 ]
[v21  v22  v23 ]
[v31  v32  v33 ]


Tensor has nine component
Tensor is tensor of rank two


If the rank is three then the components are 27


Scalar          Vector              Tensor
Temp            Velocity            Stress
Value           Value/Direction     Value/Direction/Plane
1 comp          3 Component         9 Component
Rank zero       Rank One            Rank Two

"""



"""
Difference between LIST and ARRAY 

Every array has one and only one dtype. 
All items in it should be of that dtype.

Once an array is created, you cannot change its size. 

You will have to create a new array or overwrite the existing one.

An equivalent numpy array occupies much less space than a python list of lists.

Arrays support VECTORIZED operations, while lists don’t.

Arrays are the main data structure used in machine learning.

In Python, arrays from the NumPy library, called N-dimensional arrays or the ndarray, 
are used as the primary data structure for representing data.

"""

# NumPy == Numerical Python
# library consisting of multidimensional array objects 
# and a collection of routines for processing those arrays. 

# Mathematical and logical operations on arrays.
# Fourier transforms and routines for shape manipulation
# NumPy has in-built functions for linear algebra and random number generation.


# NumPy – A Replacement for MatLab
# NumPy is often used along with packages like SciPy (Scientific Python) and 
# Matplotlib (plotting library).

# pip install numpy 


# N-dimensional array type called ndarray.
# It describes the collection of items of the same type. 
# Items in the collection can be accessed using a zero-based index.
# Any item extracted from ndarray object (by slicing)
# is represented by a Python object of one of array scalar types.


"""
Important concepts
1. Array Creation
2. Array Indexing
3. Array Slicing
4. Array Reshaping
"""


"""
There are a couple of mechanisms for creating arrays in NumPy:
 a. Conversion from other Python structures (e.g., lists, tuples).
 b. Built-in NumPy array creation (e.g., arange, ones, zeros, etc.).
 c. Reading arrays from disk, either from standard or custom formats 
     (e.g. reading in from a CSV file).
"""


"""
Convert your list data to NumPy arrays
"""

a = [0,1,2,3,4,5,6,7,8]
print (type(a))
print (a)  # it always prints the values WITH comma, that's list


import numpy as np

x = np.array( a ) 
print (type(x))

print (x)  # it always prints the values WITHOUT comma seperated , thats ndarray


"""
Explain the ndarray data Structure Image
NumPy_NDArray_Data_Structure.png
"""

# to print the data type of the elements of array 
print (x.dtype)


# to print the dimension of the array 
print (x.ndim)

# to print the shape of the array 
# returns a tuple listing the length of the array along each dimension
# For a 1D array, the shape would be (n,) 
# where n is the number of elements in your array.
print (x.shape)


# Shows bytes per element 
print (x.itemsize)

# reports the entire number of elements in an array
print(x.size)

# returns the number of bytes used by the data portion of the array
print (x.nbytes)  # size * itemsize  

print (x.strides)



"""
Array Indexing will always return the data type object 
"""
print (x[0])
print (x[2])
print (x[-1])



"""
Array Slicing will always return ndarray  

x[start:end] # items start through the end (but the end is not included!)
x[start:]    # items start through the rest of the array
X[:end]      # items from the beginning through the end (but the end is not included!)
"""


print (x[:])  # blank means from start or till end
print (x[0:]) 
print (x[:3]) 
print (x[0:2])
print (x[0:1])




"""
Reshaping is changing the arrangement of items so that shape of the array changes
Flattening, however, will convert a multi-dimensional array to a flat 1d array. 
And not any other shape.
"""

# Reshaping to 2 Dimensional Array - 3 Rows and 3 Columns
x = x.reshape(3,3)
print (x)


print (x.ndim)
print (x.shape)
print (x.strides)


# Due to reshaping .. none of the below has changed 
print (x.dtype)
print (x.itemsize)
print(x.size)
print (x.nbytes)


# Reshaping to 3 Dimensional Array -  3 layers of 3 Rows and 3 Columns 

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

#x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27\
#     ,28,29,30,31,32,33,34,35,36]

x = np.array(x)
print(x)

x = x.reshape(3,3,3)
x = x.reshape(4,3,3)

 
print (x)
print (x.ndim)
print (x.shape)

print (x.dtype)
print (x.itemsize)
print(x.size)
print (x.nbytes)

       

"""
For 1D array, shape return a  tuple with only 1 component (i.e. (n,))
For 2D array, shape return a  tuple with only 2 components (i.e. (n,m))
For 3D array, shape return a  tuple with only 3 components (i.e. (n,m,k) )
"""


"""
Creating 2 Dimensional Array 
"""
x = np.array( [ [1, 2, 3], [4, 5, 6] ] )
print (type(x))

print (x)
print (x.ndim)
print (x.shape)
print (x.dtype) 
# For 2D array, return a shape tuple with only 2 elements (i.e. (n,m))



# Array Indexing 
print (x)

print (x[0])
print (type(x[0]))

print (type(x[0,0]))
print (x[0,0])
print (x[0,1])
print (x[0,2])


print (x[1])
print (type(x[1]))

print (type(x[1,0]))
print (x[1,0])
print (x[1,1])
print (x[1,2])


"""
Introduce the visualisation of 1D, 2D and 3D using an image
(NumPy_3d_visualisation_NDArray.jpg)
"""

"""
Creating 3 Dimensional Array
"""

#x = np.array([ [ [1, 2, 3], [4, 5, 6]], [ [11, 22, 33], [44, 55, 66] ], [ [111, 222, 333], [444, 555, 666] ]  ] )
x = np.array([ [ [1, 2, 3], [4, 5, 6], [7,8,9] ], [ [11, 22, 33], [44, 55, 66], [77,88,99] ], [ [111, 222, 333], [444, 555, 666], [777,888,999] ]  ] )
print (x)

print (x.ndim)
print (x.shape)
print (x.dtype)
# For 3D array, return a shape tuple with only 3 elements (i.e. (k,n,m) )
# We introduced the concept of another layer represented by k


# Array Indexing 
print (x)
print (x[0])      # 0th Layer
print (x[0,0])    # 0th Layer and 0th Row
print (x[0,0,0])  # 0th Layer and 0th Row and 0th Column


# This part can be removed 
"""
Creating multi dimensional array 
"""

# One Dimensional Array 
x = np.array( [1,2,3], ndmin = 1 )  # ndmin = 1
print (type(x))
print (x)

print(x.strides)
print (x.ndim )
print (x.shape )
print (x.dtype )
print (x[0])
print (type(x[0]))
# If we access on the zeroth location we would get 1


# Two Dimensional Array with only one row of data
x = np.array( [1,2,3] , ndmin = 2) 
print (type(x))
print (x)

print(x.strides)
print (x.ndim)
print (x.shape)
print (x.dtype)

# If we access on the zeroth location we would get the 1D array [1 2 3]
print (x[0])
print (type(x[0]))
print (x[0][0])
print (x[0,0])
print (type(x[0][0]))


# Three Dimensional Array with only one row of data 
x = np.array( [1,2,3] , ndmin = 3) 
print (type(x))
print (x)

print(x.strides) # (24, 24, 8)
print (x.ndim)
print (x.shape)
print (x.dtype)
# If we access on the zeroth location we would get 2D array [[1 2 3]]
print (x[0])
print (type(x[0]))
print (x[0][0])
print (type(x[0][0]))
print(x[0][0][0])
print (type(x[0][0][0]))


"""
Array         Dimen     Shape
[1 2 3]         1       (3,)

[[1 2 3]]       2       (1,3)

[[[1 2 3]]]     3       (1,1,3)

"""


# Numpy supports all data types likes bool, integer, float, complex etc.
# They are defined by the numpy.dtype class 

import numpy as np 

x = np.float32(1.0) 
print (x) 
print (type(x)) 
 

x = np.float64(1.0)
print (x) 
print (type(x)) 
 

x = np.int_([1,2,4]) 
print ( x )
print (type(x)) 
 

x = np.array([1, 2, 3], dtype = complex) 
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)
print (x.strides)

print (x.itemsize)
print(x.size)
print (x.nbytes) # size * itemsize  





"""
Using the built in function arange 
"""

# Arange function will generate array from 0 to size-1 
# arange is similar to range function but generates an array , 
# where in range gives you a list of elements

import numpy as np 

x = np.arange(20, dtype=np.uint8)
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)
print (x.itemsize)

# zeros(shape) -- creates an array filled with 0 values with the specified shape.
# The default dtype is float64.

x = np.zeros((3, ))
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)
print (x.itemsize)


x = np.zeros((3, 3))
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)


x = np.zeros((4, 3, 3))
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)




# ones(shape) -- creates an array filled with 1 values. 

import numpy as np 
x = np.ones((3, ), dtype=np.int8 )
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)
print (x.itemsize)

x = np.ones((3, 3), dtype=np.int8 )
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)


x = np.ones((3, 3, 3), dtype=np.int8 )
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)


# linspace() -- creates arrays with a specified number of elements, 
# and spaced equally between the specified beginning and end values.

import numpy as np 
x = np.linspace(1, 4, 10, dtype = np.float) # try with float16,float32,float64
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)
print (x.itemsize)


import numpy as np 
#random.random(shape) – creates arrays with random floats over the interval [0,1].
x = np.random.random((2,3))*100
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)


# np.identity() to create a square 2d array with 1's across the diagonal
print (np.identity(n = 5))      # Size of the array



# np.eye() to create a 2d array with 1's across a specified diagonal
np.eye(N = 3,  # Number of rows
       M = 5,  # Number of columns
       k = 1)  # Index of the diagonal (main diagonal (0) is default)



"""
NaN and Infinite Value 
"""

# NaN can be defined using the following constant
print (np.nan)
print(type(np.nan))
# Infinite value can be expressed using the following contant 
print (np.inf)
print(type(np.inf))


x = np.array( [1,2,3], dtype=np.float ) 
print (x)
print(x.dtype)


x[0] = np.nan
x[2] = np.inf
print (x)

print (np.isnan(x[0]))
print(np.isnan(x))

print (np.isinf(x[2]))
print(np.isinf(x))


"""
# Replace nan and inf with -1. 
Don't use arr2 == np.nan
"""
missing_bool = np.isnan(x) | np.isinf(x)
print (missing_bool)

x[missing_bool] = -1  
print (x)



"""
Arrays Operations - Basic operations apply element-wise. 
The result is a new array with the resultant elements.
Operations like *= and += will modify the existing array.
"""

import numpy as np
a = np.arange(5) 
print (a)

b = np.arange(5) 
print(b)

x= np.array(list(zip(a,b)))
print (x) 
print (x.ndim)
print (x.shape)
print (x.dtype)

x = a + b
print (x) 

x = a - b
print (x)

x = a**3
print (x)
 
x = a>3
print (x)
 
x= 10*np.sin(a)
print (x) 

x = a*b
print (x)


"""
Basic Functions         
"""

import numpy as np 

x = np.array( [1,2,3] , ndmin = 1) 
print (type(x))
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)


print("Sum is: ", x.sum())
print("Average/Mean value is: ", x.mean())
print("Max value is: ", x.max())
print("Min value is: ", x.min())


#print("Median value is: ", np.median(x))
#print("Correlation coefficient value is: ", np.corrcoef(x))
#print("Standard Deviation is: ", np.std(x))


import numpy as np 

x = np.array( [[1,2,3],[4,5,6]]) 
print (type(x))
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)


print("Sum is: ", x.sum())
print("Average/Mean value is: ", x.mean())
print("Max value is: ", x.max())
print("Min value is: ", x.min())


#print("Median value is: ", np.median(x))
#print("Correlation coefficient value is: ", np.corrcoef(x))
#print("Standard Deviation is: ", np.std(x))


# Row wise min
print("Row wise minimum: ", np.amin(x, axis=0))
print("Row wise maximum: ", np.amax(x, axis=0))


# Column wise min
print("Column wise minimum: ", np.amin(x, axis=1))
print("Column wise maximum: ", np.amax(x, axis=1))



"""
Other Advanced Operations on NumPy  Arrays
"""

one_d_array = np.array([1,2,3,4,5,6])
print (one_d_array)

# Create a new 2d array
two_d_array = np.array([one_d_array, one_d_array + 6, one_d_array + 12])
print(two_d_array)

# Slice elements starting at row 2, and column 5
two_d_array[1:, 4:]

# Reverse both dimensions (180 degree rotation)
two_d_array[::-1, ::-1]


#Reshaping an Array
np.reshape(a=two_d_array,        # Array to reshape
           newshape=(6,3))       # Dimensions of the new array

#Unravel a multi-dimensional into 1 dimension with np.ravel():
np.ravel(a=two_d_array,
         order='C')         # Use C-style unraveling (by rows)

np.ravel(a=two_d_array,
         order='F')         # Use Fortran-style unraveling (by columns)


#Alternatively, use ndarray.flatten() to flatten a multi-dimensional into 1 dimension and return a copy of the result:
two_d_array.flatten()


#Transpose of the array
two_d_array.T


#Flip an array vertically np.flipud(), upside down :
np.flipud(two_d_array)

  
#Flip an array horizontally with np.fliplr(), left to right:
np.fliplr(two_d_array)


#Rotate an array 90 degrees counter-clockwise with np.rot90():
np.rot90(two_d_array,
         k=2)             # Number of 90 degree rotations


#Shift elements in an array along a given dimension with np.roll():
np.roll(a= two_d_array,
        shift = 1,        # Shift elements 2 positions
        axis = 1)         # In each row

np.roll(a= two_d_array,
        shift = 2,        # Shift elements 2 positions
        axis = 0)         # In each columns

#Join arrays along an axis with np.concatenate():
array_to_join = np.array([[10,20,30],[40,50,60],[70,80,90]])

np.concatenate( (two_d_array,array_to_join),  # Arrays to join
               axis=1)                        # Axis to join upon


# Get the mean of all the elements in an array with np.mean()
np.mean(two_d_array)

# Provide an axis argument to get means across a dimension
np.mean(two_d_array,
        axis = 0)     # Get means of each row

# Get the standard deviation all the elements in an array with np.std()
np.std(two_d_array)


# Provide an axis argument to get standard deviations across a dimension
np.std(two_d_array,
        axis = 0)     # Get stdev for each column

# Sum the elements of an array across an axis with np.sum()
np.sum(two_d_array, 
       axis=1)        # Get the row sums

np.sum(two_d_array,
       axis=0)        # Get the column sums

# Take the square root of each element with np.sqrt()
np.sqrt(two_d_array)


# Take the dot product of two arrays with np.dot(). 
# This function performs an element-wise multiply and then a sum for 1-dimensional 
# arrays (vectors) and matrix multiplication for 2-dimensional arrays.
# Take the vector dot product of row 0 and row 1

np.dot(two_d_array[0,0:],  # Slice row 0
       two_d_array[1,0:])  # Slice row 1
 
#Linear Algebra functions are also available

# Matrices
A = np.mat('1.0 2.0; 3.0 4.0') 
print (A)
print (type(A)) 

print (A.T) # transpose 

X = np.mat('5.0 7.0') 
print(X)
Y = X.T
print (Y)
 
print (A*Y) # matrix multiplication 
print (A.I) # inverse 

print (np.linalg.solve(A, Y)) # solving linear equation 

#How to check for library version
import numpy as np
print (np.__version__)







"""
Color-image data for single image is typically stored in three dimensions. 
Each image is a three-dimensional array of (height, width, channels), 
where the channels are usually red, green, and blue (RGB) values. 
One 256x256 RGB images would have shape (256, 256, 3). 

(An extended representation is RGBA, where the A–alpha–denotes the level of opacity.)
One 256x256 ARGB images would have shape (256, 256, 4). 


Color-image data for multiple images is typically stored in four dimensions. 
A collection of images is then just (image_number, height, width, channels). 
One thousand 256x256 RGB images would have shape (1000, 256, 256, 3). 

"""
 

from skimage import io

photo = io.imread('hawa_mahal.jpg') 

print(type(photo))
print (photo.dtype)
print (photo.itemsize)
print (photo.size) # 147x220x3 = 97020
print (photo.nbytes)

print (photo.ndim)
# height = 147, width = 220 , RBG 
print (photo.shape) #(147, 220, 3)

print (photo)

print(photo[0]) # first layer
print(photo[146]) # Last layer

print(photo[146][0]) # 0th row for the last layer

print(photo[146][0][0]) # RED Component of 0th row for the last layer


import matplotlib.pyplot as plt
plt.imshow (photo)

# Reversed rows
plt.imshow(photo[::-1])

# Revered the columns so we got a mirrored image
plt.imshow(photo[:,::-1])

# Section of the photos
plt.imshow(photo[50:147, 150:220])

# halved the size of the image
plt.imshow(photo[::2,::2])

#import numpy as np
#photo_sin = np.sin(photo)
#photo_sin

"""
Statistics of the image using numpy array 
"""


import numpy as np
print (np.mean(photo))
print (np.std(photo))
print (np.var(photo))
print (np.min(photo))
print (np.max(photo))
print (np.argmin(photo)) # index value of the min
print (np.argmax(photo)) # index value of the max

                        # condition,True,False
photo_masked = np.where(photo>100, 255, 0)
plt.imshow(photo_masked)

# Converts landscape into portrait
plt.imshow(photo[:,:,0].T)


"""
Basics of Statistics for Machine Learning ( Data Exploration )

The major types of Data are:
    Numerical
        This represents some quantifiable thing that you can measure.
        the number of clothes bought by a customer on an eCommerce platform
    
    Categorical
        These are data that has no inherent numerical meaning, such as man, woman. 
        Or the state of birth of a group of people
        good ways to denote categorical values is through graphs.
        
    Ordinal
        This is the mixture of numerical and categorical data
        Ratings given by a customer as in 5 stars is better than 1 star

"""    

"""
# Mean, Median, Mode
# These are the measures of central tendency of a data set.


# Mean
# Mean is given by the total of the values of the samples divided by the number of samples

# x = [10,20,30,40,50]
# mean = (10+20+30+40+50)/5 = 30


# Median
# To calculate the median, sort the values and take the middle value. 
# Now, in case there are even number of values then 
# the average of the two middle values are taken as the median.

# x = [23, 40, 6, 74, 38, 1, 70]
# sorted_x = [1, 6, 23, 38, 40, 70, 74]
# Median = 38

# The advantage of the median over the mean is that median is less susceptible to outliers

# So, in situations where there is a high chance that there may be outliers present 
# in the data set, it is wiser to take the median instead of the mean.
# For example, to understand what is the per capita income of a country 


# Mode
# Mode represents the most common value in a data set.
# The mode is the number that is repeated more often than any other
# For example, a retailer may want to understand the mode of sizes purchased 
# so that he can set stocking labels optimally.
"""


"""
# Variance and Standard Deviation


Variance and Standard Deviation are essentially a measure 
of the spread of the data in the data set.

Variance is the average of the squared differences from the mean.
Standard deviation is the square root of the variance
 
    1. Calculate the mean
    2. Calculate the difference from the mean
    3. find the square of the differences 
    4. Variance is the Sum of the squares of the differences
    5. Standard deviation is the square root of the Variance

# observations = [23, 40, 6, 74, 38, 1, 70]
# mean = (23+40+6+74+38+1+70) / 7 = 252 /7 = 36
# difference_from_the_mean = [13, -4, 30, -38, -2, 35, -34]
# square_of_the_differences = [169, 16, 900, 1444, 4, 1225, 1156]
# variance = (169+16+900+1444+4+1225+1156)/7 = 4914/7 = 702
# standard deviation = square_root(702)= 26.49

# Standard deviation is an excellent way to identify outliers.
# Data points that lie more than one standard deviation from the mean can be considered unusual. 
# Data points that are more than two standard deviations away from the mean are not considered in analysis.
"""



"""
Mean, Median, Mode

Let's create some fake income data, centered around 27,000 
with a normal distribution and standard deviation of 15,000, with 10,000 data points. 
Then, compute the mean (average)

"""

import numpy as np
                          #mean, sd, total
incomes = np.random.normal(27000, 15000, 10000)
#loc=150, scale=20, size=1000

print (type(incomes))
print(incomes.size)
print (incomes)
print (len(incomes))
print (incomes.ndim)
print (incomes.shape)
print (incomes.dtype)

print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))


from scipy import stats
print("Mode value is: ", stats.mode(incomes)[0])
 

print("Minimum value is: ", np.min(incomes))
print("Maximum value is: ", np.max(incomes))
print("Standard Deviation is: ", np.std(incomes))
#print("Correlation coefficient value is: ", np.corrcoef(incomes))



#We can segment the income data into 50 buckets, and plot it as a histogram:
import matplotlib.pyplot as plt
plt.hist(incomes, 20)
plt.show()


#box and whisker plot to show distribution
#https://chartio.com/resources/tutorials/what-is-a-box-plot/
plt.boxplot(incomes)

# Explain NumPy_boxplot.png


print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))

#Adding Bill Gates into the mix. income inequality!(Outliers)
incomes = np.append(incomes, [10000000000])

#Median Remains Almost SAME
print("Median value is: ", np.median(incomes))

#Mean Changes distinctly
print("Mean value is: ", np.mean(incomes))

      
# Give an example for bincount function
num = np.bincount(incomes).argmax()





"""
Take this rest on Day 13
"""

# Explain the NumPy_Normal_Distribution.png
# https://www.mathsisfun.com/data/standard-normal-distribution.html

"""
Some of the properties of a standard normal distribution are mentioned below:

    The normal curve is symmetric about the mean and bell shaped.
    mean = median = mode is zero which is the centre of the curve.
    symmetry about the center
    50% of values less than the mean and 50% greater than the mean
    
    Approximately 68.26% of the data will be between -1 and +1 
    (i.e. within 1 standard deviation from the mean), 
    95.44% between -2 and +2 (within 2 SD from the mean) and 
    99.72% between -3 and 3 (within 3 SD from the mean)
    
    68 | 95 | 99.7 Rule
    
    Question 1:
    Suppose that IQ scores have a bell shaped distribution with a mean of 100
    and a standard deviation of 15.
    What percentage of people should have an IQ score between 85 and 115
    What percentage of people should have an IQ score between 70 and 130
    What percentage of people should have an IQ score more than 130
    A person with an IQ score greater than 145  is considered genius.
    Does empirical rule support this statement?
    
    
    Sigma_sd = 15
    Mu = 100
    x1 = 85 
    x2 = 115
    Z Score for x1  = (x1- Mu) / Sigma_sd
                    = 85 - 100 / 15 = -1.00
    
    Z Score for x2  = (x2- Mu) / Sigma_sd
                    = 115 - 100 / 15 = +1.00
    
    Refer now to the SD(Z) table to get .3413 



"""

"""
Example 1:

A town has 330,000 adults. Their heights are normally distributed with a 
mean of 175 cm and a variance of 100 cm 2 .
How many people would you expect to be taller than 205 cm?

The variance of the data set is given to be 100cm 2 . 
So, the standard deviation is √100 or 10 cm.

Now, 175+3(10)=205, so the number of people taller than 205 cm corresponds 
to the subset of data which lies more than 3 standard deviations above the mean.

The graph above shows that this represents about 0.15%of the data. 
However, this percentage is approximate, and in this case, we need more precision. 
The actual percentage, correct to 4 decimal places, is 0.1318%.

330,000×0.001318≈435

So, there will be about 435 people in the town taller than 205 cm. 
"""

"""
Example 2:

The life of a fully-charged cell phone battery is normally distributed with a 
mean of 14 hours with a standard deviation of 1 hour. 
What is the probability that a battery lasts at least 13 hours?

The mean is 14 and the standard deviation is 1.

50% of the normal distribution lies to the right of the mean, so 50% of the time, 
the battery will last longer than 14 hours.

The interval from 13 to 14 hours represents one standard deviation to the left 
of the mean. 
So, about 34% of time, the battery will last between 13 and 14 hours.

Therefore, the probability that the battery lasts at least 13 hours is about 34%+50% or 0.84 . 
"""

"""
Example 3:

The average weight of a raspberry is 4.4 gm with a standard deviation of 1.3 gm. 
What is the probability that a randomly selected raspberry would weigh at 
least 3.1 gm but not more than 7.0 gm?

The mean is 4.4 and the standard deviation is 1.3.

Note that

4.4−1.3=3.1

and

4.4+2(1.3)=7.0

So, the interval 3.1≤x≤7.0 is actually between one standard deviation below the mean 
and 2 standard deviations above the mean.

In normally distributed data, about 34% of the values lie between the mean 
and one standard deviation below the mean, and 34% between the mean and 
one standard deviation above the mean.

In addition, 13.5% of the values lie between the first 
and second standard deviations above the mean.

Adding the areas, we get 34%+34%+13.5%=81.5%.

Therefore, the probability that a randomly selected raspberry will weigh at least 3.1
gm but not more than 7.0 gm is 81.5% or 0.815 . 

"""



"""
import numpy as np
import scipy.stats as stats
import pylab as pl

h = sorted([186, 176, 158, 180, 186, 168, 168, 164, 178, 170, 189, 195, 172,
     187, 180, 186, 185, 168, 179, 178, 183, 179, 170, 175, 186, 159,
     161, 178, 175, 185, 175, 162, 173, 172, 177, 175, 172, 177, 180])  #sorted

# Probability Density Function
fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed

pl.plot(h,fit,'-o')

pl.hist(h,normed=True)      #use this to draw histogram of your data

pl.show()                   #use may also need add this 

"""





"""
# percentiles and moments

# When a value is given x percentile, 
# this means that x percentage of values in the distribution is below that value


# Moments try to measure the shape of the probability distribution function.
# The zeroth moment is the total probability of the distribution which is 1.

# The first moment is the mean.
# The second moment is the variance
# The third moment is the skew which measures how lopsided the distribution is.
# The fourth moment is kurtosis which is the measure of how sharp is the peak of the graph.

# x = [1,2,6,7]
# first_moment = (1 + 2 + 6 + 7)/ 4 = 16/4 = 4
# sec_moment = (1 + 4 + 36 + 49) / 4 = 90/4 = 22.5
# third_moment = ( 1 + 8 + 216 + 343)/4 = 568/4 = 142

"""

"""
# Covariance and Corelation
# Covariance and Correlation are the tools that we have to measure 
# if the two attributes are related to each other or not.

# Covariance measures how two variables vary in tandem to their means.
# Correlation also measures how two variables move with respect to each other

# A perfect positive correlation means that the correlation coefficient is 1. 
# A perfect negative correlation means that the correlation coefficient is -1. 
# A correlation coefficient of 0 means that the two variables are independent of each other.

# Both correlation and covariance only measure the linear relationship between data.

# Correlation is a special case of covariance when the data is standardized.

"""

"""
#Probability and Statistics

# We use a lot of probability concepts in statistics and hence in machine learning, 
# they are like using the same methodologies. 

#In probability, the model is given and we need to predict the data. 
# While in statistics we start with the data and predict the model. 

#We look at probability and search from data distributions which closely match 
# the data distribution that we have. 

#Then we assume that the function or the model must be the same as the one we 
# looked into in probability theory.


# Conditional Probability and Bayes Theorem
"""







"""
Color-image data for single image is typically stored in three dimensions. 
Each image is a three-dimensional array of (height, width, channels), 
where the channels are usually red, green, and blue (RGB) values. 
One 256x256 RGB images would have shape (256, 256, 3). 

(An extended representation is RGBA, where the A–alpha–denotes the level of opacity.)
One 256x256 ARGB images would have shape (256, 256, 4). 


Color-image data for multiple images is typically stored in four dimensions. 
A collection of images is then just (image_number, height, width, channels). 
One thousand 256x256 RGB images would have shape (1000, 256, 256, 3). 

"""
 

from skimage import io

photo = io.imread('hawa_mahal.jpg') 

print(type(photo))
print (photo.dtype)
print (photo.itemsize)
print (photo.size) # 147x220x3 = 97020
print (photo.nbytes)

print (photo.ndim)
# height = 147, width = 220 , RBG 
print (photo.shape) #(147, 220, 3)

print (photo)

print(photo[0]) # first layer
print(photo[146]) # Last layer

print(photo[146][0]) # 0th row for the last layer

print(photo[146][0][0]) # RED Component of 0th row for the last layer


import matplotlib.pyplot as plt
plt.imshow (photo)

# Reversed rows
plt.imshow(photo[::-1])

# Revered the columns so we got a mirrored image
plt.imshow(photo[:,::-1])

# Section of the photos
plt.imshow(photo[50:147, 150:220])

# halved the size of the image
plt.imshow(photo[::2,::2])

#import numpy as np
#photo_sin = np.sin(photo)
#photo_sin

"""
Statistics of the image using numpy array 
"""


import numpy as np
print (np.mean(photo))
print (np.std(photo))
print (np.var(photo))
print (np.min(photo))
print (np.max(photo))
print (np.argmin(photo)) # index value of the min
print (np.argmax(photo)) # index value of the max

                        # condition,True,False
photo_masked = np.where(photo>100, 255, 0)
plt.imshow(photo_masked)

# Converts landscape into portrait
plt.imshow(photo[:,:,0].T)



"""
3-channel RGB PIL Image to 3D NumPy array and back 
"""

from PIL import Image
import numpy as np

#Import an image
image = Image.open('hawa_mahal.jpg')

image
print(type(image))

arr = np.array(image)
 
arr
print(type(arr))


# Convert array to Image
img = Image.fromarray(arr)

img


# convert into gray-scale:
im = image.convert('L')

im



"""
Learn how to use numpy to store and manipulate image data
use PIL to create (and display) an image
"""

from PIL import Image
import numpy as np

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[256, 256] = [255, 0, 0]
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()

#from matplotlib import pyplot as plt
#plt.imshow(data, interpolation='nearest')
#plt.show()



"""
Create an image from array 
"""

import numpy as np
import matplotlib.pyplot as plt
     
# Generate random array
width, height = 16,16
iMat = np.random.rand(width*height).reshape((width,height))
iMat
print(type(iMat))
print(iMat.ndim)
print(iMat.shape)


# Show it!
plt.imshow(iMat,'gray')
plt.show() 

# Save it
img = Image.fromarray(iMat, 'L') # RGB for color images 
img.save('rgb.png')
img.show()
    


# http://www.pythoninformer.com/python-libraries/numpy/numpy-and-images/

import numpy as np
width = 5 
height = 4

# data is ordered by lines, then each line is ordered by pixels, 
# and finally each pixel contains 3 byte values for RGB
#  Each colour is represented by an unsigned byte (numpy type uint8)

array = np.zeros([height, width, 3], dtype=np.uint8)

# Fill the array with orange pixels (red=255, green=128, blue=0)
array[:,:] = [255, 128, 0]


from PIL import Image
img = Image.fromarray(array) 
img.save('testrgb.png')
img.show()


array = np.zeros([100, 200, 3], dtype=np.uint8) 
array[:,:100] = [255, 128, 0]

#Orange left side 
#Blue right side
array[:,100:] = [0, 0, 255] 
img = Image.fromarray(array) 
img.save('testrgb.png')
img.show()


"""
Creating RGBA images
"""

"""
An RGBA image has 4 channels (unlike an RGB image that has only 3). 
The fourth channel is an alpha channel. 
An alpha value of 255 will make the pixel fully opaque, value 0 will make it 
fully transparent, values in between will make the pixel partly transparent.

"""

array = np.zeros([100, 200, 4], dtype=np.uint8) 
array[:,:100] = [255, 128, 0, 255] 
#Orange left side 
array[:,100:] = [0, 0, 255, 255] 
#Blue right side

for x in range(200): 
    for y in range(100): 
        array[y, x, 3] = x

img = Image.fromarray(array) 
img.save('testrgba.png')
img.show()


# Creating greyscale images
array = np.zeros([100, 200], dtype=np.uint8)
for x in range(200): 
    for y in range(100): 
        if (x % 16) // 8 == (y % 16) // 8: 
            array[y, x] = 0 
        else: 
            array[y, x] = 255

img = Image.fromarray(array) 
img.save('testgrey.png')
img.show()

 

# Importing the required module
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

img = np.ones((8, 8))

img = [
       [1, 1, 0, 0, 0, 0, 1, 1],
       [1, 0, 1, 1, 1, 1, 0, 1],
       [0, 1, 0, 1, 1, 0, 1, 0],
       [0, 1, 1, 1, 1, 1, 1, 0],
       [0, 1, 0, 1, 1, 0, 1, 0],
       [0, 1, 1, 0, 0, 1, 1, 0],
       [1, 0, 1, 1, 1, 1, 0, 1],
       [1, 1, 0, 0, 0, 0, 1, 1]
       ]

print(type(img))


plt.imshow(img, "gray")


img_file = Image.fromarray(img, "I")
img_file.save("Smile.png")
img_file.show()


""" 
Wap to create an  colored image using numpy array
"""
# Importing the numpy and matplotlib module
import numpy as np
import matplotlib.pyplot as plt

# Importing Pillow libraray for saving the numpy array as image
from PIL import Image

# Defining the color codes for creating the image
numpy_img = [
[(255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 255, 255)],
[(255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255)],
[(255, 0, 0), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 0, 0)],
[(255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0)],
[(255, 0, 0), (255, 255, 255), (0, 255, 0), (255, 255, 255), (255, 255, 255), (0, 255, 0), (255, 255, 255), (255, 0, 0)],
[(255, 0, 0), (255, 255, 255), (255, 255, 255), (0, 255, 0), (0, 255, 0), (255, 255, 255), (255, 255, 255), (255, 0, 0)],
[(255, 255, 255),(255,0,0),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,0,0),(255,255,255)],
[(255,255,255),(255,255,255),(255,0,0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 255, 255)]
]

# Creating the image using .imshow
plt.imshow(np.array(numpy_img, dtype=np.uint8))

# Saving the numpy array as image
img_data = Image.fromarray(np.array(numpy_img,dtype=np.uint8), 'RGB')
img_data.save("images/colorsmile.png")
img_data.show()


"""

# Real World Examples

# Image Feature Extraction
# First, we can map the image into a NumPy array of its pixel values:
# For simplicity’s sake, the image is loaded in grayscale, resulting in a 2d array of 64-bit floats 
# rather than a 3-dimensional MxNx4 RGBA array, with lower values denoting darker spots:
    
from skimage import io
url = ('https://www.history.navy.mil/bin/imageDownload?image=/'
       'content/dam/nhhc/our-collections/photography/images/'
       '80-G-410000/80-G-416362&rendition=cq5dam.thumbnail.319.319.png')
img = io.imread(url, as_grey=True)

fig, ax = plt.subplots()
ax.imshow(img, cmap='gray')
ax.grid(False)

img.shape

img.min(), img.max()

img[0, :10]  # First ten cells of the first row

img[-1, -10:]  # Last ten cells of the last row

img.dtype

#Internally, img is kept in memory as one contiguous block of 648,208 bytes
img.nbytes

#strides is hence a sort of “metadata”-like attribute that tells us how many bytes we need to jump ahead 
#to move to the next position along each axis. 
#We move in blocks of 8 bytes along the rows but need to traverse 8 x 319 = 2,552 bytes to move “down” from one row to another.
 
img.strides

"""





