import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
from kmeans import k_means

def main():
    df = pd.read_csv('../iris.csv')

    df = df.drop(['species'], axis=1).to_numpy()

    k = 2

    clusters_indexes, centroids, clusters = k_means(df, k)

    print(f"Clusters: {clusters}")
    print(f"Centroids: {centroids}")
    print(f"Clusters Indexes: {clusters_indexes}")

    

main()