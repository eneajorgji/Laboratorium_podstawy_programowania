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


bigger = 0
smaller = 0

for index, row in df.iterrows():
    for item in row:
        if item > .5:
            bigger += 1
        else:
            smaller += 1

print("bigger: ", bigger)
print("smaller: ", smaller)

# Zadanie 4
x = ["bigger", "smaller"]
y = [bigger, smaller]

plt.bar(x, width=0.4, height=y)
plt.show()

#
DF_y = pd.DataFrame(y)

write_to_csv = DF_y.to_csv("DF_zad_4.csv")

print("Zadanie 4 \n")
