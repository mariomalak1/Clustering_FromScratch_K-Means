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

    def calcNewCenterLocation(self) -> list:
        if not self.__points:
            return self.__currentLocation
        
        points_list = list(self.__points)
        num_points = len(points_list)
        num_features = len(points_list[0]) if num_points > 0 else 0
        
        new_center = []
        for feature_idx in range(num_features):
            try:
                # sum feature data in all points and divide it by num of points
                feature_sum = sum(point[feature_idx] for point in points_list)
                
                new_center.append(feature_sum / num_points)
            except (IndexError, TypeError) as e:
                print(f"Error calculating feature {feature_idx}: {e}")
                new_center.append(0)  # Fallback value
        
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
    
    def getClusterPoints(self) -> set:
        return self.__points

    def getCurrentLocation(self):
        return self.__currentLocation
    