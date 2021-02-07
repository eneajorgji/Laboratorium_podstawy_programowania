import numpy as np
import math


def encrypt_matrix(password):
    len_password = len(password)
    n_matrix = math.ceil(pow(len_password, 0.5))

    # turn password into a list, by splitting each letter
    tokens = list(password)

    # add "X" to tokens until == 4 x4
    while len(tokens) < n_matrix ** 2:
        tokens.append("x")
    tokens_np_array = np.array(tokens)

    # create matrix n_matrix * n_marix, write each character in matrix, starting from up row left, to right
    tokens_n_matrix = np.reshape(tokens_np_array, (n_matrix, n_matrix))
    print(tokens_n_matrix)

    # read matrix by columns starting up down
    read_matrix = tokens_n_matrix.copy(order="F")

    encrypted_matrix_password = []
    for char in np.nditer(read_matrix):
        print(char, end="")
        encrypted_matrix_password.append(char)

    # return encrypted_matrix_password
    print(encrypted_matrix_password)

enc_mat = encrypt_matrix("verylongpassword2021")
