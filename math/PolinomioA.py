import numpy as np

# Definir a matriz A
A = np.array([[4, 5], [5, 7]])

# Calcular o quadrado de A
A_squared = np.matmul(A, A)

# Calcular o polinômio em A
polynomial = A_squared - 11 * A + 3 * np.eye(2)

# Imprimir o resultado
print(polynomial)
