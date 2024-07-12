import guessing
import hangman
import memory

def choose_game():

    print("*********************************")
    print("*******Escolha o seu game!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação (3) Memória")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando forca")
        hangman.play()
        print("Jogo da forca foi encerrado.")
    elif (jogo == 2):
        print("Jogando adivinhação")
        guessing.play()
        print("Jogo da advinhação foi encerrado.")
    elif (jogo == 3):
        print("Jogando memória")
        memory.play()
        print("Jogo da memória foi encerrado.")

if (__name__ == "__main__"): #seta a variável de execução __name__ para verificar se o arquivo é executado diretamente
    choose_game()