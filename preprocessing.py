from clustering.LoadData import LoadData
from clustering.DataFrame import DataFrame
from clustering.Normalization import Normalization
from clustering.K_Means import K_Means


def preprocessingSuperMarketProb(precentageReadingFromFile, k):
    loadData = LoadData("../SS2025_Clustering_SuperMarketCustomers.csv/", precentageReadingFromFile, isLabeled=True)

    data = loadData.loadDataFromFile()

    dataFrame = DataFrame(data, loadData.labels)
    beforeNormalizationDataFrame = dataFrame.copy()

    # droppedFeature = dataFrame.dropFeature(0)

    normalization = Normalization(dataFrame)

    genderFeature = dataFrame.getFeature(1)

    # convert categorical data to numerical one
    genderToNumerical = normalization.convert_categorical_data_to_numerical(genderFeature)

    dataFrame.setFeatureData(1, genderToNumerical)

    normalization.setDataFrame(dataFrame)

    normalization.normalize_MinMax()
    newDataFrame = normalization.getDataFrame()

    # clusterMethod = K_Means(2, newDataFrame, False, [7, 145])
    clusterMethod = K_Means(k, newDataFrame, beforeNormalizationDataFrame)

    clusters, num_iterations = clusterMethod.run()

    dataAfterClusteringWithModification = clusterMethod.getRealDataFromClusters()

    outliers = clusterMethod.getOutliers()

    return clusters, num_iterations, dataAfterClusteringWithModification, outliers, beforeNormalizationDataFrame.labels

def preprocessingCreditCardProb(precentageReadingFromFile, k):
    loadData = LoadData("../SS2025_Clustering_CreditCardData.csv/", precentageReadingFromFile, isLabeled=True)

    data = loadData.loadDataFromFile()

    dataFrame = DataFrame(data, loadData.labels)
    dataFrame.dropNA()
    beforeNormalizationDataFrame = dataFrame.copy()

    droppedFeature = dataFrame.dropFeature(0)

    normalization = Normalization(dataFrame)

    normalization.normalize_MinMax()
    newDataFrame = normalization.getDataFrame()

    clusterMethod = K_Means(k, newDataFrame, beforeNormalizationDataFrame)

    clusters, num_iterations = clusterMethod.run()

    dataAfterClusteringWithModification = clusterMethod.getRealDataFromClusters()

    outliers = clusterMethod.getOutliers()

    return clusters, num_iterations, dataAfterClusteringWithModification, outliers, beforeNormalizationDataFrame.labels

def defaultPreprocessing(dataFileName, precentageReadingFromFile, k, isLabeld):
    loadData = LoadData(dataFileName, precentageReadingFromFile, isLabeled=isLabeld)

    data = loadData.loadDataFromFile()

    dataFrame = DataFrame(data, loadData.labels)
    beforeNormalizationDataFrame = dataFrame.copy()

    # drop customer_id field
    droppedFeature = dataFrame.dropFeature(0)

    normalization = Normalization(dataFrame)

    normalization.normalize_MinMax()
    newDataFrame = normalization.getDataFrame()

    clusterMethod = K_Means(k, newDataFrame, beforeNormalizationDataFrame)

    clusters, num_iterations = clusterMethod.run()

    dataAfterClusteringWithModification = clusterMethod.getRealDataFromClusters()

    outliers = clusterMethod.getOutliers()

    return clusters, num_iterations, dataAfterClusteringWithModification, outliers, beforeNormalizationDataFrame.labels


def preprocessing(dataFileName: str, precentageReadingFromFile: int, k: int):
    if dataFileName.find("SS2025_Clustering_SuperMarketCustomers.csv") != -1:
        print("super market")
        clusters, num_iterations, dataAfterClusteringWithModification, outliers, labels = preprocessingSuperMarketProb(precentageReadingFromFile, k)
    elif dataFileName.find("SS2025_Clustering_CreditCardData.csv") != -1:
        print("credit")
        clusters, num_iterations, dataAfterClusteringWithModification, outliers, labels = preprocessingCreditCardProb(precentageReadingFromFile, k)
    else:
        print("else")
        clusters, num_iterations, dataAfterClusteringWithModification, outliers, labels = defaultPreprocessing(dataFileName, precentageReadingFromFile, k, True)

    return clusters, num_iterations, dataAfterClusteringWithModification, outliers, labels
