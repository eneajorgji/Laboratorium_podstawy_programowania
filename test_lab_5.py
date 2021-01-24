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


# Zadania 6

def contour_plot(x, y):
    X, Y = np.meshgrid(x, y)
    Z = np.sqrt((X ** 2 + Y ** 2))
    CS = plt.contour(X, Y, Z)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.clabel(CS, inline=1, fontsize=10)

    plt.show()


x = np.arange(5, 15, 0.4)
y = np.arange(-2, 8, 0.3)
result_zad_6 = contour_plot(x, y)
