# Zadanie 1
print("Zadanie 1")
list_1 = [1, 2, 3, 4]
list_2 = [4, 5, 6, 7]

for element_1, element_2 in zip(list_1, list_2):
    print(element_1 + element_2)

# Zadanie 2
print("Zadanie 2")
list__kart_1 = [1, 2, 3]
list_kart_2 = [4, 5, 6]

for i in range(len(list__kart_1)):
    for j in range(len(list_kart_2)):
        print(list__kart_1[i], list_kart_2[j])

# Zadanie 3
print("Zadanie 3")
list_zad_3 = [1, 2, 2, 3, 5, 6, 6, 7, 8, 9]
unique_list = []

for element in list_zad_3:
    if element not in unique_list:
        unique_list.append(element)

print(unique_list)

# Zadanie 4
print("Zadanie 4")
list_zad_4 = [99, 88, 45, 78, 54, 123, 69, 2]

print("Indeks najmniejszy wartosci w liscie jest: ", list_zad_4.index(min(list_zad_4)))

##################################
# Zadanie 5
print("Zadanie 5")
list_a_zad_5 = [1, 2, 3, 4, 5]
value_x = 5
value_sum = 0

for index, a_number in enumerate(list_a_zad_5):
    value_sum = value_sum + (a_number * (value_x ** index))

print("Suma szeregu wynosi: ", value_sum)

# Zadanie 6
print("Zadanie 6")
list_zad_6 = [99, 88, 45, 78, 54, 123, 69, 2]

max_element = max(list_zad_6)
print("Najwiekszy element jest: ", max_element)

# Zadanie 7
print("Zadanie 7")
list_zad_7 = [-9, 1, 2, 3, 30, -6, -4, 8, 101, -8]

for i, element in enumerate(list_zad_7):
    if element < 0:
        list_zad_7[i] = -1
    else:
        list_zad_7[i] = 1

print("Lista poo zmiany wartosci", list_zad_7)

# Zadanie 8
print("Zadanie 8")
list_zad_8 = []
n = 5
potega = 5

for i in range(potega + 1):
    list_zad_8.append(n ** i)

print("Lista zlozona z kolejnych wartosci poteg", list_zad_8)

# Zadanie 9
print("Zadanie 9")
ciag_fibonacci = [0, 1]
n_razy = 10 - 2
count = 0

# ciag_fibonacci.append(ciag_fibonacci[0] + ciag_fibonacci[1])
while count < n_razy:
    ciag_fibonacci.append(ciag_fibonacci[-2] + ciag_fibonacci[-1])
    count = count + 1

print(f"Wartosc ciagu Fibonacciego dla zadanego rozmiaru n {n_razy + 2}:", ciag_fibonacci)

# Zadanie 10
print("Zadanie 10")
list_zad_10 = [5, 45, 12, 1, 2, 5, 6, 7, 89, 4, 1, 2]
minus_p = -1
plus_p = 1
new_list_zad_10 = []
half_list = int(len(list_zad_10) / 2)

for index, element in enumerate(list_zad_10):
    if index <= half_list:
        new_list_zad_10.append(element * minus_p)
    else:
        new_list_zad_10.append(element * plus_p)

print("Lewa polowe wypelni wartoscia -p, prawa polowe wypelni wartoscia p", new_list_zad_10)
