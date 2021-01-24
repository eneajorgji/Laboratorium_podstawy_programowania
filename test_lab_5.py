import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# x = np.arange(0, 6, 0.1)
# y = np.arange(0, 6, 0.1)
# X, Y = np.meshgrid(x, y)
# Z = np.sin(X) * np.cos(Y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.contour(X, Y, Z)
# plt.show()


# Zadania 7
def box_plot(n, m):
    matrix = np.random.randn(n, m)
    plt.boxplot(matrix)

    plt.xlabel("numer wketora")
    plt.ylabel("liczba probek")

    plt.show()


result_zad_7 = box_plot(9, 12)
