# Dirichlet Process Means Clustering Challenge

Copy the starter file from 
```/home/ubuntu/clustering_lesson/dmp.py``` 

The dirichlet process is a method of clustering without knowing the number of clusters ahead of time. The means part of the name indicates that we will be defining clusters by taking the mean of the members in the cluster. Something like this algorithm may be used for example 2 in the list of clustering related bioinformatics problems. Here are the steps:
 
&nbsp;&nbsp;  I. Add the first point in your data as the first center. A single data point is a numpy array.
  
&nbsp;&nbsp;  II. Iterate through all of the points in your data, calculating the distance between the current point and all existing centers. 
  
&nbsp;&nbsp;&nbsp;&nbsp; A. If the point falls within a certain threshold distance of the center, add that point to that center's cluster
  
&nbsp;&nbsp;&nbsp;&nbsp; B. If the point does not fall within a certain threshold distance of the center, add that point to the list of centers
    
&nbsp;&nbsp; III. Once you have gone through the Dirichlet Process, you do the means part. Redefine the centers of each cluster to be the average of all points in the cluster. 
  
&nbsp;&nbsp; IV. Repeat steps II and III either until an iteration provides no change in the assignment of points to centers, or a maximum number of cycles is reached. 

**HINT 1:** You will need an array of arrays to keep track of which points are in which clusters. Array 1 will contain the indices of the points in the first cluster and so on. If a point moves from its current cluster, remember to take it out of the old cluster before adding it to its new cluster.
  
**HINT 2:** You will need an array of arrays to contain the centers of each cluster. The first array will be the center of the first cluster and so on.

