def integral(func, a, b, N):
    # func - funkcja, a - poczatek przedział, b - koniec przedzial, i - liczba podprzedzialow
    dx = (b - a) / N
    integr = 0
    # for x in range(i):
    #     x = x * dx + a
    #     fx1 = eval(func)
    #     x += dx
    #     fx2 = eval(func)
    #     integr += 0.5 * dx * (fx1 + fx2)
    # return integr

    for i in N:
        while i < N:
            integr = integr + .5 * dx * (func(0 + i * dx) + func(dx + i * dx))
    return integr


func = (x ** 2)
a = 0
b = 2
i = 5
calkowanie = integral(func, a, b, i)

print(calkowanie)
