import matplotlib.pyplot as plt


def visualize_clusters(clusters_number, data):
    if clusters_number == 1:
        plt.scatter(data[0][:, 0], -data[0][:, 1])
        plt.show()
    elif clusters_number > 1:
        for cluster in data:
            if len(cluster) != 1:
                plt.scatter(cluster[:, 0], -cluster[:, 1])
            else:
                x, y = cluster[0]
                plt.scatter(x, -y)
        plt.show()
    else:
        print('Incorrect clusters number')
