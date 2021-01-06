import numpy as np

def first_composition(n, m):
    upper_triangle = np.triu_indices(n)
    ones = np.ones((n, m))
    ones[upper_triangle] = -1

    new_mat = ones - np.diag(np.diag(ones))

    return new_mat


n = 6
m = 6

resuult_firt_comp = first_composition(n, m)

print(resuult_firt_comp)
