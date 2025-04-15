from .DataFrame import DataFrame 

# take data frame 
# normalize using min_max normalization method
# can convert specific field to numerical if it's categorical
class Normalization():
    def __init__(self, dataFrame: DataFrame):
        self.__dataFrame = dataFrame
    
    def convert_categorical_data_to_numerical(self, featureData):
        unique_categories = list(set(featureData))
        # make number for every unique category
        feature_map = {feature: i for i, feature in enumerate(unique_categories)}
        
        def mapCategoryToNumber(element):
            return feature_map.get(element)

        # make new list of feature that have numerical data        
        numerical_data = map(mapCategoryToNumber, featureData)

        return list(numerical_data)

    def __min_max_normalization(self, feature):
        min_val = min(feature)
        max_val = max(feature)
        if max_val == min_val:
            return [0.5 for _ in feature]

        return [(x - min_val) / (max_val - min_val) for x in feature]

    def normalize_MinMax(self):
        self.__checkAllFeaturesNumeric_or_tryParse()
        for i in range(len(self.__dataFrame.features)):
            normalizedFeature = self.__min_max_normalization(self.__dataFrame.getFeature(i))
            self.__dataFrame.setFeatureData(i, normalizedFeature)
        
    def getDataFrame(self):
        return self.__dataFrame

    def setDataFrame(self, dataFrame: DataFrame):
        self.__dataFrame = dataFrame


    def __checkAllFeaturesNumeric_or_tryParse(self):
        for _, values in self.__dataFrame.features.items():
            for i in range(len(values)):
                if type(values[i]) is not int:
                    try:
                        values[i] = int(values[i])
                    except:
                        raise TypeError("unsupported operand type(s) for -: 'str' and 'str'")
