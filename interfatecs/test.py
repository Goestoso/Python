def imprimir_numeros(n):
    if n > 0:
        imprimir_numeros(n - 1)  # Chamada recursiva para imprimir os números de 1 a n-1
        print(n)  # Imprime o número atual

imprimir_numeros(10)  # Chama a função para imprimir os números de 1 a 10
