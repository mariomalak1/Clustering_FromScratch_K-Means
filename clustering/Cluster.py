class Cluster():
    def __init__(self, clusterName):
        self.__clusterName = clusterName
        self.__currentLocation = []
        self.__oldLocation = []
        self.__points = []
    
    # take list of new centers 
    # put the current location to the old one 
    def updateCenterLocation(self, newLocation: list):
        self.__oldLocation = self.__currentLocation
        self.__currentLocation = newLocation

    def addPoint(self, p: list):
        self.__points.append(p)

    def removePoint(self, p: list):
        self.__points.remove(p)

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
