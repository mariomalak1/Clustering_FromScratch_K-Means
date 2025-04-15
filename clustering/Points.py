import math


class Points():
    # calculate distance from p1 to p2 by euclidean equation
    @staticmethod
    def euclideanEquation(p1, p2):
        if len(p1) != len(p2):
            raise RuntimeError("must p1 and p2 have the same features")
        sumOfSquaredDiff = 0
        for i in range(len(p1)):
            # get square diff between two features values
            squareOfDiff = math.pow((p1[i] - p2[i]), 2)
            # add it to sum
            sumOfSquaredDiff += squareOfDiff
        # get square root of the sum 
        result = math.sqrt(sumOfSquaredDiff)
        return result
