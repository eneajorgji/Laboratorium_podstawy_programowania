import numpy as np
import matplotlib.pyplot as plt


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
def bar_plot(x, y):
    plt.bar(x, width=1, height=y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xticks([1, 2, 3, 4, 5, 6])

    plt.show()


# y = np.array([[1, 8], [2, 5], [3, 9], [4, 5]])

x = [1, 2, 3, 4, 5, 6]
y = [8, 5, 6, 3, 5, 6]

result_zad_4 = bar_plot(x, y)

print(result_zad_4)


# Zadania 5
def heat_plot(matrix_n, matrix_m):
    matrix = np.random.random((matrix_n, matrix_m))

    plt.imshow(matrix, cmap='jet', interpolation='nearest')
    plt.colorbar()

    plt.show()


result_heat_plot = heat_plot(15, 15)

print(result_heat_plot)


# Zadania 6
def contour_plot(x, y):
    X, Y = np.meshgrid(x, y)

    Z = np.sqrt((X ** 2 + Y ** 2))
    CS = plt.contour(X, Y, Z)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.clabel(CS, inline=1, fontsize=10)

    plt.show()


x = np.arange(5, 15, 0.4)
y = np.arange(-2, 8, 0.3)
result_zad_6 = contour_plot(x, y)


# Zadania 7
def box_plot(n, m):
    matrix = np.random.randn(n, m)
    plt.boxplot(matrix)

    plt.xlabel("numer wketora")
    plt.ylabel("liczba probek")

    plt.show()


result_zad_7 = box_plot(9, 12)


# Zadania 8
def pie_plot(sizes, labels):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.show()


sizes = [45.7, 24.3, 9.5, 7.5, 3]
labels = ["Shareholder 1", "Shareholder 2", "Shareholder 3", "Shareholder 4", "Shareholder 5"]
result_zad_8 = pie_plot(sizes, labels)


# Zadania 9
def make_subplots(m1, m2):
    figure, (ax1, ax2) = plt.subplots(ncols=2)

    ax1.plot(m1)
    ax1.grid(True)

    ax2.plot(m2, marker="o")

    plt.show()


m1 = np.random.randn(13, 3)
m2 = np.random.randn(18, 4)
result_zad_9 = make_subplots(m1, m2)


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
