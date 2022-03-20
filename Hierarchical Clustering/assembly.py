import numpy as np
import pathlib

from calculation import calculate
from visualization import visualize_clusters

import matplotlib.pyplot as plt

from SortingStrategies import single_linkage, \
                              complete_linkage, \
                              UPGMA, \
                              UPGMC, \
                              wards_method

from ClusteringEvaluationMethod import silhouette_method, \
                                       e2_hypothesis

from Metrics import v_measure

from Data.DataCreation import resave_data

distance_calculation_method = {'SL': single_linkage,
                               'CL': complete_linkage,
                               'UPGMA': UPGMA,
                               'UPGMC': UPGMC,
                               'WM': wards_method}

clustering_evaluation = {'SM': silhouette_method,
                         'E2H': e2_hypothesis}

measure = {'VM': v_measure}


def clustering(data, distance_calculation_method_name, clustering_evaluation_name):
    all_clusters, distance_list = calculate(data, distance_calculation_method[distance_calculation_method_name])

    clusters_number, evaluation = clustering_evaluation[clustering_evaluation_name](all_clusters, distance_list.copy())

    print(distance_calculation_method_name, clustering_evaluation_name)
    # print(distance_list)
    print(evaluation)

    # plt.scatter(range(len(distance_list)), distance_list)
    # plt.show()

    # clusters_number = 5

    # v_measure(all_clusters[-clusters_number])
    v_measure(all_clusters)

    visualize_clusters(clusters_number, all_clusters[-clusters_number])


def stages_of_stable_clustering(data, distance_calculation_method_name):
    clustering_evaluation_name = 'E2H'
    all_clusters, distance_list = calculate(data, distance_calculation_method[distance_calculation_method_name])

    clusters_number, evaluation = clustering_evaluation[clustering_evaluation_name](all_clusters, distance_list.copy())

    print(distance_calculation_method_name, clustering_evaluation_name)
    print(distance_list)
    print(evaluation)

    for i in evaluation:
        clusters_number = -i[2]
        v_measure(all_clusters[-clusters_number])
        visualize_clusters(-clusters_number, all_clusters[-clusters_number])


def cluster_shift(distance_calculation_method_name):
    clustering_evaluation_name = 'SM'
    print(distance_calculation_method_name, clustering_evaluation_name)

    steps_number = 30
    step = -1
    variances = np.zeros(steps_number)
    centroid_variances = np.zeros(steps_number)
    clusters_number_silhouette = np.zeros(steps_number)

    for i in range(steps_number):
        data_path = pathlib.Path('Data/data.npy')
        data = np.load(data_path)

        all_clusters, distance_list = calculate(data, distance_calculation_method[distance_calculation_method_name])

        clusters_number, evaluation = clustering_evaluation[clustering_evaluation_name](all_clusters, distance_list.copy())

        # print(evaluation)

        def calculate_variance(cluster):
            centroid_x = cluster[:, 0].sum() / len(cluster)
            # centroid_y = cluster[:, 1].sum() / len(cluster)

            square_centroid_x = (cluster[:, 0] ** 2).sum() / len(cluster)
            # square_centroid_y = (cluster[:, 1] ** 2).sum() / len(cluster)

            variance = square_centroid_x - centroid_x ** 2
            variances[i] = variance
            clusters_number_silhouette[i] = clusters_number

        calculate_variance(all_clusters[-1][0])

        def calculate_centroid_variance(cluster):
            centroid_x_list = np.zeros(len(cluster))
            # centroid_y_list = np.zeros(len(cluster))

            for j in range(len(cluster)):
                current_cluster = cluster[j]
                centroid_x_list[j] = current_cluster[:, 0].sum() / len(current_cluster)
                # centroid_y_list[j] = current_cluster[:, 1].sum() / len(current_cluster)

            centroid_x = centroid_x_list.sum() / len(cluster)
            # centroid_y = centroid_y_list[:, 1].sum() / len(cluster)

            square_centroid_x = (centroid_x_list ** 2).sum() / len(cluster)
            # square_centroid_y = (centroid_y_list[:, 1] ** 2).sum() / len(cluster)

            variance = square_centroid_x - centroid_x ** 2
            centroid_variances[i] = variance
            clusters_number_silhouette[i] = clusters_number

        calculate_centroid_variance(all_clusters[-clusters_number])

        # visualize_clusters(clusters_number, all_clusters[-clusters_number])

        resave_data(3, step)

    # print(variances)
    # print(centroid_variances)
    print(clusters_number_silhouette)

    plt.scatter(range(steps_number), variances)
    plt.scatter(range(steps_number), centroid_variances)
    # plt.scatter(range(steps_number), clusters_number_silhouette)
    plt.grid(axis='y')
    plt.xlabel('Step')
    plt.show()
