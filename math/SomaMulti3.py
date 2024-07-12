from itertools import combinations

U = set(range(1, 38))
Z3 = set(range(3))

count = 0

# Encontrar todas as combinações de três números do conjunto U
combinations_3 = list(combinations(U, 3))

# Verificar se a soma de cada combinação é um múltiplo de três
for comb in combinations_3:
    if sum(comb) % 3 == 0:
        count += 1

print("Número de maneiras de escolher três números cuja soma é múltiplo de três:", count)
