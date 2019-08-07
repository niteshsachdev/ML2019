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
#x = x.reshape(4,3,3)

 
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




### Day 13#####################



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


####End of day 13############

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
    
"""

import numpy as np
                          #mean, sd, total
incomes = np.random.normal(27000, 15000, 10000)
#loc=150, scale=20, size=1000


print (type(incomes))
print (incomes.size)
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

"""
Explain NumPy_boxplot.png
"""


print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))

#Adding Bill Gates into the mix. income inequality!(Outliers)
incomes = np.append(incomes, [10000000000])

#Median Remains Almost SAME
print("Median value is: ", np.median(incomes))

#Mean Changes distinctly
print("Mean value is: ", np.mean(incomes))

      
# Give an example for bincount function
# num = np.bincount(incomes).argmax()

