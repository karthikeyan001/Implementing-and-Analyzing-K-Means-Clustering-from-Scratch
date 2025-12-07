
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from kmeans import KMeans

df = pd.read_csv("data.csv")
X = df.values

# Store SSE and silhouette manually
def silhouette(X, labels):
    from scipy.spatial.distance import cdist
    d = cdist(X, X)
    s_vals = []
    for i in range(len(X)):
        own = labels[i]
        a = d[i][labels==own].mean() if sum(labels==own)>1 else 0
        b = min([d[i][labels==c].mean() for c in set(labels) if c!=own])
        s_vals.append((b-a)/max(a,b))
    return np.mean(s_vals)

Ks = range(2,8)
SSE = []
SIL = []

for k in Ks:
    model = KMeans(n_clusters=k)
    model.fit(X)
    SSE.append(model.inertia_)
    SIL.append(silhouette(X, model.labels_))

plt.plot(Ks, SSE, marker="o")
plt.title("Elbow Method (SSE)")
plt.xlabel("K")
plt.ylabel("SSE")
plt.savefig("elbow.png")
plt.close()

plt.plot(Ks, SIL, marker="o")
plt.title("Silhouette Score")
plt.xlabel("K")
plt.ylabel("Silhouette")
plt.savefig("silhouette.png")
plt.close()

print("Analysis complete. Files saved: elbow.png, silhouette.png")
