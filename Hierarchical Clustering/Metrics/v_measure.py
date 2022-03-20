import numpy as np

from sklearn.metrics.cluster import v_measure_score as v_measure

true_data = np.array([
        # first cluster
        [(74, 10),
         (79, 11),
         (70, 13),
         (76, 13),
         (73, 14),
         (81, 14),
         (68, 16),
         (76, 16),
         (67, 18),
         (71, 18),
         (78, 18),
         (74, 19),
         (71, 21)],
        # second cluster
        [(27, 22),
         (24, 24),
         (28, 24),
         (31, 24),
         (24, 25),
         (27, 25),
         (26, 26),
         (29, 26),
         (32, 26),
         (30, 27),
         (25, 28),
         (27, 28),
         (29, 28),
         (34, 28),
         (31, 29),
         (27, 30),
         (29, 30),
         (32, 30),
         (33, 30),
         (29, 32),
         (33, 32),
         (31, 33)],
        # third cluster
        [(27, 64),
         (22, 67),
         (31, 67),
         (26, 69),
         (31, 70),
         (29, 72),
         (24, 74),
         (28, 67),
         (23, 70),
         (26, 72)],
        # fourth cluster
        [(60, 54),
         (61, 54),
         (64, 54),
         (59, 55),
         (61, 56),
         (63, 56),
         (57, 57),
         (59, 57),
         (60, 58),
         (62, 58),
         (59, 59),
         (61, 59),
         (63, 59),
         (57, 60),
         (60, 60),
         (62, 60),
         (62, 61),
         (63, 61),
         (58, 62),
         (60, 62),
         (62, 63),
         (64, 56),
         (64, 58),
         (64, 60),
         (65, 57)],
        # fifth cluster
        [(72, 58),
         (69, 59),
         (70, 59),
         (71, 60),
         (72, 60),
         (67, 61),
         (69, 61),
         (73, 61),
         (69, 62),
         (71, 62),
         (67, 63),
         (70, 63),
         (72, 63),
         (64, 65),
         (66, 64),
         (69, 64),
         (74, 64),
         (67, 65),
         (68, 65),
         (70, 65),
         (72, 65),
         (65, 66),
         (63, 67),
         (68, 67),
         (70, 67),
         (72, 67),
         (66, 68),
         (71, 68),
         (64, 69),
         (69, 69),
         (66, 70),
         (68, 70),
         (66, 62)]
    ], dtype=object)


def get_labels(data):
    labels_true = np.array([])

    a = 0

    for i in data:
        cluster = np.ones(len(i)) * a
        a += 1
        labels_true = np.concatenate((labels_true, cluster))

    return labels_true


def count_measure(pred_data):
    for i in [1, 3, 4, 9, 14, 16, 25, 35, 59, 79, 93]:
        labels_true = get_labels(true_data)
        labels_pred = get_labels(pred_data[-i])

        v_measure_score = v_measure(labels_true, labels_pred)

        print(i, 'v_measure_score: ', v_measure_score)
