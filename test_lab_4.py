import numpy as np


# def third_composition(n, m):
#     third_matrix = np.fromfunction(lambda i, j: i + j, (n, m), dtype=int)
#     return third_matrix
#
#
# print(third_composition(9, 9))


def third_composition(n, m):
    half_n = int(n / 2)
    half_m = int(m / 2)

    up_left_one_fourth = np.full((half_n, half_m), 1)
    up_right_one_fourth = np.full((half_n, half_m), -2)

    down_left_one_fourth = np.full((half_n, half_m), 2)
    down_right_one_fourth = np.full((half_n, half_m), -1)

    first_up_concatenate = np.concatenate((up_left_one_fourth, up_right_one_fourth), axis=1)
    first_down_concatenate = np.concatenate((down_left_one_fourth, down_right_one_fourth), axis=1)

    full_matrix = np.concatenate((first_up_concatenate, first_down_concatenate), axis=0)

    return full_matrix


n = 100
m = 100
print(third_composition(n, m))
