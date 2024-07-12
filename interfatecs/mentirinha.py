def mentirinha(numero):
    index = 2
    lista_div = [1, numero]
    while index < numero:
        if numero % index == 0:
            lista_div.append(index)
        index += 1
    
    if len(lista_div) == 3: return "sim"
    return "nao"
    
entrada = int(input())
print(mentirinha(entrada))

