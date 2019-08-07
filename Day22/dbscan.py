# -*- coding: utf-8 -*-
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
from sklearn.datasets import load_iris
iris = load_iris()

from sklearn.cluster import DBSCAN
dbscan = DBSCAN()

print dbscan
"""
DBSCAN(eps=0.5, metric='euclidean', min_samples=5,
  random_state=111)
"""

dbscan.fit(iris.data)

dbscan.labels_

# Visualising the clusters 
# as data is in 3d space, we need to apply PCA for 2d ploting
from sklearn.decomposition import PCA
pca = PCA(n_components=2).fit(iris.data)
pca_2d = pca.transform(iris.data)
explained_variance = pca.explained_variance_ratio_

df_pca =  pd.DataFrame(pca.components_,columns=iris.feature_names,index = ['PC-1','PC-2'])


"""
#alternative way, fit_transform
pca = PCA(n_components = 2)
pca_2d =  pca.fit_transform(iris.data)
"""
for i in range(0, pca_2d.shape[0]):
    if dbscan.labels_[i] == 0:
        c1 = plt.scatter(pca_2d[i,0],pca_2d[i,1],c='r', marker='+')
    elif dbscan.labels_[i] == 1:
        c2 = plt.scatter(pca_2d[i,0],pca_2d[i,1],c='g',
                        marker='o')
    elif dbscan.labels_[i] == -1:
        c3 = plt.scatter(pca_2d[i,0],pca_2d[i,1],c='b',
                        marker='*')
    
    
plt.legend([c1, c2, c3], ['Cluster 1', 'Cluster 2','Noise'])
plt.title('DBSCAN finds 2 clusters and noise')
plt.savefig("dbscan.jpg")
plt.show()

"""
plt.scatter(pca_2d[dbscan.labels_ == 0,0], pca_2d[dbscan.labels_ == 0,1],c='r', marker='+' )
plt.scatter(pca_2d[dbscan.labels_ == 1,0], pca_2d[dbscan.labels_ == 1,1],c='g', marker='o' )
plt.scatter(pca_2d[dbscan.labels_ == -1,0], pca_2d[dbscan.labels_ == -1,1],c='b', marker='*' )
"""

pca.components_

for i in range(0, pca_2d.shape[0]):
    if iris.target[i] == 0:
        c1 = plt.scatter(pca_2d[i,0],pca_2d[i,1],c='r', marker='+')
    elif iris.target[i] == 1:
        c2 = plt.scatter(pca_2d[i,0],pca_2d[i,1],c='g',
                        marker='o')
    elif iris.target[i] == 2:
        c3 = plt.scatter(pca_2d[i,0],pca_2d[i,1],c='b',
                        marker='*')
    
plt.legend([c1, c2, c3], ['Cluster 1', 'Cluster 2','Noise'])
plt.title('DBSCAN finds 2 clusters and noise')

plt.savefig("classifier.jpg")
plt.show()


# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit_predict(iris.data)
for i in range(0, pca_2d.shape[0]):
    if y_kmeans[i] == 0:
        c1 = plt.scatter(pca_2d[i,0],pca_2d[i,1],c='r', marker='+')
    elif y_kmeans[i] == 1:
        c2 = plt.scatter(pca_2d[i,0],pca_2d[i,1],c='g',
                        marker='o')
    elif y_kmeans[i] == 2:
        c3 = plt.scatter(pca_2d[i,0],pca_2d[i,1],c='b',
                        marker='*')
    
plt.legend([c1, c2, c3], ['Cluster 1', 'Cluster 2','Noise'])
plt.title('DBSCAN finds 2 clusters and noise')
plt.savefig("kmeans.jpg")

plt.show()

"""
Very important about noise points
You can see that DBSCAN produced three groups. 
Note, however, that the figure closely resembles a two-cluster 
solution: It shows only 17 instances of label – 1. 
That’s because it’s a two-cluster solution; the third group (–1)
 is noise (outliers). You can increase the distance parameter 
 (eps) from the default setting of 0.5 to 0.9, and it will 
 become a two-cluster solution with no noise.

The distance parameter is the maximum distance an 
observation is to the nearest cluster. The greater the value 
for the distance parameter, the fewer clusters are found 
because clusters eventually merge into other clusters. The –1 
labels are scattered around Cluster 1 and Cluster 2 in a few 
locations:

Near the edges of Cluster 2 (Versicolor and Virginica classes)

Near the center of Cluster 2 (Versicolor and Virginica classes)

"""



"""
DBSCAN Details

https://towardsdatascience.com/how-dbscan-works-and-why-should-i-use-it-443b4a191c80

https://www.dummies.com/programming/big-data/data-science/how-to-create-an-unsupervised-learning-model-with-dbscan/
"""

"""
Animation
https://www.naftaliharris.com/blog/visualizing-dbscan-clustering/
"""

"""
eps: if the eps value chosen is too small, 
a large part of the data will not be clustered. 
It will be considered outliers because don’t 
satisfy the number of points to create a dense 
region. On the other hand, if the value that was 
chosen is too high, clusters will merge and the 
majority of objects will be in the same cluster.
The eps should be chosen based on the distance of 
the dataset (we can use a k-distance graph to find 
it), but in general small eps values are preferable.

minPoints: As a general rule, a minimum 
minPoints can be derived from a number of 
dimensions (D) in the data set, as minPoints ≥ D + 1.
Larger values are usually better for data sets 
with noise and will form more significant clusters.
The minimum value for the minPoints must be 3,
but the larger the data set, the larger the 
minPoints value that should be chosen.
"""