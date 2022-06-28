import numpy as np


def count_distance(cluster_1, cluster_2):
    united_cluster = np.concatenate((cluster_1, cluster_2), axis=0)

    # united_cluster
    centroid_united_cluster_x = united_cluster[:, 0].sum() / len(united_cluster)
    centroid_united_cluster_y = united_cluster[:, 1].sum() / len(united_cluster)

    united_cluster_distance = 0.

    for point in united_cluster:
        x, y = point
        united_cluster_distance += (x - centroid_united_cluster_x) ** 2 + (y - centroid_united_cluster_y) ** 2

    # cluster_1
    centroid_cluster_1_x = cluster_1[:, 0].sum() / len(cluster_1)
    centroid_cluster_1_y = cluster_1[:, 1].sum() / len(cluster_1)

    cluster_1_distance = 0.

    for point in cluster_1:
        x, y = point
        cluster_1_distance += (x - centroid_cluster_1_x) ** 2 + (y - centroid_cluster_1_y) ** 2

    # cluster_2
    centroid_cluster_2_x = cluster_2[:, 0].sum() / len(cluster_2)
    centroid_cluster_2_y = cluster_2[:, 1].sum() / len(cluster_2)

    cluster_2_distance = 0.

    for point in cluster_2:
        x, y = point
        cluster_2_distance += (x - centroid_cluster_2_x) ** 2 + (y - centroid_cluster_2_y) ** 2

    distance = united_cluster_distance - cluster_1_distance - cluster_2_distance

    return distance
