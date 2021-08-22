import numpy as np
import math

coefficients = []
seq = [1, 25, 101, 261, 537]
save = [seq[0]]

def matrix_generator(dim):
    empty_matrix = np.zeros((dim, dim))
    for z in range(0, dim):
        empty_matrix[0, z] = seq[z]
    for x in range(1, dim - 1):
        for y in range(0, dim - x):
            if int(empty_matrix[x - 1, y + 1]) - int(empty_matrix[x - 1, y]) == 0:
                return empty_matrix
            else:
                empty_matrix[x, y] = empty_matrix[x - 1, y + 1] - empty_matrix[x - 1, y]
    coefficients.append(str((empty_matrix[dim-2, 0])/math.factorial(dim-2))+"_"+str(dim-2))
    return empty_matrix

matrix = matrix_generator(len(seq))

a = seq[0]

for x in range(0, len(seq)):
    seq[x] = seq[x] - a

def degree_checker(matrix):
    for x in range(1, len(seq)):
        if matrix[x, 0] == 0:
            return (x - 1)
    print("not enough info or not a polynomial")
    quit()

degree = degree_checker(matrix)

for z in range(degree, 0, -1):
    for x in range(1, len(seq)):
        seq[x] = seq[x] - (matrix[z, 0] / math.factorial(z)) * (x ** z)
    matrix = matrix_generator(z + 1)

coefficients.reverse()
del coefficients[0]
coefficients.insert(0, save[0])
print(coefficients)
