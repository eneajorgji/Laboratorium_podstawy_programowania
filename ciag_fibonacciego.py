def ciag_fibonacciego(n):
    ciag_fibonacci = [0, 1]
    n_razy = n - 2
    count = 0

    while count < n_razy:
        ciag_fibonacci.append(ciag_fibonacci[-2] + ciag_fibonacci[-1])
        count = count + 1

    print(f"Wartosc ciagu Fibonacciego dla zadanego rozmiaru n {n_razy + 2}:", ciag_fibonacci)


ciag_fibo = ciag_fibonacciego(19)