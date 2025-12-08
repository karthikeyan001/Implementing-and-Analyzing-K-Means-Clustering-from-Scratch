import numpy as np

class KMeans:
    def __init__(self, k=3, max_iters=300, tol=1e-4):
        self.k = k
        self.max_iters = max_iters
        self.tol = tol

    def fit(self, X):
        n = len(X)
        idx = np.random.choice(n, self.k, replace=False)
        self.centroids = X[idx]

        for _ in range(self.max_iters):
            d = np.linalg.norm(X[:, None, :] - self.centroids[None, :, :], axis=2)
            labels = np.argmin(d, axis=1)

            new_centroids = np.array([
                X[labels == i].mean(axis=0) if np.any(labels == i) else self.centroids[i]
                for i in range(self.k)
            ])

            if np.linalg.norm(new_centroids - self.centroids) < self.tol:
                break

            self.centroids = new_centroids

        self.labels_ = labels
        return self

    def predict(self, X):
        d = np.linalg.norm(X[:, None, :] - self.centroids[None, :, :], axis=2)
        return np.argmin(d, axis=1)
