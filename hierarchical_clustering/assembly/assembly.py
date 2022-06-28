from hierarchical_clustering.calculation import calculate
from hierarchical_clustering.visualization import visualize_clusters

from hierarchical_clustering.sorting_strategies import single_linkage, complete_linkage, UPGMA, UPGMC, wards_method

from hierarchical_clustering.clustering_evaluation_methods import silhouette_method, e2_hypothesis

from hierarchical_clustering.metrics import v_measure

distance_calculation_methods = {'SL': single_linkage,
                                'CL': complete_linkage,
                                'UPGMA': UPGMA,
                                'UPGMC': UPGMC,
                                'WM': wards_method}

clustering_evaluation_methods = {'SM': silhouette_method,
                                 'E2H': e2_hypothesis}

measure = {'VM': v_measure}


def cluster(data, distance_calculation_method, clustering_evaluation_method):
    all_clusters, distance_list = calculate(data, distance_calculation_methods[distance_calculation_method])

    clusters_number, evaluation = \
        clustering_evaluation_methods[clustering_evaluation_method](all_clusters, distance_list.copy())

    visualize_clusters(clusters_number, all_clusters[-clusters_number],
                       distance_calculation_method, clustering_evaluation_method)
