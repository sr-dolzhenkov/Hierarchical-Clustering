from calculation import calculate
from visualization import visualize_clusters

import matplotlib.pyplot as plt

from SortingStrategies import single_linkage, \
                              complete_linkage, \
                              UPGMA, \
                              UPGMC, \
                              wards_method

from ClusteringEvaluationMethod import silhouette_method

distance_calculation_method = {'SL': single_linkage,
                               'CL': complete_linkage,
                               'UPGMA': UPGMA,
                               'UPGMC': UPGMC,
                               'WM': wards_method}

clustering_evaluation = {'SM': silhouette_method}


def clustering(clusters_number, data, distance_calculation_method_name, clustering_evaluation_name):
    all_clusters = calculate(data, distance_calculation_method[distance_calculation_method_name])

    evaluation = clustering_evaluation[clustering_evaluation_name](clusters_number, all_clusters)

    print(evaluation)

    plt.plot(range(len(evaluation)), [i[2] for i in evaluation])
    plt.show()

    visualize_clusters(clusters_number, all_clusters[-clusters_number])
