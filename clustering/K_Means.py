from .DataFrame import DataFrame
from .Cluster import Cluster

import random

class K_Means():
    MAX_NUMBER_OF_ITERATIONS = 4
    
    def __init__(self, k, dataFrame: DataFrame):
        self.k = k
        self.__dataFrame = dataFrame
        self.__clusters = []

        # to make data frame prepare points in list if it not make it before 
        self.__dataFrame.getPoints()

        for i in range(k):
            cluster = Cluster(f"c{i}")
            self.__clusters.append(cluster)

    # all logic of k-means here
    def run(self):
        self.__chooseRandomCentroidPointToEachCluster()
        self.clustering()
        self.updateAllClusterCentroids()
        
        counter = 0

        while True:
            self.clustering()
            
            if not self.isAllClustersTheSame():
                self.updateCentroidOfChangedClusters()
            else:
                break

            if counter >= K_Means.MAX_NUMBER_OF_ITERATIONS:
                break
        
        return self.__clusters
    
    # make each point be in specific cluster 
    def clustering(self):
        for point in self.__dataFrame.getPoints():
            distances = {}
            for cluster in self.__clusters:
                distances.update({cluster, cluster.distanceToPoint(point)})
            
            cluster = self.getNearestClusterFromDistances(distances)
            cluster.addPoint(point)
        
    # get random centroids for each clusters
    def __chooseRandomCentroidPointToEachCluster(self):
        for cluster in self.__clusters:
            pointIndex = random.randint(0, self.__dataFrame.numOfRows)
            centerPoint = self.__dataFrame.getRow(pointIndex)
            cluster.updateCenterLocation(centerPoint)
    
    # loop on clusters and update each cluster centroid
    def updateAllClusterCentroids(self):
        for cluster in self.__clusters:
            cluster.calcNewCenterLocation()

    def getClusters(self) -> list:
        return self.__clusters

    def getNearestClusterFromDistances(self, distances) -> Cluster:
        # ascending order sort
        sorted_distances = dict(sorted(distances.items(), key=lambda item: item[1]))
        return list(sorted_distances.items())[0]

    def isAllClustersTheSame(self):
        for cluster in self.__clusters:
            if cluster.isClusterCentroidChanged():
                return False
        return True
    

    def updateCentroidOfChangedClusters(self):
        for cluster in self.__clusters:
            if cluster.isClusterCentroidChanged():
                cluster.calcNewCenterLocation()

