import numpy as np

def silhouette_score_numpy(X, labels):
    n = len(X)
    s = []

    for i in range(n):
        same = X[labels == labels[i]]
        others = [X[labels == lab] for lab in set(labels) if lab != labels[i]]

        a = np.mean(np.linalg.norm(same - X[i], axis=1)) if len(same) > 1 else 0
        b = min(
            np.mean(np.linalg.norm(group - X[i], axis=1))
            for group in others
        ) if others else 0

        score = (b - a) / max(a, b) if max(a, b) > 0 else 0
        s.append(score)

    return np.mean(s)
