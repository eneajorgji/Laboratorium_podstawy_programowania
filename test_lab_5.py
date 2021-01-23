import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Zadania 3
def scatter_plot(a, b):
    a = [3, 1, 4, 7, 10, 8, 0]
    b = [2, 5, 8, 11, -6, -3, 4]

    plt.scatter(a, b)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    plt.show()


a = [1, 4, 7, 10]
b = [2, 5, 8, 11]

result_zad_3 = scatter_plot(a, b)
print(result_zad_3)
