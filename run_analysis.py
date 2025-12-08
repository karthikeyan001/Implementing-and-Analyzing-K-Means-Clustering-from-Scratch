import numpy as np
import matplotlib.pyplot as plt
from kmeans_numpy import KMeans
from silhouette_score_numpy import silhouette_score_numpy

X = np.loadtxt("data.csv", delimiter=",", skiprows=1)

sse = []
sil = []
Ks = range(2, 11)

for k in Ks:
    km = KMeans(k=k).fit(X)
    d = np.linalg.norm(X - km.centroids[km.labels_], axis=1)
    sse.append(np.sum(d**2))
    sil.append(silhouette_score_numpy(X, km.labels_))

optimal_k_sil = Ks[sil.index(max(sil))]

print("Optimal K (Silhouette):", optimal_k_sil)

km = KMeans(k=optimal_k_sil).fit(X)

plt.scatter(X[:, 0], X[:, 1], c=km.labels_)
plt.scatter(km.centroids[:, 0], km.centroids[:, 1], marker='x', s=200)
plt.savefig("final_clusters.png")

print("Saved final_clusters.png")
