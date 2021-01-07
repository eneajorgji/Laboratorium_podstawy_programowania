import numpy as np


def second_composition(n, m):
    upper_triangle = np.triu_indices(n, 1)
    ones = np.cumsum(np.ones((n, m)), axis=0)
    ones[upper_triangle] = -1

    return ones


n = 6
m = 6

result_second_composition = second_composition(n, m)

print(result_second_composition)
