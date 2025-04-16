from .Points import Points

class Cluster():
    def __init__(self, clusterName):
        self.__clusterName = clusterName
        self.__currentLocation = []
        self.__oldLocation = []
        self.__points = []
    
    # take list of new centers 
    # put the current location to the old one 
    def updateCenterLocation(self, newLocation: list):
        self.__oldLocation = self.__currentLocation.copy()
        self.__currentLocation = newLocation

    def addPoint(self, p: dict):
        self.__points.append(p)

    def removePoint(self, p: dict):
        counter = 0
        for point in self.__points:
            if(point.values() == p.values()):
                break
            counter += 1
        self.__points.pop(counter)

    def calcNewCenterLocation(self) -> list:
        if not self.__points:
            return self.__currentLocation
        
        num_points = len(self.__points)
        num_features = len(list(self.__points[0].values())) if num_points > 0 else 0
        
        new_center = []
        for feature_idx in range(num_features):
            try:
                # sum feature data in all points and divide it by num of points
                feature_sum = sum(list(point.value())[feature_idx] for point in self.__points)
                new_center.append(feature_sum / num_points)
            except (IndexError, TypeError) as e:
                print(f"Error calculating feature {feature_idx}: {e}")
                new_center.append(0)
        
        self.updateCenterLocation(new_center)
        return new_center

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

    # return true if the cluster centroid changed
    def isClusterCentroidChanged(self) -> bool:
        return self.__oldLocation != self.__currentLocation
    
    def getClusterPoints(self) -> list:
        return self.__points

    def getCurrentLocation(self):
        return self.__currentLocation

    def getName(self):
        return self.__clusterName