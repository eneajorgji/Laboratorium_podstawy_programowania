# # Zadanie 1
# liczba_a = int(input("Podaj liczbe a: "))
# liczba_b = int(input("Podaj liczbe b: "))
#
# suma_a_i_b = liczba_a + liczba_b
#
# print(suma_a_i_b)
#
# # Zadanie 2
# licz_a = int(input("Podaj a: "))
# licz_b = int(input("Podaj b: "))
#
# if licz_a != 0:
#     licz_x = -(licz_b / licz_a)
# else:
#     print("liczba a nie moze byc 0")
#
# print(licz_x)
#
# Zadanie 3
pole_a = int(input("Podaj pole a: "))
pole_b = int(input("Podaj pole b: "))

pole_prost = pole_a * pole_b

print(pole_prost)

# Zadanie 4
r = int(input("Podaj R: "))
objetosc_kuli = 4 / 3 * 3.14 * r ** 3
print(objetosc_kuli)

# # Zadanie 5
# x = 8
# y = 9
# wartosc_funkcji = x ** 2 - x * y + 4
#
# print(wartosc_funkcji)
#
#
# # Zadanie 6
# def silnia(n):
#     if n >= 1:
#         return n * (n - 1)
#
#
# print(silnia(4))

# Zadania 7
for i in range(2, 13):
    if i % 4 == 0:
        print("liczby podzielne bez reszty przez 4: ", i)

for i in range(5, 19):
    if i % 5 == 0:
        print("liczby podzielne bez reszty przez 5: ", i)

# Zadania 8
for i in range(5):
    print(i * "*")
