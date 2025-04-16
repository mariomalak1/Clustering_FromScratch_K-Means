from clustering.LoadData import LoadData 
from clustering.DataFrame import DataFrame
from clustering.Normalization import Normalization
from clustering.K_Means import K_Means

def main():
    # loadData = LoadData("../SS2025_Clustering_CreditCardData.csv/", 100, isLabeled=True)
    loadData = LoadData("../SS2025_Clustering_SuperMarketCustomers.csv/", 100, isLabeled=True)
    data = loadData.loadDataFromFile()

    dataFrame = DataFrame(data)
    # print(dataFrame)
    droppedFeature = dataFrame.dropFeature(0)
    # print(dataFrame)
    
    # print(dataFrame.numOfRows)
    dataFrame.dropNA()
    # print(dataFrame.numOfRows)

    normalization = Normalization(dataFrame)
    
    genderFeature = dataFrame.getFeature(0)

    lis = normalization.convert_categorical_data_to_numerical(genderFeature)
    
    dataFrame.setFeatureData(0, lis)

    normalization.setDataFrame(dataFrame)

    normalization.normalize_MinMax()
    
    
    newDataFrame = normalization.getDataFrame()

    clusterMethod = K_Means(3, newDataFrame, True, [5, 4, 113])

    clusters = clusterMethod.run()

    cluster1 = clusters[0].getClusterPoints() 
    cluster2 = clusters[1].getClusterPoints() 
    cluster3 = clusters[2].getClusterPoints() 

    if cluster1.issubset(cluster2):
        print("1 with 2")
        common = cluster1.intersection(cluster2)

        for i in common:
            print(i)

    if cluster1.issubset(cluster3):
        print("1 with 3")
        common = cluster1.intersection(cluster3)

        for i in common:
            print(i)

    if cluster2.issubset(cluster3):
        print("2 with 3")
        common = cluster2.intersection(cluster3)

        for i in common:
            print(i)


    for cluster in clusters:
        print("-" * 50)
        print(len(cluster.getClusterPoints()))
        print("-" * 50)



main()

