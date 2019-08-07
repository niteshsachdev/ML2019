"""
Histogram
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

plt.hist(data)

plt.hist(data, normed=True, bins=30)

#plt.hist(data, bins=30, normed=True, alpha=0.5,
#         histtype='stepfilled', color='steelblue',
#         edgecolor='none');
         

         
"""
2D plotting with matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 20.0, 0.01)
s = np.sin(t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('A nice sine wave')
plt.grid(True)
plt.savefig('sinewave.png')
plt.show()



"""
Showing bubbles
"""

import numpy as np 
import matplotlib.pyplot as plt 

# Define the number of values
num_vals = 40

# Generate random values
x = np.random.rand(num_vals)
y = np.random.rand(num_vals)

# Define area for each bubble
# Max radius is set to a specified value
max_radius = 25
area = np.pi * (max_radius*np.random.rand(num_vals)) ** 2

# Generate colors
colors = np.random.rand(num_vals)

# Plot the points
plt.scatter(x, y, s=area, c=colors, alpha=.5)
plt.show()



"""
Showing bubbles 2
"""

rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar() # show color scale
# In this way, the color and size of points can be used to convey information in the visualization, 
# in order to visualize multidimensional data.


         
"""
Box Plot
"""
"""
import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt 

## agg backend is used to create plot as a .png file
mpl.use('agg')         
         
## Create data
np.random.seed(10)
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)
collectn_4 = np.random.normal(70, 25, 200)

## combine these different collections into a list    
data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)


fig.savefig('fig1.png', bbox_inches='tight')

"""


"""
Now make a pie chart for all car makers
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Automobile.csv")

series = df["make"].value_counts()

print (series.index[0:11])
print (series.values[0:11])

explode = (0.5,0,0,0,0,0,0,0,0,0,0)

plt.pie(series.values[0:11], explode = explode, labels=series.index[0:11], autopct='%2.2f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

              
"""
# Showing Different ways of Scatter Plots with plot
# Convert the random function from random class

import numpy as np
import matplotlib.pyplot as plt 
rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
             label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8);
"""


"""
More on box ploting to identify the outliers
"""

# https://plot.ly/create/box-plot/


import numpy as np

incomes = np.random.normal(27000, 15000, 10000)
np.mean(incomes)
np.median(incomes)
np.std(incomes)

#We can segment the income data into 20 buckets, and plot it as a histogram:

import matplotlib.pyplot as plt
plt.hist(incomes, 20)
plt.show()

plot = plt.boxplot(incomes)


#box and whisker plot to show distribution
#https://chartio.com/resources/tutorials/what-is-a-box-plot/
#box plot creating: https://plot.ly/create/box-plot/#/
incomes = np.append(incomes,100000000)
plot = plt.boxplot(incomes)


#second version

import pandas as pd
bp= pd.DataFrame.boxplot(pd.DataFrame(incomes), return_type='dict')

outliers = [flier.get_ydata() for flier in bp["fliers"]]
boxes = [box.get_ydata() for box in bp["boxes"]]
medians = [median.get_ydata() for median in bp["medians"]]
whiskers = [whiskers.get_ydata() for whiskers in bp["whiskers"]]

"""
removing outlies from the incomes
xx = [item for item in incomes if (item > -13124 and item < 67665)]
you get the min and max values from whiskers

"""


"""
return_type : {‘axes’, ‘dict’, ‘both’} or None, default ‘axes’
The kind of object to return. The default is axes.

‘axes’ returns the matplotlib axes the boxplot is drawn on.

‘dict’ returns a dictionary whose values are the matplotlib Lines of the boxplot.

‘both’ returns a namedtuple with the axes and dict.
http://colingorrie.github.io/outlier-detection.html

