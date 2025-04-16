import preprocessing
from clustering.LoadData import LoadData
from clustering.DataFrame import DataFrame
from clustering.Normalization import Normalization
from clustering.K_Means import K_Means


def main(dataFileName: str, precentageReadingFromFile: int, k: int):
    return preprocessing.preprocessing(dataFileName, precentageReadingFromFile, k)

if __name__ == "__main__":
    # clusters, num_iterations = main(r"D:\FCAI-CU\Fourth Year\Second Semester\Data Mining\Assignments\Assignment 2\SS2025_Clustering_SuperMarketCustomers.csv", 100, 2)
    clusters, num_iterations = main(r"SS2025_Clustering_CreditCardData.csv", 50, 4)

    print(f"done in {num_iterations} iterations")
    for cluster in clusters:
        print('*' * 20)
        print(
            f"cluster name: {cluster.getName()} - num of points = {len(cluster.getClusterPoints())} - center = {(cluster.getCurrentLocation())}"
        )
        # print(f"points: {[x for x in cluster.getClusterPoints()]}")
        print('*' * 20)

