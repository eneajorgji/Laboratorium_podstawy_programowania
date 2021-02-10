import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Zadanie 1
arr_zad_1 = np.random.uniform(0, 1, size=(10, 5))  # uniform distribution

print("Zadanie 1\n", arr_zad_1)

# Zadanie 2
df = pd.DataFrame(arr_zad_1, columns=["col1", "col2", "col3", "col4", "col5"])
print("Zadanie 2 \n", df)

# Zadanie 3
df_to_sum = df.where(df < .5, True)
df_to_sum = df_to_sum.where(df_to_sum > .5, False)
print("Zadanie 3 \n", df_to_sum)

sum_of_bigger = df_to_sum.sum()
print("Zadanie 3 \n", sum_of_bigger)

# Zadanie 4
plt.bar(sum_of_bigger, height=50)
plt.show()

write_to_csv = sum_of_bigger.to_csv("DF_zad_4.csv")

print("Zadanie 4 \n")

# Zadanie 5
df_2 = df.append(df, ignore_index=True)
print("Zadanie 5 \n", df_2)

# Zadanie 6
arr_zad_6 = np.random.uniform(0, 1, size=(20, 5))
df_zad_6 = pd.DataFrame(arr_zad_6, columns=["col1", "col2", "col3", "col4", "col5"])
# print("Zadanie 6 \n", df_zad_6)

df_concat = df_2.copy()
df_concat.columns = ["col6", "col7", "col8", "col9", "col10"]
df_zad_6 = pd.concat([df_zad_6, df_concat], axis=1)
print("Zadanie 6 \n", df_zad_6)

df_zad_6_sort = df_zad_6.sort_values(by=["col1", "col6"])
print("Zadanie 6 - sort by col1 and col 6 \n", df_zad_6_sort)

df_zad_6_sort_index = df_zad_6_sort.sort_index()
print("Zadanie 6 - sort index \n", df_zad_6_sort_index)

# wykres pudelkowy
plt.boxplot(df_zad_6_sort_index)
plt.show()
