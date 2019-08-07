"""
Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) and the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

    Perform K-means clustering to distinguish urban drivers and rural drivers.
    Perform K-means clustering again to further distinguish speeding drivers from those who follow speed limits, in addition to the rural vs. urban division.
    Label accordingly for the 4 groups.
"""

import matplotlib.pyplot as plt
import pandas as pd

dataset =pd.read_csv("deliveryfleet.csv")
features=dataset.iloc[:,1:].values

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()


# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)    

#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()
# now we find that we have to groups using elbow method


# Fitting K-Means to the dataset
kmeans=KMeans(n_clusters=2,init='k-means++',random_state=0)
pred_cluster=kmeans.fit_predict(features)



# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'rural')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'urban')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance')
plt.ylabel('Speeding')
plt.legend()
plt.show()

#    Perform K-means clustering again to further distinguish speeding drivers from those who follow speed limits, in addition to the rural vs. urban division.

# Fitting K-Means to the dataset
kmean=KMeans(n_clusters=4,init='k-means++',random_state=0)
pred_cluster=kmean.fit_predict(features)


# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'rural')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'urban')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'yellow', label = 'rural_speedig')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'green', label = 'urban_speeding')
plt.scatter(kmean.cluster_centers_[:, 0], kmean.cluster_centers_[:, 1], c = 'orange', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance')
plt.ylabel('Speeding')
plt.legend()
plt.show()

"""
Q2. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. How would you figure out the actual size of these 3 types of shirt to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of the data as stated above.
"""


import matplotlib.pyplot as plt
import pandas as pd

dataset =pd.read_csv("tshirts.csv")
features=dataset.iloc[:,1:].values

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()


# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)    

#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()
# now we find that we have three groups using elbow method


# Fitting K-Means to the dataset
kmeans=KMeans(n_clusters=3,init='k-means++',random_state=0)
pred_cluster=kmeans.fit_predict(features)



# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'small')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'medium')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'large')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('height')
plt.ylabel('weight')
plt.legend()
plt.show()


"""
Code Challenge - 
 This is a pre-crawled dataset, taken as subset of a bigger dataset 
 (more than 4.7 million job listings) that was created by extracting data 
 from Monster.com, a leading job board.
 
 
 
 Remove location from Organization column?
 Remove organization from Location column?
 
 In Location column, instead of city name, zip code is given, deal with it?
 
 Seperate the salary column on hourly and yearly basis and after modification
 salary should not be in range form , handle the ranges with their average
 
 Which organization has highest, lowest, and average salary?
 
 which Sector has how many jobs?
 Which organization has how many jobs
 Which Location has how many jobs?
"""


import matplotlib.pyplot as plt
import pandas as pd

dataset =pd.read_csv("monster_com-job_sample.csv")
dataset.isnull().any(axis=0)

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

#dataset['organization']
dataset['location']=dataset['location'].str.split(',')
for row in range(len(dataset['location'])):
    if len(dataset['location'][row])>3:
        dataset['location'][row]=float('nan')
    else:
        dataset['location'][row]=",".join(dataset['location'][row])
for row in range(len(dataset['location'])):
    if str(dataset['location'][row])!='nan':
        dataset['location'][row]=dataset['location'][row].str.split(',')
        if len(dataset['location'][row])==1:
            if hasNumbers(dataset['location'][row])!=True:
                dataset['location'][row]=float('nan')  
            else:
                dataset['location'][row].str.split(' ')
                