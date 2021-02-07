import numpy as np
import math


def encrypt_matrix(password):
    len_password = len(password)
    n_matrix = math.ceil(pow(len_password, 0.5))

    # zmien password w list
    tokens = list(password)

    # dodaj "x", zeby macierz byla kwadratowa
    while len(tokens) < n_matrix ** 2:
        tokens.append("x")
    tokens_np_array = np.array(tokens)

    # stworz macierz n_matrix * n_marix, wpisuj kazda litere w macierz
    tokens_n_matrix = np.reshape(tokens_np_array, (n_matrix, n_matrix))
    print(tokens_n_matrix)

    # odczytaj zaszyfrowana macierz
    read_matrix = tokens_n_matrix.copy(order="F")

    encrypted_matrix_password = []
    for char in np.nditer(read_matrix):
        print(char, end="")
        encrypted_matrix_password.append(char)

    print(encrypted_matrix_password)


enc_mat = encrypt_matrix("bardzodlugiehaslo2021")
