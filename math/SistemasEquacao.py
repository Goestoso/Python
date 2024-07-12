import numpy as np

# Definindo a matriz de coeficientes
A = np.array([[2, -3, -7], [3, -4, -3], [4, -5, -3]])

# Definindo o vetor de termos independentes
b = np.array([14, -5, -8])

# Resolvendo o sistema de equações
x = np.linalg.solve(A, b)

print("A solução do sistema é:")
print("x =", x[0])
print("y =", x[1])
print("z =", x[2])
