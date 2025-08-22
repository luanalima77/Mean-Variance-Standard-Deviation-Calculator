import numpy as np

def calculate(list):
    #Verificando se a lista fornecida possui quantidade de valores diferente de 9 e retornando um ValueError.
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    #Convertendo a lista em matriz 3x3 e também transformando-a em unidimensional (flatten).
    matrix_3_x_3 = np.reshape(list, (3,3))
    flatten_matrix = matrix_3_x_3.flatten()

    #OPERAÇÕES SOLICITADAS.
    #Calculando as médias.
    mean_axis_1 = np.mean(matrix_3_x_3, axis = 0).tolist() 
    mean_axis_2 = np.mean(matrix_3_x_3, axis = 1).tolist() 
    mean_flatten_matrix = np.mean(flatten_matrix).tolist()

    #Calculando as variâncias.
    var_axis_1 = np.var(matrix_3_x_3, axis = 0).tolist()
    var_axis_2 = np.var(matrix_3_x_3, axis = 1).tolist()
    var_flatten_matrix = np.var(flatten_matrix).tolist()
    
    return calculations