"""
"""
https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba
"""

#---------------------------------------
#Standard Deviation, Variance, Mode, Frequency Table

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 50.0, 10000)
#incomes = np.random.normal(27000.0, 15000.0, 10000)
plt.hist(incomes, 50)
plt.show()

print (incomes.std())
print (incomes.var())
#The standard deviation is the square root of the variance. 


randNumbers = np.random.randint(5,15,40)
counts = np.bincount(randNumbers)
print (np.argmax(counts))



#################


from numpy import genfromtxt
#to read as record array
my_data = genfromtxt('Salaries.csv', delimiter=',', dtype=None)



###################











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
two_d_array[::-1]
two_d_array[:,::-1]
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

print (array_to_join)

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


"""
print(type(photo))
print (photo.dtype)
print (photo.itemsize)
print (photo.size) # 147x220x3 = 97020
print (photo.nbytes)
"""


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
Key Machine Learning Terminology

Descriptive - What Happened
Predictive - What will happen
Prescriptive - What to do 


Prediction can be of two types 
1. Continuous values ( Regression Model )
2. Discrete Values   ( Classification Model )


Label = variable we're predecting, typically represented by variable y
Feature = Input variables describing the data, represented by variables {x1,x2,x3....xn}
Model = Piece of Software or Mapping function ( maps examples to predicted labels )

ML = Process of training the Model for prediction on never-before-seen dataset

Supervised learning = Is a type of ML where the model is 
                      provided with labeled training data.

Example is a particular instance of data X
Labelled example has { feature,label } : {x,y}, it is used to train the model
UnLabelled example has { feature,? } : {x,?}, used to make predictions on new data 

Give ( Classification )Example of Spam Detection of Email to explain the below concept
In the spam detector example, the features could include the following:
    (feature)          words in the email text
    (feature)          sender's address
    (feature)          time of day the email was sent
    (feature)          email contains the phrase "one weird trick."
    (label )           Whether the email is SPAM or HAM

Another ( Regression )Example is the Housing Prices in Jaipur
housingMedianAge            (feature)
totalRooms                  (feature)
totalBedrooms               (feature)
medianHouseValue            (label)





Hands On 1:
Suppose you want to develop a supervised machine learning model to predict 
whether a given email is "spam" or "not spam." 
Which of the following statements are true? 

1. We'll use unlabeled examples to train the model. ( FALSE)
2. Emails not marked as "spam" or "not spam" are unlabeled examples ( TRUE)
3. Words in the subject header will make good labels. ( FALSE )
4. The labels applied to some examples might be unreliable. ( TRUE )


Hands On  2:
Suppose an online shoe store wants to create a supervised ML model that will 
provide personalized shoe recommendations to users. 
That is, the model will recommend certain pairs of shoes to Marty and different 
pairs of shoes to Janet. 
Which of the following statements are true? 
    
1. "Shoe beauty" is a useful feature. ( FALSE )
2. "The user clicked on the shoe's description" is a useful label. ( TRUE )
3. "Shoe size" is a useful feature. ( TRUE )
4. "Shoes that a user adores" is a useful label. ( FALSE )



Example of amateur botanist ( to define features and label)
Leaf Width 	Leaf Length 	Species
2.7 	    4.9 	        small-leaf
3.2 	    5.5 	        big-leaf
2.9 	    5.1 	        small-leaf
3.4 	    6.8 	        big-leaf

Leaf width and leaf length are the features (which is why they are both labeled X), 
while the species is the label.

Features are measurements or descriptions; the label is essentially the "answer."

For example, the goal of the data set is to help other botanists answer the question, 
"Which species is this plant?"




In Supervised Machine Learning

Training = Feeding the features and their corresponding labels into an algorithm

During training, the algorithm gradually determines the relationship (mapping fucntion)
between features and their corresponding labels. 
This relationship is called the model.


Real World Example of Supervised Learning
Study from Stanford University to detect skin cancer in images
training set contained images of skin labeled by dermatologists as having one of several diseases. 
The ML system found signals that indicate each disease from its training set
and used those signals to make predictions on new, unlabeled images.


In Unsupervised Machine Learning
In unsupervised learning, the goal is to identify meaningful patterns in the data. 
To accomplish this, the machine must learn from an unlabeled data set.
In other words, the model has no hints how to categorize each piece of data 
and must infer its own rules for doing so.


In Reinforcement Learning ( RL )
In RL you don't collect examples with labels.
Imagine you want to teach a machine to play a very basic video game and never lose. 
You set up the model (often called an agent in RL) with the game, and you tell 
the model not to get a "game over" screen. 
During training, the agent receives a reward when it performs this task, 
which is called a reward function. With reinforcement learning, 
the agent can learn very quickly how to outperform humans. 

However, designing a good reward function is difficult, and RL models are less stable 
and predictable than supervised approaches.
 

Types of ML Problems
    
    Type of ML Problem	Description	                  Example
Classification 	    Pick one of N labels 	      Cat, dog, horse, or bear

Regression 	        Predict numerical values 	  Click-through rate

Clustering 	        Group similar examples 	      Most relevant documents (unsupervised)

Association         Infer likely association      If you buy hamburger buns,
rule learning 	    patterns in data 	          you're likely to buy hamburgers (unsupervised)

Structured output 	Create complex output 	      Natural language parse trees, image recognition bounding boxes

Ranking 	        Identify position on a  	      Search result ranking
                    scale or status


How ML powers Google Photos: 
Find a specific photo by keyword search without manual tagging
ML powers the search behind Google Photos to classify people, places, and things.

Smart Reply Feature of Gmail

Give a use case of WholesaleBox Recommendation Old logic and
How we enabled it using Machine Learning Techniques

With these examples in mind ask yourself the following questions:

What problem is my product facing?
Would it be a good problem for ML?

ML is better at making decisions than giving you insights.

Prediction	
What video the learner wants to watch next.	

Decision
Show those videos in the recommendation bar.

"""



