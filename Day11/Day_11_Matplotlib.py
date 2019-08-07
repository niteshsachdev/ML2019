"""
Basics of Matplotlib
    Scatter Plot
    Line Plot
    Pie Chart
    Bar Chart
    Histogram
    Box Plot
"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]  

y = [1,2,3,4,5,6,7,8,9,10]


# Setting the title
plt.title("A Line Graph")

# Setting the X Label 
plt.xlabel("X")

# Setting the Y Label
plt.ylabel("Y")

# Displaying the Grid
plt.grid(True)

# Changing the x axes limits of the scale
plt.xlim(0, 10)

# Changing the y axes limits of the scale
plt.ylim(0, 10)

# Or
plt.axis([0, 10, 0, 10]);

# Showing the points on the graph
plt.scatter(x, y)

# Simple Line plot
plt.plot(x, y)

plt.savefig("scatter.jpg")

plt.show()


# Changing the color of the line
plt.plot(x, y, color='green') # #000000

# Changing the style of the line
plt.plot(x, y, linestyle='dashed') # solid dashed  dashdot dotted

# For Plotting Scatter Plot
plt.plot(x, y, '<', color='black') # o  .  , x  +  v  ^  <  >  s d 

# Scatter Plot with scatter method 
plt.scatter(x, y, marker='.', color='black',label="marker='{0}'".format('.')); # o  .  , x  +  v  ^  <  >  s d 
plt.legend(numpoints=1)



"""
Pie chart, where the slices will be ordered and plotted counter-clockwise:
"""

labels = 'CSE', 'ECE', 'IT', 'EE'
sizes = [15, 30, 25, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

#plt.pie(sizes, labels=labels, autopct='%.0f%%')

# or

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)


plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

        

"""
Plotting a bar chart
"""

import matplotlib.pyplot as plt
 
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
performance = [10,8,6,4,2,1]
 
plt.bar([0,1,2,3,4,5], performance, align='center', alpha=1.0)
plt.xticks([0,1,2,3,4,5], objects)
plt.ylabel('Usage')
plt.title('Programming Language Usage')
 
plt.show()



"""
Another Example of Bar Chart
"""
	
import matplotlib.pyplot as plt

 
# 14 categories of movies
label = ['Adventure', 'Action', 'Drama', 'Comedy', \
         'Thriller/Suspense', 'Horror', 'Romantic Comedy', 'Musical', \
         'Documentary', 'Black Comedy', 'Western', 'Concert/Performance', \
         'Multiple Genres', 'Reality']
 
no_movies = [941,854,4595,2125,942,509,548,149,1952,161,64,61,35,5]

index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

plt.bar(index, no_movies)
plt.xlabel('Genre', fontsize=15)
plt.ylabel('No of Movies', fontsize=15)
plt.xticks(index, label, fontsize=10, rotation=90)
plt.title('Market Share for Each Genre 1995-2017')
plt.show()



"""
Histogram - Bar Graph of Frequency 

A histogram is used to summarize discrete or continuous data. 
In other words, it provides a visual interpretation of numerical data by 
showing the number of data points that fall within a specified range of 
values (called "bins").
However, a histogram, unlike a vertical bar graph, shows no gaps between the bars.


X Axis = width = Class Interval
Y Axis = height = Frequency

Creating a histogram provides a visual representation of data distribution.
The median and distribution of the data can be determined by a histogram.
It can show any outliers or gaps in the data.

Types of Distribution
1. Normal distribution
    Points on one side of the average are as likely to occur as on the other 
    side of the average

2. Bimodal distribution
    There are two peaks
    The data should be separated and analyzed as separate normal distributions
    
3. Right-skewed distribution
    A large number of the data values occur on the left side 

4. Left-skewed distribution
    A large number of the data values occur on the right side

5. Random distribution
    Has several peaks

"""


"""
Ramesh is the branch manager at a local bank. 
Recently, Ramesh’s been receiving customer feedback saying that the wait times 
for a client to be served by a customer service representative are too long. 
Ramesh decides to observe and write down the time spent by each customer on waiting.

Write down the wait times spent by 20 customers
[43.1,35.6,37.6,45.3,43.5,40.3,50.2,47.3,31.2,42.2,45.5,30.3,31.4,35.6,45.2,
54.1,45.6,36.5,43.1]

# [25 to 30]                                          [0]
# [30 to 35]     30.3, 31.2, 31.4                     [3]
# [35 to 40]     35.6, 35.6, 36.5, 37.6               [4]
# [40 to 45]     40.3, 42.2, 43.1, 43.1, 43.5         [5]
# [45 to 50]     45.2, 45.3, 45.5, 45.6, 47.3         [5]
# [50 to 55]     50.2, 54.1                           [2]
# [55 to 60]                                          [0]


"""



import matplotlib.pyplot as plt
# Customers wait times in seconds ( n = 20 customers )
customerWaitTime = [43.1,35.6,37.6,45.3,43.5,40.3,50.2,47.3,31.2,42.2,45.5,30.3\
                    ,31.4,35.6,45.2,54.1,45.6,36.5,43.1]

customerWaitTime.sort()
print (customerWaitTime)
# [30.3, 31.2, 31.4, 35.6, 35.6, 36.5, 37.6, 40.3, 42.2, 43.1, 43.1, 43.5, 45.2,
# 45.3, 45.5, 45.6, 47.3, 50.2, 54.1]

# [25 to 30]                                          [0]
# [30 to 35]     30.3, 31.2, 31.4                     [3]
# [35 to 40]     35.6, 35.6, 36.5, 37.6               [4]
# [40 to 45]     40.3, 42.2, 43.1, 43.1, 43.5         [5]
# [45 to 50]     45.2, 45.3, 45.5, 45.6, 47.3         [5]
# [50 to 55]     50.2, 54.1                           [2]
# [55 to 60]                                          [0]


#Ramesh can conclude that the majority of customers wait between 35 and 50 seconds.
 
plt.hist(customerWaitTime,bins=[25,30,35,40,45,50,55,60]) 

plt.axis([25, 60, 0, 6]) 
plt.xlabel('Seconds')
plt.ylabel('Customers')


######Day 13 Start ##########



"""""""""""""""""""""""""""""
Matplotlib Part 2 After Numpy 
"""""""""""""""""""""""""""""

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

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
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


#fig.savefig('fig1.png', bbox_inches='tight')

         
## add patch_artist=True option to ax.boxplot() 
## to get fill color
bp = ax.boxplot(data_to_plot, patch_artist=True)

## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#7570b3', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='#7570b3', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='#b2df8a', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)
              


"""
Matplotlib Part 3 After Pandas 
"""


# Now make a pie chart for all car makers
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


for x,y in zip(series.index, series.values):
    print (x,y)
    




              
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

### End of Day 13 #######
