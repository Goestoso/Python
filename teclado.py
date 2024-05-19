n = int(input())
index = 0
palavras = []
dois = ('A', 'B', 'C')
tres = ('D', 'E', 'F')
quatro = ('G', 'H', 'I')
cinco = ('J', 'K', 'L')
seis = ('M','N','O')
sete = ('P', 'Q', 'R', 'S')
oito = ('T', 'U', 'V')
nove = ('W', 'X', 'Y', 'Z')
while index < n:
    temp = input()
    palavras.append(temp)
    index +=1

for palavra in palavras:
    numeros = ""
    for letra in palavra:
        if letra in dois:
            numeros += '2'
        if letra in tres:
            numeros +='3'
        if letra in quatro:
            numeros += '4'
        if letra in cinco:
            numeros += '5'
        if letra in seis:
            numeros += '6'
        if letra in sete:
            numeros += '7'
        if letra in oito:
            numeros += '8'
        if letra in nove:
            numeros += '9'
    print(numeros)
    

    
