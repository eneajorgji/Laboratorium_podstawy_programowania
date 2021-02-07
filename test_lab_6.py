import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HASLO = "bardzobardzodlugiehaslo"

E = len(HASLO)  #funkcja len() zwraca liczbę znaków
i = 1

while(i * i < E):
    i = i + 1
print(i)
print(HASLO)
WYNIK = []
print(WYNIK)

x = 0
while x < i:
    y = 0
    while y < i:
        if (y * i + x) > E - 1:
            WYNIK.append("X")
        else:
            WYNIK.append(HASLO[y * i + x])
        y = y + 1
    x = x + 1
print(WYNIK)