import sys


def clustering_evaluation(all_clusters, _):
    tested_clusters_number = len(*all_clusters[-1]) - 1

    points_number = len(*all_clusters[-1])

    clusters_silhouette_coefficient = list(range(tested_clusters_number))
    index = 0
    for clusters_number in range(2, 2 + tested_clusters_number):
        current_clusters_silhouette_sum = 0
        current_clusters = all_clusters[-clusters_number]
        for cluster in current_clusters:
            if len(cluster) == 1:
                continue
            for point in cluster:
                x, y = point

                average_intracluster_distance = 0.
                average_distance_to_the_nearest_cluster = sys.float_info.max
                for cluster_i in current_clusters:
                    current_distance = 0.
                    trigger = False
                    for point_i in cluster_i:
                        x_i, y_i = point_i
                        if x == x_i and y == y_i:
                            trigger = True
                        current_distance += ((x - x_i) ** 2 + (y - y_i) ** 2) ** (1 / 2)

                    if trigger:
                        average_intracluster_distance = current_distance / (len(cluster_i) - 1)
                    else:
                        current_distance /= len(cluster_i)
                        if current_distance < average_distance_to_the_nearest_cluster:
                            average_distance_to_the_nearest_cluster = current_distance

                current_point_silhouette = (average_distance_to_the_nearest_cluster - average_intracluster_distance) / \
                                           max([average_distance_to_the_nearest_cluster, average_intracluster_distance])

                current_clusters_silhouette_sum += current_point_silhouette

        clusters_silhouette_coefficient[index] = (clusters_number, current_clusters_silhouette_sum / points_number)
        index += 1

    max_silhouette_coefficient = 0.
    max_silhouette_clusters_number = 0.

    for clusters_number, current_clusters_silhouette_coefficient in clusters_silhouette_coefficient:
        if max_silhouette_coefficient < current_clusters_silhouette_coefficient:
            max_silhouette_coefficient = current_clusters_silhouette_coefficient
            max_silhouette_clusters_number = clusters_number

    return max_silhouette_clusters_number, clusters_silhouette_coefficient
