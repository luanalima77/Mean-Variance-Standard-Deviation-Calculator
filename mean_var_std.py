import numpy as np

def calculate(list):
    #Verificando se a lista fornecida possui quantidade de valores diferente de 9 e retornando um ValueError.
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    #Convertendo a lista em matriz 3x3 e também transformando-a em unidimensional (flatten).
    matrix_3_x_3 = np.reshape(list, (3,3))
    flatten_matrix = matrix_3_x_3.flatten()


    return calculations
