# K-Means From Scratch (NumPy Only)

## Overview
This project implements the K-Means clustering algorithm entirely from scratch using only NumPy.  
It includes:

- Manual K-Means implementation  
- SSE (Elbow) Analysis  
- Silhouette Score (custom NumPy version)  
- Automatic optimal K selection  
- Final clustering visualization  

---

## Files Included

| File | Description |
|------|-------------|
| `kmeans_numpy.py` | Core K-Means algorithm (NumPy only) |
| `silhouette_score_numpy.py` | Manual Silhouette Score implementation |
| `run_analysis.py` | Runs full analysis, finds optimal K, generates plots |
| `data.csv` | Dataset containing X and Y numeric columns |

---

## How It Works

### 1. K-Means Algorithm  
Implemented manually without sklearn.

### 2. Elbow & Silhouette Methods  
Evaluates K from **2 to 10**, computes:

- SSE
- Silhouette Score

### 3. Optimal K  
The script selects the best K based on **maximum silhouette score**.

### 4. Output  
Running `run_analysis.py` will generate:

- `final_clusters.png`
- Printed optimal K values

---

## How to Run
```
python run_analysis.py
```

Make sure `data.csv` is in the same directory.

---
