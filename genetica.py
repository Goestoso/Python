tamanho_palindromo = int(input())
entrada = input()
anterior = 0
proximo = tamanho_palindromo
lista_sub = []
qtd = 0

while proximo <= len(entrada):
    lista_sub.append(entrada[anterior:proximo])
    anterior += 1
    proximo += 1
    
lista_reversa = list(map(lambda sub:sub[::-1], lista_sub))
tem_palindromo = False
for sub_str in lista_sub:
    for sub_reversa in lista_reversa:
        if sub_reversa == sub_str: tem_palindromo = True
        
if tem_palindromo: print("S")
else: print("N")