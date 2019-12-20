import numpy as np

def vander_matrix(ip_vector, n, increasing = True):
    if  not increasing:
        op_matrix = np.array([x ** i for x in ip_vector for i in range(n)]).reshape(ip_vector.size, n)
    else:
        return 1

    return op_matrix


input  =np.array([1,2,3])
col = 3
op_mat = vander_matrix(input,col,False)
print('input matrix :\n',input)
print('\n\nVandermonde output matrix :\n',op_mat)
