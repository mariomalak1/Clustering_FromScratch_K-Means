from clustering.LoadData import LoadData 
from clustering.DataFrame import DataFrame
from clustering.Normalization import Normalization


def main():
    # loadData = LoadData("../SS2025_Clustering_CreditCardData.csv/", 100, isLabeled=True)
    loadData = LoadData("../SS2025_Clustering_SuperMarketCustomers.csv/", 100, isLabeled=True)
    data = loadData.loadDataFromFile()

    dataFrame = DataFrame(data)
    print(dataFrame)
    droppedFeature = dataFrame.dropFeature(0)
    print(dataFrame)
    
    print(dataFrame.numOfRows)
    dataFrame.dropNA()
    print(dataFrame.numOfRows)

    normalization = Normalization(dataFrame)
    
    genderFeature = dataFrame.getFeature(0)

    lis = normalization.convert_categorical_data_to_numerical(genderFeature)
    
    dataFrame.setFeatureData(0, lis)

    normalization.setDataFrame(dataFrame)

    normalization.normalize_MinMax()
    
    print(dataFrame)

main()

