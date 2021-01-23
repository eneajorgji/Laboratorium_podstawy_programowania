import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Zadania 4

def bar_plot(x, y):
    plt.bar(x, width=1, height=y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xticks([1, 2, 3, 4, 5, 6])

    plt.show()


# y = np.array([[1, 8], [2, 5], [3, 9], [4, 5]])

x = [1, 2, 3, 4, 5, 6]
y = [8, 5, 6, 3, 5, 6]

reslut_zad_4 = bar_plot(x, y)

print(reslut_zad_4)
