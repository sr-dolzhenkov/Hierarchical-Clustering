def count_distance(cluster_1, cluster_2):
    distance = 0.
    for i_point in cluster_1:
        i_x, i_y = i_point
        for j_point in cluster_2:
            j_x, j_y = j_point

            distance += ((i_x - j_x) ** 2 + (i_y - j_y) ** 2) ** (1/2)

    distance /= len(cluster_1) * len(cluster_2)

    return distance
