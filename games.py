import guessing
import hangman  

def choose_game():

    print("*********************************")
    print("*******Escolha o seu game!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando forca")
        hangman.play()
    elif (jogo == 2):
        print("Jogando adivinhação")
        guessing.play()
        
if (__name__ == "__main__"): #seta a variável de execução __name__ para verificar se o arquivo é executado diretamente
    choose_game()