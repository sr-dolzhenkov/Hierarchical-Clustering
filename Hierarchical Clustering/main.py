import numpy as np
import pathlib

from Data.DataCreation import save_data
from assembly import clustering

if __name__ == '__main__':
    save_data()
    data_path = pathlib.Path('Data/data.npy')
    data = np.load(data_path)

    clustering(5, data, 'SL', 'SM')
    clustering(5, data, 'CL', 'SM')
    clustering(5, data, 'UPGMA', 'SM')
    clustering(5, data, 'UPGMC', 'SM')
    clustering(5, data, 'WM', 'SM')

    pass
