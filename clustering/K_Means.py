from .DataFrame import DataFrame

class K_Means():
    def __init__(self, k, dataFrame: DataFrame):
        self.k = k
        self.__dataFrame = dataFrame
    
    def cluster(self):
        pass
    
    def __chooseRandomClustersCentroids(self):
        pass

    def __calculateCentroids(self):
        pass

