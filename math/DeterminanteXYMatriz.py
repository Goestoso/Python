import numpy as np

# Definir a matriz A
A = np.array([[4, 5], [5, 7]])

# Definir a matriz identidade I
I = np.eye(2)

# Definir o símbolo 'x'
x = 2

# Calcular a matriz A - xI
A_minus_xI = A - x * I

# Calcular o determinante da matriz A - xI
det = np.linalg.det(A_minus_xI)

# Imprimir o resultado
print(det)
