"""
Q1. (Create a program that fulfills the following specification.)

Import Crime.csv File.

    Perform dimension reduction and group the cities using k-means based on Rape, Murder and assault predictors.
"""

# PCA

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Crime_data.csv')
features = dataset.iloc[:,[1,2,4]].values
labels=dataset.iloc[:,0].values
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features = sc.fit_transform(features)


# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 1)
features = pca.fit_transform(features)
explained_variance = pca.explained_variance_ratio_


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


# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)


# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0], labels[pred_cluster == 0],s=20, c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1], labels[pred_cluster == 1],s=20, c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2], labels[pred_cluster == 2],s=20, c = 'green', label = 'Cluster 3')
plt.title('Clusters of datapoints')
plt.xlabel('Cluster')
plt.ylabel('Citeies')
plt.show()

"""
Q2. (Create a program that fulfills the following specification.)

The iris data set consists of 50 samples from each of three species of Iris flower (Iris setosa, Iris virginica and Iris versicolor).



    Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres (iris.data).
    Import the iris dataset already in sklearn module using the following command:\


from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data


Reduce dimension from 4-d to 2-d and perform clustering to distinguish the 3 species.
"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data


# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(iris)
explained_variance = pca.explained_variance_ratio_


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


# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Iris setosa')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Iris virginica')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Iris versicolor')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()


"""
Q3.
Code Challenge -
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks

"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
#1. Visualize the various countries from where the artworks are coming.

dataset = pd.read_csv('data.csv')
country=dataset['Country'].value_counts()
plt.bar(country.index,country.values)

#2. Visualize the top 2 classification for the artworks
classification=dataset['Classification'].value_counts().head(2)
plt.bar(classification.index,classification.values)

#3. Visualize the artist interested in the artworks
art_interested=dataset['Artist Display Name'].value_counts()
plt.bar(art_interested.index,art_interested.values)


#4. Visualize the top 2 culture for the artworks
culture=dataset['Culture'].value_counts().head(2)
plt.bar(culture.index,culture.values)

