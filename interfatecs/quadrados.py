entrada = int(input())

def quadrado_perfeito(numero):
    impares = []
    qtd = 0
    result = 0
    for i in range(numero):
        if i % 2 != 0:
            impares.append(i)
    for impar in impares:
        if result != numero:
            result += impar
            qtd += 1
    return qtd

print(quadrado_perfeito(entrada))
        
    