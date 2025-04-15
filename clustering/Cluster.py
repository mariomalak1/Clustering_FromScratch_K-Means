class Cluster():
    def __init__(self, clusterName):
        self.__clusterName = clusterName
        self.__currentLocation = []
        self.__oldLocation = []
        self.points = []
    
    # take list of new centers 
    # put the current location to the old one 
    def updateCenterLocation(self, newLocation: list):
        pass

    def addPoint(self, p: list):
        pass

    def removePoint(self, p: list):
        pass

    # calculate the new center of the the cluster and update the center location
    def calcNewCenterLocation(self) -> list:
        pass
    
    # calculate distance between the center location to specific point
    def distanceToPoint(self, p: list) -> int:
        pass

    def isClusterCentroidChanged(self) -> bool:
        pass
    
    def getClusterPoints(self) -> list:
        pass
