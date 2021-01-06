# Zadanie 1
print("Zadanie 1")


def sum_list(list_1, list_2):
    list_sum_1_2 = []

    for element_1, element_2 in zip(list_1, list_2):
        list_sum_1_2.append(element_1 + element_2)

    return list_sum_1_2


list_1 = [1, 2, 3, 4]
list_2 = [4, 5, 6, 7]
result_zad_1 = sum_list(list_1, list_2)

print(result_zad_1)
# Zadanie 2
print("Zadanie 2")


def index_min():
    list_zad_2 = [1, 0, 2, 5, 6, 99, 8, -3]
    return list_zad_2.index(min(list_zad_2))


print(index_min())

# Zadanie 3
print("Zadanie 3")


def change_list():
    list_zad_3 = [-9, 1, 2, 3, 30, -6, -4, 8, 101, -8]

    for i, element in enumerate(list_zad_3):
        if element < 0:
            list_zad_3[i] = -1
        else:
            list_zad_3[i] = 1

    return list_zad_3


print(change_list())

# Zadanie 4
print("Zadanie 4")


def half_list():
    list_zad_4 = [5, 45, 12, 1, 2, 5, 6, 7, 89, 4, 1, 2, 99]
    minus_p = -1
    plus_p = 1
    new_list_zad_4 = []
    div_half_list = int(len(list_zad_4) / 2)

    for index, element in enumerate(list_zad_4):
        if index <= div_half_list:
            new_list_zad_4.append(element * minus_p)
        else:
            new_list_zad_4.append(element * plus_p)
    return new_list_zad_4


print(half_list())

# Zadanie 5
print("Zadanie 5")


def intervals(low, up, steps):
    tab_zad_5_a = []
    tab_zad_5_b = []
    for i in range(low[0], up[0], steps[0]):
        tab_zad_5_a.append(i)
    for i in range(low[1], up[1], steps[1]):
        tab_zad_5_b.append(i)

    return tab_zad_5_a, tab_zad_5_b


print(intervals([1, 20], [20, 100], [3, 15]))

# Zadanie 6
print("Zadanie 6")


def elem_freq(list_zad_6, freq_p):
    return list_zad_6.count(freq_p)


list_zad_6 = [1, 1, 1, 1, 2, 3, 5, 6, 5, 5, 9, 8, 7, 7, 8]
freq_p = 1

print(elem_freq(list_zad_6, freq_p))

# Zadanie 7
print("Zadanie 7")


def euclidean_distance(dist_x, dist_y):
    result = (pow(dist_y[0] - dist_x[0], 2) + pow(dist_y[1] - dist_x[1], 2))
    return pow(result, .5)


dist_x = [-3, - 5]
dist_y = [6, 10]

print(euclidean_distance(dist_x, dist_y))

# Zadanie 8
print("Zadanie 8")


def link_list(list_zad_8_a, list_zad_8_b):
    tab_res_zad_8 = []
    for a, b in zip(list_zad_8_a, list_zad_8_b):
        tab_res_zad_8.append(a)
        tab_res_zad_8.append(b)
    return tab_res_zad_8


list_zad_8_a = [1, 2, 3]
list_zad_8_b = [4, 5, 6]

print(link_list(list_zad_8_a, list_zad_8_b))

# Zadanie 9
print("Zadanie 9")


def even(list_zad_9):
    list_even = []
    for a in list_zad_9:
        if a % 2 == 0:
            list_even.append(a)
    return list_even


list_zad_9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 45, 85, 90, 96, 88, 100]

print(even(list_zad_9))

# Zadanie 10
print("Zadanie 10")


def factorial(n):
    if n >= 1:
        return n * (n - 1)


print(factorial(10))
