import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Zadania 10
def make_3D(x, y):
    fig = plt.figure(figsize=(50, 50))
    ax = fig.gca(projection='3d')

    X, Y = np.meshgrid(x, y)
    Z = np.sqrt((X ** 2 + Y ** 2))

    ax.plot_surface(X, Y, Z, cmap='jet')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    plt.show()


x = np.arange(-52, 100, 2.4)
y = np.arange(-28, 81, 0.9)
result_zad_10 = make_3D(x, y)
