def count_distance(cluster_1, cluster_2):
    centroid_1_x = cluster_1[:, 0].sum() / len(cluster_1)
    centroid_1_y = cluster_1[:, 1].sum() / len(cluster_1)

    centroid_2_x = cluster_2[:, 0].sum() / len(cluster_2)
    centroid_2_y = cluster_2[:, 1].sum() / len(cluster_2)

    distance = ((centroid_1_x - centroid_2_x) ** 2 + (centroid_1_y - centroid_2_y) ** 2) ** (1/2)

    return distance
