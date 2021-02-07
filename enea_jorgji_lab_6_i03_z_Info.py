import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Zadanie 1
arr_zad_1 = np.random.randint(2, size=(10, 5))

print("Zadanie 1\n", arr_zad_1)

# Zadanie 2

df = pd.DataFrame(arr_zad_1, columns=["col1", "col2", "col3", "col4", "col5"])
print("Zadanie 2 \n", df)

# Zadanie 3
bigger_than_o5 = 0

for key, value in df.iteritems():
    df["col1"] = df["col1"].apply(if value > 0.5)

    # print("Zadanie 3 \n")

    # Zadanie 4
    # Zadanie 5
    # Zadanie 6
