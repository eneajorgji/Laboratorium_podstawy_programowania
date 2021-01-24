import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Zadania 8

def pie_plot(sizes, labels):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.show()


sizes = [45.7, 24.3, 9.5, 7.5, 3]
labels = ["Shareholder 1", "Shareholder 2", "Shareholder 3", "Shareholder 4", "Shareholder 5"]
result_zad_8 = pie_plot(sizes, labels)
