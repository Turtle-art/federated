import pandas as pd
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
import matplotlib.pyplot as plt

# data includes household number and its hyperparameters

df = pd.DataFrame(data)

# Perform hierarchical clustering
linkage_matrix = linkage(df, method='ward', metric='euclidean')

# Specify the number of clusters (4 in your case)
num_clusters = 4

# Assign data points to clusters
df['cluster'] = fcluster(linkage_matrix, num_clusters, criterion='maxclust')

# Display the DataFrame with cluster assignments
print(df)

# You can also visualize the dendrogram to help choose the number of clusters
dendrogram(linkage_matrix, labels=df.index, leaf_rotation=90, leaf_font_size=8)
plt.show()