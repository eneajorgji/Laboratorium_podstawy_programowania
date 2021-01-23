import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Zadania 1
def simple_plot(a, b):
    plt.plot((a), label="red", color="red")
    plt.plot((b), label="blue", color="blue")

    plt.xlabel("x")
    plt.ylabel("y")

    plt.legend(bbox_to_anchor=(1.01, 1), title="Legenda", loc='upper left', ncol=1)

    plt.show()


a = [1, 4, 7, 10]
b = [2, 5, 8, 11]

result_simple_plot = simple_plot(a, b)
print(result_simple_plot)


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
# Zadania 4
# Zadania 5
# Zadania 6
# Zadania 7
# Zadania 8
# Zadania 9
# Zadania 10
