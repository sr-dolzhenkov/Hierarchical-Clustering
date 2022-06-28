import numpy as np

from assembly import cluster

if __name__ == '__main__':
    data = np.load('hierarchical_clustering/data.npy')

    sorting_strategies = ['SL', 'CL', 'UPGMA', 'UPGMC', 'WM']
    clustering_evaluation_methods = ['SM', 'E2H']

    for sorting_strategy in sorting_strategies:
        for clustering_evaluation_method in clustering_evaluation_methods:
            cluster(data, sorting_strategy, clustering_evaluation_method)
