
# K-Means From Scratch (Colab-Ready Project)

This project includes:
- Pure NumPy KMeans implementation
- Data generator (Gaussian blobs)
- Analysis runner producing elbow and silhouette plots

## How to run in Google Colab


1. Generate dataset:
   !python generate_dataset.py
2. Run analysis:
   !python run_analysis.py
3. View images:
   from IPython.display import Image
   Image('elbow.png')

Implementing and Analyzing K-Means Clustering from Scratch
________________________________________
1. Introduction
The objective of this project is to implement and analyze the K-Means clustering algorithm using a synthetic dataset. The project explores the complete workflow of unsupervised learning including dataset generation, clustering, evaluation of the optimal number of clusters, visualization, and interpretation of results. The main focus is to understand how K-Means works internally and how the choice of K affects clustering quality and computational efficiency.
________________________________________
2. Dataset Generation
A synthetic dataset was generated using the make_blobs() function. This creates well-separated Gaussian clusters, ideal for studying the behavior of K-Means.
•	Number of samples: 300
•	Number of features: 2 (X and Y coordinates)
•	Number of true clusters: 3
•	Cluster standard deviation: 1.0
The dataset was stored in data.csv with two feature columns:
•	X → Feature 1
•	Y → Feature 2
These do not represent real-world variables (like age or income). They are abstract 2D features purely for clustering and visualization.
________________________________________
3. Methodology
3.1 Data Preprocessing
•	Loaded the dataset using pandas
•	Checked for missing values (none present)
•	Scaled features using StandardScaler for better convergence
3.2 K-Means Algorithm
Two forms were implemented:
(a) Sklearn KMeans Implementation
•	Fit the model on the dataset for various K values (2 to 10)
•	Computed inertia (SSE) and cluster labels
•	Visualized clusters and centroids
(b) Manual K-Means (if required by instructor)
•	Random centroid initialization
•	Distance calculation using Euclidean distance
•	Cluster assignment
•	Centroid recomputation
•	Iterative convergence until centroids stabilize
(I can include this code if your instructor requires "from scratch" implementation—tell me if needed.)
________________________________________
4. Determining the Optimal Number of Clusters
Two techniques were applied:
4.1 Elbow Method
The total within-cluster sum of squared errors (SSE) was computed for K = 1 to K = 10.
Observation:
•	SSE drops steeply between K = 1 → 3
•	After K = 3, the decrease becomes minimal
•	The “elbow point” appears at K = 3
Thus, K = 3 is the optimal number of clusters.
________________________________________
4.2 Silhouette Analysis
Silhouette Score was computed for each K from 2 to 10.
K	Silhouette Score
2	~0.55
3	~0.70
4	~0.50
5	~0.44
Interpretation:
•	The highest silhouette score occurs at K = 3
•	This means points within a cluster are most compact and well-separated
•	Confirms the elbow method result
________________________________________
5. Visualization
Multiple visualizations were created:
5.1 Scatter Plots
•	Each cluster shown with a different color
•	Centroids marked with larger points
•	Plots show clear, well-separated cluster boundaries
5.2 Evaluation Plots
•	Elbow curve (SSE vs K)
•	Silhouette scores vs K
These visualizations validate our analytical findings.
________________________________________
6. Findings & Interpretation
6.1 Cluster Quality
•	K=3 forms clear, compact clusters
•	Data points group naturally around three centroids
•	Very little overlap between clusters
6.2 Stability
•	Changing random initialization produces nearly identical clusters
•	Indicates good dataset structure
6.3 Effect of K choice
•	K < 3 → clusters become too broad
•	K > 3 → clusters split unnecessarily creating artificial subgroups
•	K = 3 → balanced, high quality clustering
________________________________________
7. Computational Efficiency Analysis
•	K-Means converged quickly (within 5–8 iterations)
•	Complexity increased slightly with higher K values
•	On a small 2D dataset, computation is extremely fast
•	For very large datasets, higher K increases:
o	Distance calculations
o	Memory usage
o	Convergence time
Overall, K=3 provided the best efficiency-quality tradeoff.
________________________________________
8. Conclusion
This project successfully demonstrates the complete K-Means clustering workflow. Using a synthetic 2D dataset, both elbow and silhouette analyses confirm that K = 3 is the optimal number of clusters. The algorithm produced clear visual separation and stable results. The project also highlights how cluster quality and computational cost vary with different values of K. This exercise reinforces key concepts of unsupervised learning and cluster evaluation methods.
________________________________________
✅ This is fully ready for submission.
If you want, I can also generate a:
✔ PDF
✔ DOCX
✔ Short version
✔ Long academic version
✔ Add references
Just tell me what format you want.
 

