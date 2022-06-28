import numpy as np


def clustering_evaluation(all_clusters, F):
    points_number = len(*all_clusters[-1])

    def fix_F():
        for i in range(len(F) - 1):
            if F[i] > F[i + 1]:
                F[i + 1] = F[i]

    def delta(y0, y1, y2, y3):
        y1 = y1 - y0
        y2 = y2 - y0
        y3 = y3 - y0
        return (19 * y1 ** 2 - 11 * y2 ** 2 + 41 * y3 ** 2 + 12 * y1 * y2 - 64 * y1 * y3 - 46 * y2 * y3) / 245

    def get_y(q):
        y = np.arange(len(F), dtype=np.float64)

        for i in range(len(F)):
            y[i] = F[i] + q * i

        return y

    fix_F()

    q_step = 0.1
    q = 0.
    Q = []
    last_k = 0
    q_start = 0.
    start_i = 3

    while last_k != len(F):
        y = get_y(q)

        for i in range(start_i, len(y)):
            if delta(y[i - 3], y[i - 2], y[i - 1], y[i]) > 0.:
                k = i + 1
                start_i = i

                if last_k == 0:
                    last_k = k

                if last_k != k:
                    Q.append((q_start, q - q_step, last_k))
                    q_start = q
                    last_k = k

                break

            if i == len(y) - 1:
                Q.append((q_start, q - q_step, last_k))
                q_start = q
                last_k = len(y)

        q += q_step

    else:
        Q.append((q_start, np.inf, last_k))

    cluster_number = points_number - Q[-3][2]

    return cluster_number, Q
