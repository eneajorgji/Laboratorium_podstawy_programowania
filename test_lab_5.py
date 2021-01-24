import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Zadania 5
def heat_plot(matrix_n, matrix_m):
    matrix = np.random.random((matrix_n, matrix_m))

    plt.imshow(matrix, cmap='jet', interpolation='nearest')
    plt.colorbar()

    plt.show()


result_heat_plot = heat_plot(15, 15)

print(result_heat_plot)
