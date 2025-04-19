import preprocessing

def main(dataFileName: str, precentageReadingFromFile: int, k: int):
    return preprocessing.preprocessing(dataFileName, precentageReadingFromFile, k)

if __name__ == "__main__":
    # clusters, num_iterations, dataAfterClusteringWithModification, labels = main(r"SS2025_Clustering_SuperMarketCustomers.csv", 100, 2)
    clusters, num_iterations, dataAfterClusteringWithModification, beforeNormalizationDataFrame = main(r"SS2025_Clustering_CreditCardData.csv", 20, 3)

    print(f"done in {num_iterations} iterations")
    # for i in range(len(clusters)):
    #     print('*' * 20)
    #     print(
    #         f"cluster name: {clusters[i].getName()} - num of points = {len(clusters[i].getClusterPoints())} - center = {(clusters[i].getCurrentLocation())}"
    #     )
    #     for j in range(5):
    #         print('*' * 5)
    #         print(f"point {j}: {dataAfterClusteringWithModification[i][j]}")
    #         print('*' * 5)
    #
    #     print('*' * 20)

