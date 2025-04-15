from .DataFrame import DataFrame 

# take data frame 
# normalize using min_max normalization method
# can convert specific field to numerical if it's categorical
class Normalization():
    def __inti__(self, dataFrame: DataFrame):
        self.dataFrame = dataFrame
    
    def convert_categorical_data_to_numerical(self, featureData):
        pass

    def min_max_normalization(self):
        pass

