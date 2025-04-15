from .DataFrame import DataFrame
from .Cluster import Cluster

from random import random 

class K_Means():
    def __init__(self, k, dataFrame: DataFrame):
        self.k = k
        self.__dataFrame = dataFrame
        self.__clusters = []
        
        for i in range(k):
            cluster = Cluster(f"c{i}")
            self.__clusters.append(cluster)

    # all logic of k-means here
    def run(self):
        pass
    
    # make each point be in specific cluster 
    def clustering(self):
        pass
        
    # get random centroids for each clusters
    def __chooseRandomClustersCentroids(self):
        pass
        # random.randint(3, 9)

    # loop on clusters and update each cluster centroid
    def updateClusterCentroids(self):
        for cluster in self.__clusters:
            cluster.calcNewCenterLocation()


    def getClusters(self) -> list:
        return self.__clusters

    def getNearestClusterFromDistances(self):
        pass

