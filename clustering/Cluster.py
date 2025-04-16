from .Points import Points

class Cluster():
    def __init__(self, clusterName):
        self.__clusterName = clusterName
        self.__currentLocation = []
        self.__oldLocation = []
        self.__points = set()
    
    # take list of new centers 
    # put the current location to the old one 
    def updateCenterLocation(self, newLocation: list):
        self.__oldLocation = self.__currentLocation.copy()
        self.__currentLocation = newLocation

    def addPoint(self, p: list):
        self.__points.add(tuple(p))

    def removePoint(self, p: list):
        self.__points.remove(tuple(p))

    # calculate the new center of the the cluster and update the center location
    def calcNewCenterLocation(self) -> list:
        if len(self.__points) == 0:
            return self.__currentLocation

        lis = []
        numOfFeatureInPoints = len(list(self.__points)[0])
        for i in range(numOfFeatureInPoints):
            try:
                sumOfFeature = [x for x in list(self.__points)[i]]
                sumOfFeatures = sum(sumOfFeature)
                lis.append( (sumOfFeatures / numOfFeatureInPoints) )
            except:
                print(f"error in zft calcNewCenterLocation i = {i} and num of features = {numOfFeatureInPoints}")
                print(f"list(self.__points)[i] = {list(self.__points)}")
                lis.append(0)
        self.updateCenterLocation(lis)

    # calculate distance between the center location to specific point
    def distanceToPoint(self, p: list) -> int:
        # try:
        dis = Points.euclideanEquation(self.__currentLocation, p)
        return dis
        # except:
            # print("error in euclideanEquation")
            # print(f"len of current = {len(self.__currentLocation)} and current = {self.__currentLocation}")
            # print(f"len of p = {len(p)} and p = {p}")
            # print("done error")
    
    def isClusterCentroidChanged(self) -> bool:
        return self.__oldLocation != self.__currentLocation
    
    def getClusterPoints(self) -> set:
        return self.__points

    def getCentroid(self):
        return self.__currentLocation