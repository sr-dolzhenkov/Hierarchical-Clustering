import numpy as np

from Data import save_data

from assembly import clustering
from assembly import stages_of_stable_clustering
from assembly import cluster_shift

if __name__ == '__main__':
    save_data()
    data = np.load('Data/data.npy')

    # clustering(data, 'SL', 'SM')
    # clustering(data, 'CL', 'SM')
    # clustering(data, 'UPGMA', 'SM')
    # clustering(data, 'UPGMC', 'SM')
    # clustering(data, 'WM', 'SM')

    # clustering(data, 'SL', 'E2H')
    # clustering(data, 'CL', 'E2H')
    # clustering(data, 'UPGMA', 'E2H')
    # clustering(data, 'UPGMC', 'E2H')
    # clustering(data, 'WM', 'E2H')

    # stages_of_stable_clustering(data, 'SL')
    # stages_of_stable_clustering(data, 'CL')
    # stages_of_stable_clustering(data, 'UPGMA')
    # stages_of_stable_clustering(data, 'UPGMC')
    # stages_of_stable_clustering(data, 'WM')

    # cluster_shift('SL')
    # cluster_shift('CL')
    # cluster_shift('UPGMA')
    # cluster_shift('UPGMC')
    # cluster_shift('WM')

    pass
