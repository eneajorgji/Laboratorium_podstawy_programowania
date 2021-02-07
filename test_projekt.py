import numpy as np
import math


def encrypt_matrix(password):
    len_password = len(password)
    n_matrix = math.ceil(pow(len_password, 0.5))

    # turn password into a list, by splitting each letter
    tokens = list(password)

    # add "X" to tokens until == 4 x4
    ##################################################################################
    # Not needed to use a loop, you know for sure how many missing characters you have
    # while len(tokens) < n_matrix ** 2:
    #     tokens.append("x")
    ##################################################################################
    tokens = tokens + ['x']*((n_matrix**2) - len(tokens))

    tokens_np_array = np.array(tokens)

    # create matrix n_matrix **2, write each character in matrix, starting from up row left, to right
    tokens_n_matrix = np.reshape(tokens_np_array, (n_matrix, n_matrix))
    print(tokens_n_matrix)
    # Output
    # [['v' 'e' 'r' 'y' 'l']
    #  ['o' 'n' 'g' 'p' 'a']
    #  ['s' 's' 'w' 'o' 'r']
    #  ['d' '2' '0' '2' '1']
    #  ['x' 'x' 'x' 'x' 'x']]

    # read matrix by columns starting up down
    read_matrix = tokens_n_matrix.copy(order="F")

    encrypted_matrix_password = ''  # use a string instead of a list
    # for char in np.nditer(read_matrix):
    #     print(char, end="")
    #     encrypted_matrix_password.append(char)

    # Based on what @hpaulj commented
    for col in range(0, read_matrix.shape[1]):
        for row in range(0, read_matrix.shape[0]):
            encrypted_matrix_password += read_matrix[row, col]
    # return encrypted_matrix_password
    print(encrypted_matrix_password)
    # output
    # vosdxens2xrgw0xypo2xlar1x


enc_mat = encrypt_matrix("verylongpassword2021")