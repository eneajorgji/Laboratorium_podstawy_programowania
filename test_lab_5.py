import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Zadania 2

def func_plot(x):
    value_of_func = pow(x, 2) - x * 4 + 8
    return value_of_func


vmin = 1
vmax = 25
step = .25

x = np.arange(vmin, vmax, step)

plt.plot(x, func_plot(x))
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.show()
