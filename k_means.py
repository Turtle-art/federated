import pandas as pd
from sklearn.cluster import KMeans


# Select the features for clustering
features = df[['epochs', 'neurons_fc1', 'neurons_fc2','learning_rate']]

# Loop through the desired number of clusters (3 to 6)
for n_clusters in range(3, 7):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    df[f'kmeans_{n_clusters}'] = kmeans.fit_predict(features)

print(df)