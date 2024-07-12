import numpy as np

# Matriz de exemplo
matrix = np.array([
    [5, -1, -1, 6],
    [4, -3, 0, 0],
    [-2, 4, -1, -3],
    [3, 1, -2, 2]
])

determinant = np.linalg.det(matrix)
print("Determinante:", determinant)

