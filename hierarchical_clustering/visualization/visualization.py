import matplotlib.pyplot as plt


def visualize_clusters(clusters_number, data, distance_calculation_method, clustering_evaluation_method):
    if clusters_number == 1:
        plt.scatter(data[0][:, 0], -data[0][:, 1])
        plt.title(f'Clustering\n{distance_calculation_method} and {clustering_evaluation_method}')
        plt.show()
    elif clusters_number > 1:
        for cluster in data:
            if len(cluster) != 1:
                plt.scatter(cluster[:, 0], -cluster[:, 1])
            else:
                x, y = cluster[0]
                plt.scatter(x, -y)
        plt.title(f'Clustering\n{distance_calculation_method} and {clustering_evaluation_method}')
        plt.show()
