import numpy as np

# Zadanie 1
print("Zadanie ")


def difference_array(array_a, array_b):
    diffs = array_a - array_b
    return diffs


array_a = np.array([1, 2, 6])
array_b = np.array([0, 5, 3])

print(difference_array(array_a, array_b))

# Zadanie 2
print("Zadanie 2")


def random_array(value_n, value_m):
    random = np.random.rand(value_n, value_m)
    return random


print(random_array(2, 5))

# Zadanie 3
print("Zadanie 3")


def add_padding():
    array_zad_3 = np.array([[1, 3, 2], [8, 5, 2]])
    b = np.array([[9], [9]])
    array_zad_3_c = np.hstack([array_zad_3, b])
    return array_zad_3_c


print(add_padding())

# Zadanie 4
print("Zadanie 4")


def count_value(val_number, array_zad_4):
    count_number = 0

    for i in array_zad_4:
        if i == val_number:
            count_number += 1
    return count_number


array_zad_4 = np.array([1, 3, 2, 2, 2, 2, 3])
val_number = 2

print(count_value(val_number, array_zad_4))

# Zadanie 5
print("Zadanie 5")


def sum_rows(a):
    return array_zad_5.sum(axis=1)


array_zad_5 = np.array([[5, 3, 2], [6, 5, 3]])
result_zad_5 = sum_rows(array_zad_5)
print(result_zad_5)

# Zadanie 6
print("Zadanie 6")


def normalize(array_zad_6):
    row_sum = array_zad_6.sum(axis=1)
    normalized_matrix = array_zad_6 / row_sum[:, np.newaxis]

    return normalized_matrix


array_zad_6 = np.array([[1, 2, 2], [4, 5, 8]])
norm_matrix = normalize(array_zad_6)

print(norm_matrix)

# Zadanie 7
print("Zadanie 7")

# Zadanie 8
print("Zadanie 8")

# Zadanie 9
print("Zadanie 9")

# Zadanie 10
print("Zadanie 10")
