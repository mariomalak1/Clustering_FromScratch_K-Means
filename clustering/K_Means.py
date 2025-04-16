from .DataFrame import DataFrame
from .Cluster import Cluster

import random

class K_Means():
    MAX_NUMBER_OF_ITERATIONS = 50
    
    def __init__(self, k, dataFrame: DataFrame, chooseRandomly = True, indexPoints = None):
        self.k = k
        self.__dataFrame = dataFrame
        self.__clusters = []
        self.chooseRandomly = chooseRandomly
        self.indexPoints = indexPoints
        

        if(not chooseRandomly):
            if (not indexPoints or len(indexPoints) < k):
                raise ValueError(f"if not choose randomly the data need indexPoints param with {k} numbers as the clusters")

        # to make data frame prepare points in list if it not make it before 
        self.__dataFrame.getPoints()

        for i in range(k):
            cluster = Cluster(f"c{i}")
            self.__clusters.append(cluster)

    # all logic of k-means here
    def run(self):
        if (self.chooseRandomly):
            self.__chooseRandomCentroidPointToEachCluster()
        else:
            points = self.__dataFrame.getPoints()
            for i in range(len(self.__clusters)):
                centerPoint = points[i]
                self.__clusters[i].updateCenterLocation(centerPoint)

        self.clustering()
        self.updateAllClusterCentroids()

        num_iterations = 0

        while True:
            self.clustering()
            self.updateAllClusterCentroids()

            if num_iterations >= K_Means.MAX_NUMBER_OF_ITERATIONS:
                break

            if self.isAllClustersTheSame():
                break

            num_iterations += 1

        return self.__clusters, num_iterations
    
    # make each point be in specific cluster 
    def clustering(self):
        points = self.__dataFrame.getPoints()
        for point in points:
            distances = {}
            for cluster in self.__clusters:
                distances[cluster] = cluster.distanceToPoint(point)
            
            cluster = self.getNearestClusterFromDistances(distances)

            self.migratePointToCluster(point, cluster)
        
    # get random centroids for each clusters
    def __chooseRandomCentroidPointToEachCluster(self, ):
        points = self.__dataFrame.getPoints()
        for cluster in self.__clusters:
            pointIndex = random.randint(0, len(points) - 1)
            centerPoint = points[pointIndex]
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
        return list(sorted_distances.items())[0][0]

    def isAllClustersTheSame(self):
        for cluster in self.__clusters:
            if cluster.isClusterCentroidChanged():
                return False
        return True
    

    def updateCentroidOfChangedClusters(self):
        for cluster in self.__clusters:
            if cluster.isClusterCentroidChanged():
                cluster.calcNewCenterLocation()

    def migratePointToCluster(self, point, toCluster: Cluster):
        if point in toCluster.getClusterPoints():
            return
        else:
            for cluster in self.__clusters:
                if point in cluster.getClusterPoints():
                    cluster.removePoint(point)
        
        toCluster.addPoint(point)

