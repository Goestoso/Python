entrada = input()
lista_int = entrada.split(' ')
lista_int = list(map(lambda x: int(x), lista_int))
list_int = lista_int.sort()
print(lista_int[1])