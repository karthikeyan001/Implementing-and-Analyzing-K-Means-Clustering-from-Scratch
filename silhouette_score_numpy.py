
import numpy as np

def silhouette_score_numpy(X, labels):
    X = np.asarray(X)
    labels = np.asarray(labels)
    n = len(X)
    unique_labels = np.unique(labels)

    # Precompute distance matrix
    dist_matrix = np.linalg.norm(X[:, None] - X[None, :], axis=2)

    sil_scores = []

    for i in range(n):
        same_cluster = labels == labels[i]
        other_clusters = labels != labels[i]

        # a(i): mean intra-cluster distance
        a = dist_matrix[i, same_cluster]
        a = a[a != 0]  # remove distance to itself
        a_i = a.mean() if len(a) > 0 else 0

        # b(i): smallest mean distance to any other cluster
        b_i = np.inf
        for lbl in unique_labels:
            if lbl == labels[i]:
                continue
            cluster_points = labels == lbl
            b = dist_matrix[i, cluster_points].mean()
            b_i = min(b_i, b)

        # silhouette(i)
        s_i = (b_i - a_i) / max(a_i, b_i)
        sil_scores.append(s_i)

    return np.mean(sil_scores)


if __name__ == "__main__":
    # Example test
    X = np.array([[1, 2], [2, 3], [10, 10], [11, 11]])
    labels = np.array([0, 0, 1, 1])
    print("Silhouette Score:", silhouette_score_numpy(X, labels))
