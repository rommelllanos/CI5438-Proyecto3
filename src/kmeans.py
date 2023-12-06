import numpy as np
import random
import matplotlib.pyplot as plt
import sys

def k_means(data, k):
    # Paso 1: Escoger aleatoriamente los centroides μ1, ... , μK
    n_samples, n_features = data.shape
    centroids = data[np.random.choice(n_samples, k, replace=False)]
    iteration = 0

    def euclidean_distance(a, b):
        return np.sqrt(np.sum((a - b) ** 2))

    # Paso 3: Por cada Xi
    def assign_clusters(data, centroids):
        clusters = [[] for _ in range(k)]
        for idx, sample in enumerate(data):
            # Paso 3.1: Determinar el centroide μK que minimice ||xi − μk ||2
            distances = np.array([euclidean_distance(sample, centroid) for centroid in centroids])
            closest_centroid = np.argmin(distances)

            #Paso 3.2: Asignar xi al cluster k correspondiente al centroide μk
            clusters[closest_centroid].append(idx)
        return clusters

    # Paso 4: Recalcular los centroides como la media de los xi pertenecientes a su cluster
    def calculate_centroids(data, clusters, current_centroids):
        new_centroids = []

        for cluster_index, cluster_data_indices in enumerate(clusters):
            if cluster_data_indices:
                cluster_data_points = data[cluster_data_indices]
                
                mean_centroid = np.mean(cluster_data_points, axis=0)
                new_centroids.append(mean_centroid)
            else:
                new_centroids.append(current_centroids[cluster_index])

        return np.array(new_centroids)

    # Paso 2: Mientras no haya convergencia de asignaciones, repetir paso 3 y paso 4
    while True:
        iteration = iteration + 1
        sys.stdout.write(f'\r{iteration}')
        sys.stdout.flush()

        clusters_indexes = assign_clusters(data, centroids)
        new_centroids = calculate_centroids(data, clusters_indexes, centroids)

        if np.all(new_centroids == centroids):
            break
        centroids = new_centroids
        # Convert cluster indexes to cluster values
        clusters = [data[cluster].tolist() for cluster in clusters_indexes]



    return clusters_indexes, centroids, clusters