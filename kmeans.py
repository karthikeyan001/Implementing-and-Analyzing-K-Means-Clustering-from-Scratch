
import numpy as np

class KMeans:
    def __init__(self, n_clusters=3, max_iter=300, tol=1e-4, random_state=42):
        self.k = n_clusters
        self.max_iter = max_iter
        self.tol = tol
        self.random_state = random_state

    def fit(self, X):
        np.random.seed(self.random_state)
        idx = np.random.choice(len(X), self.k, replace=False)
        self.centroids = X[idx]

        for _ in range(self.max_iter):
            distances = np.sqrt(((X[:, None] - self.centroids)**2).sum(axis=2))
            labels = distances.argmin(axis=1)

            new_centroids = np.array([X[labels == i].mean(axis=0) 
                                      if np.any(labels == i) else self.centroids[i]
                                      for i in range(self.k)])

            if np.max(np.linalg.norm(new_centroids - self.centroids, axis=1)) < self.tol:
                break

            self.centroids = new_centroids

        self.labels_ = labels
        self.inertia_ = ((X - self.centroids[labels])**2).sum()
        return self

    def predict(self, X):
        distances = np.sqrt(((X[:, None] - self.centroids)**2).sum(axis=2))
        return distances.argmin(axis=1)
