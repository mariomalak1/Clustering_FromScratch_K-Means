import random

from .DataFrame import DataFrame
from .Cluster import Cluster


class K_Means():
    MAX_NUMBER_OF_ITERATIONS = 50
    
    def __init__(self, k, dataFrame: DataFrame, dataFrameBeforeEdit: DataFrame, chooseRandomly = True, indexCentroids = None):
        self.k = k
        self.__dataFrame = dataFrame
        self.__clusters = []
        self.chooseRandomly = chooseRandomly
        self.indexCentroids = indexCentroids
        self.oldDataFrame = dataFrameBeforeEdit


        if(not chooseRandomly):
            if (not indexCentroids or len(indexCentroids) < k):
                raise ValueError(f"if not choose randomly the data need indexCentroids param with {k} numbers as the clusters")

        # to make data frame prepare points in list if it not make it before 
        self.__dataFrame.getPoints(makeNewOne=True)

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
        counter = 0
        for point in points:
            distances = {}
            for cluster in self.__clusters:
                distances[cluster] = cluster.distanceToPoint(point)
            
            cluster = self.getNearestClusterFromDistances(distances)

            self.migratePointToCluster({counter: point}, cluster)

            counter += 1
        
    # get random centroids for each clusters
    def __chooseRandomCentroidPointToEachCluster(self):
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

    def migratePointToCluster(self, point: dict, toCluster: Cluster):
        # point is dict of { index of point: point values}
        if point in toCluster.getClusterPoints():
            return
        else:
            for cluster in self.__clusters:
                if point in cluster.getClusterPoints():
                    cluster.removePoint(point)
        
        toCluster.addPoint(point)

    # to return each cluster data in form of the old form of it
    def getRealDataFromClusters(self):
        clustersData = []
        for _ in self.__clusters:
            clustersData.append([])

        for i in range(len(self.__clusters)):
            for point in self.__clusters[i].getClusterPoints():
                pointIndex = list(point.keys())[0]
                oldPointForm = self.oldDataFrame.getRow(pointIndex)
                clustersData[i].append(oldPointForm)

        return clustersData

    # get distance of each point to the nearest cluster, {distance: pointIndex}
    def __distanceOfPointsToThierClusters(self):
        distances = []
        for cluster in self.__clusters:
            for point in cluster.getClusterPoints():
                distances.append(
                    {cluster.distanceToPoint(list(point.values())[0]): list(point.keys())[0]}
                )
        return distances

    def __getRealDataOfOutliers(self):
        distances = sorted(self.__distanceOfPointsToThierClusters(), key=lambda d: list(d.keys())[0])
        newDistances = []

        for point in distances:
            pointIndex = list(point.values())[0]
            oldPointForm = self.oldDataFrame.getRow(pointIndex)
            newDistances.append({list(point.keys())[0]: oldPointForm})

        return newDistances

    def getOutliers(self):
        distances = self.__getRealDataOfOutliers()

        def get_percentile(dict_list, percentile):
            keys = [list(dist.keys())[0] for dist in dict_list]
            keys.sort()

            index = (percentile / 100) * (len(keys) - 1)
            lower = int(index)
            upper = lower + 1

            if upper >= len(keys):
                return keys[lower]
            return keys[lower] + (keys[upper] - keys[lower]) * (index - lower)

        Q1 = get_percentile(distances, 25)
        Q3 = get_percentile(distances, 75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = []
        for point in distances:
            if list(point.keys())[0] < lower_bound or list(point.keys())[0] > upper_bound:
                outliers.append(list(point.values())[0])

        return outliers



