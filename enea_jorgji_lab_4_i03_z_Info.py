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


# dla mnie slowo "dlugosc" jest dwuznaczne. Czy chodzi o wynik dlugosci wektora,
# czy ilosc elemnentow?
# Zalozylem ze chodzi o ilosc elementow w tym wektorze

def to_matrix(vector_zad_7):
    n_div_2 = int(len(vector_zad_7) / 2)

    new_matrix = np.resize(vector_zad_7, (n_div_2, n_div_2))

    return new_matrix


vector_zad_7 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
result_to_matrix = to_matrix(vector_zad_7)
print(result_to_matrix)

# Zadanie 8
print("Zadanie 8")


def first_composition(n, m):
    upper_triangle = np.triu_indices(n)
    ones = np.ones((n, m))
    ones[upper_triangle] = -1

    new_matrix = ones - np.diag(np.diag(ones))

    return new_matrix


n = 6
m = 6

result_first_composition = first_composition(n, m)

print(result_first_composition)

# Zadanie 9
print("Zadanie 9")


def second_composition(n, m):
    upper_triangle = np.triu_indices(n, 1)
    ones = np.cumsum(np.ones((n, m)), axis=0)
    ones[upper_triangle] = -1

    return ones


n = 10
m = 10
result_second_composition = second_composition(n, m)
print(result_second_composition)

# Zadanie 10
print("Zadanie 10")


def third_composition(n, m):
    half_n = int(n / 2)
    half_m = int(m / 2)

    up_left_one_fourth = np.full((half_n, half_m), 1)
    up_right_one_fourth = np.full((half_n, half_m), -2)

    down_left_one_fourth = np.full((half_n, half_m), 2)
    down_right_one_fourth = np.full((half_n, half_m), -1)

    first_line_up_concatenate = np.concatenate((up_left_one_fourth, up_right_one_fourth), axis=1)
    second_line_down_concatenate = np.concatenate((down_left_one_fourth, down_right_one_fourth), axis=1)

    full_matrix = np.concatenate((first_line_up_concatenate, second_line_down_concatenate), axis=0)

    return full_matrix


n = 100
m = 100
print(third_composition(n, m))
