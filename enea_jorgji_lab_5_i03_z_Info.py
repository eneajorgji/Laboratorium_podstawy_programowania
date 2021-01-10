import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Zadania 1
def simple_plot(a, b):
    plt.plot((a), label="red", color="red")
    plt.plot((b), label="blue", color="blue")

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.legend(bbox_to_anchor=(1.01, 1),title="Legenda", loc='upper left', ncol=1)

    plt.show()


a = [1, 4, 7, 10]
b = [2, 5, 8, 11]

res_simple_plot = simple_plot(a, b)
print(res_simple_plot)

# Zadania 2
# Zadania 3
# Zadania 4
# Zadania 5
# Zadania 6
# Zadania 7
# Zadania 8
# Zadania 9
# Zadania 10
