# -*- coding: utf-8 -*-
"""PRO-C118 Clustering

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11H6Lgcfpgj1F0G2gvts3iMr-Hrg2r1xy
"""

from google.colab import files
data_to_load = files.upload()

import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("data.csv")
data1 = df["Size"].tolist()
data2 = df["Light"].tolist()
print(data1, data2)

fig = px.scatter(x = data1, y = data2)
fig.show()

from sklearn.cluster import KMeans

X = df.iloc[:, [0, 1]].values

print(X)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state = 42)
    kmeans.fit(X)

    # inertia method returns wcss for that model
    wcss.append(kmeans.inertia_)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,5))
sns.lineplot(range(1, 11), wcss, marker='o', color='red')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters= 3, init='k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)

plt.figure(figsize=(15,7))
sns.scatterplot(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], color = 'yellow', label = 'Cluster 1')
sns.scatterplot(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], color = 'blue', label = 'Cluster 2')
sns.scatterplot(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], color = 'green', label = 'Cluster 3')
sns.scatterplot(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color = 'red', label = 'Centroids',s=100,marker=',')
plt.grid(False)
plt.title('Clusters of Flowers')
plt.xlabel('Petal Size')
plt.ylabel('Sepal Size')
plt.legend()
plt.show()