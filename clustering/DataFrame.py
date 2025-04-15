# convert list of rows to rows and features
# can access specific row -> list, and can access specific column of data -> list
class DataFrame():
    def __init__(self, data: list):
        if(len(data) == 0):
            raise ValueError("Must provide data parameter")
        
        self.features = {}
        self.numOfRows = 0
        self.numOfFeatures = 0

        row = data[0]

        # for each col add it in features, that will have the data after that
        for i in range(len(row)):
            self.numOfFeatures += 1
            self.features[i] = []


        for row in data:
            # check that the data have the same features 
            if(len(row) > self.numOfFeatures):
                raise ValueError("Data must have the same feature length")

            for i in range(self.numOfFeatures):
                self.features[i].append(row[i])

            self.numOfRows += 1


    def addRow(self, rowOfData: list):
        if (len(rowOfData) > self.numOfFeatures):
            raise ValueError("Data must have the same feature length")

        for i in range(self.numOfFeatures):
            self.features[i].append(rowOfData[i])


    def dropRow(self, numOfRow):
        if(numOfRow < 0 or numOfRow > self.numOfRows):
            return ValueError("Index of row required is more than the number of data")


        for feature_values in self.features.values():
            feature_values.pop(numOfRow)
        
        self.numOfRows -= 1
    

    def getRow(self, numOfRow):
        if(numOfRow < 0 or numOfRow > self.numOfRows):
            return ValueError("Index of row required is more than the number of data")

        dataPoint = []

        for featureData in self.features:
            dataPoint.append(featureData[numOfRow])

        return dataPoint
    
    def getFeature(self, numOfFeature):
        if(numOfFeature < 0 or numOfFeature > self.numOfFeatures):
            return ValueError("Index of required feature is more than the number of features")

        return self.features.get(numOfFeature)

    def setFeatureData(self, numOfFeature, data: list):
        if(len(data) != self.numOfRows):
            return ValueError("number of data not the same")
 
        if(numOfFeature < 0 or numOfFeature > self.numOfFeatures):
            return ValueError("Index of required feature is more than the number of features")

        self.features.update({numOfFeature: data})

    def dropFeature(self, numOfFeature):
        if(numOfFeature < 0 or numOfFeature > self.numOfFeatures):
            return ValueError("Index of required feature is more than the number of features")

        self.features.pop(numOfFeature)
        self.numOfFeatures -= 1

        # rename features after that feature again
        for i in range(numOfFeature, self.numOfFeatures):
            # Step 1: Remove the old key and get its value
            value = self.features.pop(i + 1)
            self.features[i] = value


    def dropNA(self):
        rowsIndexToDrop = []
        for _, values in self.features.items():
            for i in range(len(values)):
                if(values[i] == None or values[i] == ''):
                    rowsIndexToDrop.append(i)

        rowsIndexToDrop = sorted(rowsIndexToDrop, reverse=True)

        for i in rowsIndexToDrop:
            self.dropRow(i)


    def fillNA():
        pass
