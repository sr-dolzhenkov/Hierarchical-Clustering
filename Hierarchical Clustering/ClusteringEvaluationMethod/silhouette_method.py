import sys
import numpy as np

def clustering_evaluation(clusters_number, all_clusters):
    evaluation = list(range(12))
    for i in range(-12, -1):
        silhouette = []
        current_clusters = all_clusters[i]
        for cluster in current_clusters:
            for point in cluster:
                x, y = point

                average_intracluster_distance = 0.
                average_distance_to_the_nearest_cluster = sys.float_info.max
                current_distance = 0.
                trigger = False
                for cluster_i in current_clusters:
                    for point_i in cluster_i:
                        x_i, y_i = point_i
                        if x == x_i and y == y_i:
                            trigger = True
                        current_distance += ((x - x_i) ** 2 + (y - y_i) ** 2) ** (1 / 2)

                    if trigger:
                        average_intracluster_distance = current_distance / len(cluster_i) - 1
                        trigger = False
                    else:
                        current_distance /= len(cluster_i)
                        if current_distance < average_distance_to_the_nearest_cluster:
                            average_distance_to_the_nearest_cluster = current_distance

                current_silhouette = (average_distance_to_the_nearest_cluster - average_intracluster_distance) / \
                                 max([average_distance_to_the_nearest_cluster, average_intracluster_distance])

                silhouette += [[x, y, current_silhouette]]

        evaluation[i] = silhouette.copy()

    return evaluation[clusters_number]
