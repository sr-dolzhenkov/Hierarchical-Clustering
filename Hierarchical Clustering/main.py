import numpy as np
import pathlib

from Data.DataCreation import save_data
from Data.DataCreation import resave_data

from assembly import clustering
from assembly import stages_of_stable_clustering
from assembly import cluster_shift

from sklearn.cluster import AgglomerativeClustering
from sklearn import metrics

if __name__ == '__main__':
    save_data()
    data_path = pathlib.Path('Data/data.npy')
    data = np.load(data_path)

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
