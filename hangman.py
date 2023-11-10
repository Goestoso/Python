import random

def play():
    
    start_game()
    
    numero = random.randrange(0, len(read_file_words())) #range de 0 e a quantidade de palavras lidas no arquivo words.txt
    
    palavra_secreta = read_file_words()[numero].upper() #palavra secreta recebe uma palavra do arquivo lido
    
    acertou = False
    enforcou = False
    letras_acertadas = ["_" for letra in palavra_secreta]
    erros = 0
    
    print(letras_acertadas)
    
    while(not acertou and not enforcou):
        
        chute = input("Qual letra?\n")
        chute = chute.strip().upper() #chute remove vazios e fica em caixa alta
        
        if (chute in palavra_secreta):
            
            mark_correct_guess(chute, palavra_secreta, letras_acertadas)
        
        else:
            erros += 1
            draw_hangman(erros)
                 
        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print((letras_acertadas))
        
    if(acertou):
        
        win()
        
    else:
        
        lose(palavra_secreta)
        

def start_game():
    
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
def read_file_words():
    
    arquivo = open("words.txt", "r")
    palavras = []
    
    for linha in arquivo:
        palavras.append(linha.strip())
        
    arquivo.close()
    return palavras

def mark_correct_guess(chute, palavra_secreta, letras_acertadas):
    
    index = 0
    for letra in palavra_secreta:
                
        if(chute.upper() == letra.upper()):
                    
            letras_acertadas[index] = letra
                    
        index += 1 #aumenta a iteração a cada verificação
        
def draw_hangman(erros):
    
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    
def win():
    
    print("Parabéns, você ganhou!\n")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def lose(palavra_secreta):
    
    print("\nPuxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    
if(__name__ == "__main__"):
    play()

