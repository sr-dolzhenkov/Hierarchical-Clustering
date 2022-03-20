import sys
import numpy as np


def calculate(data, count_distance):
    clusters = [np.array([[i[0], i[1]]]) for i in data]
    clusters_number = len(clusters)
    all_clusters = list(range(clusters_number))
    all_clusters[0] = clusters.copy()
    min_distance_list = []

    distances = np.zeros((clusters_number, clusters_number))

    def set_distances():
        for i in range(clusters_number - 1):
            for j in range(i + 1, clusters_number):
                distances[i, j] = count_distance(clusters[i], clusters[j])

    def find_min_distance():
        min_distance = sys.float_info.max
        i_num, j_num = 0, 0

        for i in range(clusters_number - 1):
            for j in range(i + 1, clusters_number):
                if min_distance > distances[i, j]:
                    min_distance = distances[i, j]
                    i_num = i
                    j_num = j

        min_distance_list.append(min_distance)

        return i_num, j_num

    def recount_distances(i_num, j_num):
        nonlocal distances
        distances = np.delete(distances, j_num, axis=0)
        distances = np.delete(distances, j_num, axis=1)

        for i in range(i_num):
            distances[i, i_num] = count_distance(clusters[i], clusters[i_num])

        for j in range(i_num + 1, clusters_number):
            distances[i_num, j] = count_distance(clusters[j], clusters[i_num])

    def unite_clusters(i_num, j_num):
        nonlocal clusters
        clusters[i_num] = np.concatenate((clusters[i_num], clusters[j_num]), axis=0)
        nonlocal clusters_number
        clusters_number -= 1
        del clusters[j_num]
        recount_distances(i_num, j_num)

    set_distances()

    while clusters_number != 1:
        unite_clusters(*find_min_distance())
        all_clusters[-clusters_number] = clusters.copy()

    return all_clusters, min_distance_list
