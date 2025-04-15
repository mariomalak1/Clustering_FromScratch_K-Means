from .DataFrame import DataFrame 

# take data frame 
# normalize using min_max normalization method
# can convert specific field to numerical if it's categorical
class Normalization():
    def __init__(self, dataFrame: DataFrame):
        self.dataFrame = dataFrame
    
    def convert_categorical_data_to_numerical(self, featureData):
        unique_categories = list(set(featureData))
        # make number for every unique category
        feature_map = {feature: i for i, feature in enumerate(unique_categories)}
        
        def mapCategoryToNumber(element):
            return feature_map.get(element)

        # make new list of feature that have numerical data        
        numerical_data = map(mapCategoryToNumber, featureData)

        return list(numerical_data)

    def __min_max_normalization(self):
        pass

    def normalize_MinMax():
        pass
