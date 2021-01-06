import numpy as np


def second_composition(n, m):
    upper_triangle = np.triu_indices(n)
    ones = np.ones((n, m))
    ones[upper_triangle] = -1

    return new_mat


n = 6
m = 6