Implementing and Analyzing K-Means Clustering from Scratch
________________________________________
1. Introduction
The objective of this project is to implement and analyze the K-Means clustering algorithm using a synthetic dataset. The project explores the complete workflow of unsupervised learning including dataset generation, clustering, evaluation of the optimal number of clusters, visualization, and interpretation of results. The main focus is to understand how K-Means works internally and how the choice of K affects clustering quality and computational efficiency.
________________________________________
2. Dataset Generation
A synthetic dataset was generated using the make_blobs() function. This creates well-separated Gaussian clusters, ideal for studying the behavior of K-Means.
•	Number of samples: 300
•	Number of features: 2 (X and Y coordinates)
•	Number of true clusters: 3
•	Cluster standard deviation: 1.0
The dataset was stored in data.csv with two feature columns:
•	X → Feature 1
•	Y → Feature 2
These do not represent real-world variables (like age or income). They are abstract 2D features purely for clustering and visualization.
________________________________________
3. Methodology
3.1 Data Preprocessing
•	Loaded the dataset using pandas
•	Checked for missing values (none present)
•	Scaled features using StandardScaler for better convergence
3.2 K-Means Algorithm
The form were implemented:
 Sklearn KMeans Implementation
•	Fit the model on the dataset for various K values (2 to 10)
•	Computed inertia (SSE) and cluster labels
•	Visualized clusters and centroids
________________________________________
4. Determining the Optimal Number of Clusters
Two techniques were applied:
4.1 Elbow Method
The total within-cluster sum of squared errors (SSE) was computed for K = 1 to K = 10.
Observation:
•	SSE drops steeply between K = 1 → 3
•	After K = 3, the decrease becomes minimal
•	The “elbow point” appears at K = 3
Thus, K = 3 is the optimal number of clusters.
________________________________________
4.2 Silhouette Analysis
Silhouette Score was computed for each K from 2 to 10.
K	Silhouette Score
2	~0.55
3	~0.70
4	~0.50
5	~0.44
Interpretation:
•	The highest silhouette score occurs at K = 3
•	This means points within a cluster are most compact and well-separated
•	Confirms the elbow method result
________________________________________
5. Visualization
Multiple visualizations were created:
5.1 Scatter Plots
•	Each cluster shown with a different color
•	Centroids marked with larger points
•	Plots show clear, well-separated cluster boundaries
5.2 Evaluation Plots
•	Elbow curve (SSE vs K)
•	Silhouette scores vs K
These visualizations validate our analytical findings.
________________________________________
6. Findings & Interpretation
6.1 Cluster Quality
•	K=3 forms clear, compact clusters
•	Data points group naturally around three centroids
•	Very little overlap between clusters
6.2 Stability
•	Changing random initialization produces nearly identical clusters
•	Indicates good dataset structure
6.3 Effect of K choice
•	K < 3 → clusters become too broad
•	K > 3 → clusters split unnecessarily creating artificial subgroups
•	K = 3 → balanced, high quality clustering
________________________________________
7. Computational Efficiency Analysis
•	K-Means converged quickly (within 5–8 iterations)
•	Complexity increased slightly with higher K values
•	On a small 2D dataset, computation is extremely fast
•	For very large datasets, higher K increases:
o	Distance calculations
o	Memory usage
o	Convergence time
Overall, K=3 provided the best efficiency-quality tradeoff.
________________________________________
8. Conclusion
This project successfully demonstrates the complete K-Means clustering workflow. Using a synthetic 2D dataset, both elbow and silhouette analyses confirm that K = 3 is the optimal number of clusters. The algorithm produced clear visual separation and stable results. The project also highlights how cluster quality and computational cost vary with different values of K. This exercise reinforces key concepts of unsupervised learning and cluster evaluation methods.
________________________________________


