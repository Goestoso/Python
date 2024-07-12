entradaBase = input()

entrada = ""
valido = True

for letra in entradaBase:
    if letra.isdigit(): entrada += letra
    if letra.isalpha():
        if letra.isupper(): entrada += letra
        else: 
            valido = False    
            print("Placa inválida")

def isPlacaAntiga(placa):
    placa = str(placa)
    if(placa[0] == 'A' or placa[0] == 'P'):
        if(placa[1:len(placa)].isdigit()):
            tamanho = len(placa[1:len(placa)])
            if(tamanho >= 1 and tamanho <= 5):
                return True
    return False        
                

def valida_placa(entrada):
    entrada = str(entrada)
    if len(entrada) > 7: 
        return "Placa invalida"
    if entrada.isdigit(): 
        return "Placa numerica"
    if isPlacaAntiga(entrada):
        return "Placa muito antiga"
    if (entrada[0:2].isalpha() and entrada[3:len(entrada)].isdigit()) and len(entrada) == 7:
        return "Placa AAA-9999"
    if (entrada[0:1].isalpha() and entrada[2:len(entrada)].isdigit()) and len(entrada) == 6:
        return "Placa AA-9999"
    if len(entrada) == 7 and (entrada[0:2].isalpha() and entrada[3].isdigit() and entrada[4].isalpha() and entrada[5:len(entrada)].isdigit()):
        return "Placa Mercosul"
    return "Placa invalida"

if valido:
    print(valida_placa(entrada))
