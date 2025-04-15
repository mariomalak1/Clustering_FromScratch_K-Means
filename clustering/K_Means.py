from .DataFrame import DataFrame
from random import random 

class K_Means():
    def __init__(self, k, dataFrame: DataFrame):
        self.k = k
        self.__dataFrame = dataFrame
        self.__clusters = []

    # all logic of k-means here
    def run(self):
        pass
    
    # make each point be in specific cluster 
    def clustering(self):
        pass
        
    # get random centroids for each clusters
    def __chooseRandomClustersCentroids(self):
        random.randint(3, 9)

    # loop on clusters and update each cluster centroid
    def updateClusterCentroids(self):
        pass


    def getClusters(self) -> list:
        pass

    def getNearestClusterFromDistances(self):
        pass