"""
# Show Image ML_SalesPriceVsFootage

Show the Graph of House Price ( label on Y axis ) and 
House Square Footage ( Feature on X Axis )

y = b  +  w1x1

Create a straight line so that the line tries to pass through all the points

Introduce the concept of loss and try to find the loss for those points which are not on the line

A convienient loss function for Regression 

L2 loss for a given example  is also called squared error
= square of the diff between prediction and label
= ( observation - prediciton )square 2
= (y - y') square 2

  

#Show the image of ML_Cricket.jpg

Data on chirps-per-minute and temperature
 
y' = w0 +   ( w1 * x1 ) 

y' = Predicted Label
w0 = bias
w1 = weight of feature x1
x1 = feature (input)
  

Training and Loss:
    
Training a model simply means learning (determining) good values for all the 
weights and the bias from labeled examples. 

In supervised learning, a machine learning algorithm builds a model by examining
many examples (training) and attempting to find a model that minimizes loss; 
this process is called empirical risk minimization.


Loss is the penalty for a bad prediction. 

That is, loss is a number indicating how bad the model's prediction was on a single example.

Loss Function = squared loss (also known as L2 loss)
= the square of the difference between the label and the prediction
= (observation - prediction(x))2
= (y - y')square 2

  

Mean square error (MSE) is the average squared loss per example over the whole dataset.
#https://medium.freecodecamp.org/machine-learning-mean-squared-error-regression-line-c7dde9a26b93
# https://www.statisticshowto.datasciencecentral.com/mean-squared-error/




Hands On to Calculate the Bias and Slope of the best fit line


Show ML_MSE3.jpg

Let’s take 4 points, (-2,-3), (-1,-1), (1,2), (4,3).
Let’s find M and B for the equation y=mx+b.
Sum the x values and divide by n
xbar=(-2)+(-1)+1+4 / 4 = 1/2                     #Sum the x values and divide by n
ybar = (-3)+(-1)+2+3 / 4 = 1/4                   #Sum the y values and divide by n

xybar = (-2)*(-3) + (-1)*(-1) + 1*2 + 4*3 /4     #Sum the xy values and divide by n
      = 21 / 4
      
x square bar = 4 + 1 + 1 + 16  /4 = 11 / 2       #Sum the x² values and divide by n
      

Slope calculation
m = (21/4 - 1/2*1/4 ) / 11/2 - (1/2)²
  = 41/42
  
y-intercept calculation
b = 1/4 - 41/42*1/2
  = -5/21


Let’s take those results and set them inside line equation y=mx+b.

y = (41/42)*x - (5/12)


First lets intercept the b  value on the graph (-.42)

Then now keeping y = 0 , imagine the line is cutting x axis
y = mx + b
put y =0, m = 41/42 and b = -5/21
then 
x = 10/41 = .24

mark both the points and draw a straight line


Now let’s draw the line and see how the line passes through the lines in such a
 way that it minimizes the squared distances.


 
Show ML_MSE4.jpg

As you can see, the whole idea is simple. 
We just need to understand the main parts and how we work with them.

You can work with the formulas to find the line on another graph, 
and perform a simple calculation and get the results for the slope and y-intercept.



# Code Challenge to find the MSE for a given datset
# Now calculate the predicted values for all the points based on the model
# It can be achieved by either drawing on the grpah or putting the x values in
# the line equation and getting the predicted y values

y = (41/42)*x - (5/12)
y = .98x - .24

Let’s take 4 points, (-2,-3),   (-1,-1),   (1,2),   (4,3)
Predicted values,    (-2, 2.2), (-1,1.22), (1,.74), (4,3.68)  

Finding the Difference in the predicted values ( y - y')
-3 - 2.2    = -5.2
-1 - 1.22   = -2.22
2 - .74     = +1.26
3 - 3.68    = -0.68


Square the Error
-5.2  * -5.2  = 27.04
-2.22 * -2.22 =  4.93
1.26  *  1.26 =  1.59
-0.68 * -0.68 =  0.46

Add all the squared errors
27.04 + 4.93 + 1.59 + 0.46 = 34.02

Find the mean sqaured error
34.02/4 = 8.505

The smaller the means squared error, the closer you are to finding the line of best fit.







Reducing Loss :

An iterative approach is one widely used method for reducing loss, 
and is as easy and efficient as walking down a hill.
    
"""


# Introduce the concept of Gradient Descent

# Why to us gradient Descent when we can calculate maually 
"""
The main reason why gradient descent is used for linear regression is the 
computational complexity: it's computationally cheaper (faster) to find the 
solution using the gradient descent in some cases.
"""

# Visualisation Link
# https://medium.com/meta-design-ideas/linear-regression-by-using-gradient-descent-algorithm-your-first-step-towards-machine-learning-a9b9c0ec41b1
# https://cdn-images-1.medium.com/max/947/1*IjxpxWcKX8EJUVFBNFeKdA.gif

"""
https://www.edureka.co/blog/math-and-statistics-for-data-science/
https://www.kdnuggets.com/2018/08/basic-statistics-python-descriptive-statistics.html
https://www.datacamp.com/community/tutorials/demystifying-crucial-statistics-python
"""

"""
//This is most suitable for this day.
https://medium.com/@kshitiz.k26/statistics-research-principles-and-terminologies-efc277810268
"""
