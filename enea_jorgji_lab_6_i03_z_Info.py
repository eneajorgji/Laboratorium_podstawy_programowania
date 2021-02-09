import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Zadanie 1
arr_zad_1 = np.random.uniform(0, 1, size=(10, 5))  # uniform distribution

print("Zadanie 1\n", arr_zad_1)

# arr_zad_1_uniformdist = np.random.uniform(0, 1, size=(10, 5))
# print("arr zad 1 uniformdist \n", arr_zad_1_uniformdist)

# Zadanie 2
df = pd.DataFrame(arr_zad_1, columns=["col1", "col2", "col3", "col4", "col5"])
print("Zadanie 2 \n", df)

# Zadanie 3
# Zliczyc ile wartosci w zadanej kolumnie jest wiekszych od 0.5, a ile mniejszych od 0.5.
bigger_than_o5 = 0
smaller_than_o5 = 0

subset_df = df[df["col2"] >= .5]
column_count = subset_df.count()

print(column_count)

# for key, value in df.iteritems():

# print(key, bigger_than_o5)

# print("Zadanie 3 \n")

# Zadanie 4
# Zadanie 5
df_2 = df.append(df, ignore_index=True)
print(df_2)

# Zadanie 6
arr_zad_6 = np.random.randint(2, size=(20, 5))
df_zad_6 = pd.DataFrame(arr_zad_6, columns=["col1", "col2", "col3", "col4", "col5"])
print(df_zad_6)

df_zad_6_joined = pd.concat([df_zad_6, df_2], axis=1)
print(df_zad_6_joined)
