from tkinter import Tk, Label, Button, Toplevel, Canvas, messagebox
from tkinter.font import Font
import random, time
#variaveis globais
bullet_point = '\u2022'
intro: Tk = Tk()
emojis:list = ['📱', '💻', '🖨️', '⌨️', '🖱️', '🎧']
tentativas: int = 0
first_btn: Button = Button()
second_btn: Button = Button()
coordenadas: dict = {'x': list(), 'y': list()}
indices: list = list()
acertos: int = 0
def embaralhar_emojis():
    global emojis
    list1 = list(random.sample(emojis, len(emojis)))
    list2 = list(random.sample(emojis, len(emojis)))
    emojis = list1 + list2
    random.shuffle(emojis)
def play():
    #criar janela de introdução ao jogo
    embaralhar_emojis()
    intro.iconbitmap('memory.ico')
    intro.title("Memory Game")
    largura_janela = 340
    altura_janela = 160
    largura_tela = intro.winfo_screenwidth()
    altura_tela = intro.winfo_screenheight()
    posicaoX = (largura_tela - largura_janela) // 2
    posicaoY = (altura_tela - largura_janela) // 2
    intro.wm_minsize(largura_janela, altura_janela)
    intro.wm_maxsize(largura_janela, altura_janela)
    intro.geometry(f"{largura_janela}x{altura_janela}+{posicaoX}+{posicaoY}")
    label = Label(intro, text="Informações gerais:", anchor="center", font=Font(family="Arial", size=12, weight="bold"))
    label.grid(row=0, columnspan=1, sticky='ew', pady=2, padx=0)
    label = Label(intro, text=f"{bullet_point} Aperte jogar para iniciar o game;"
                                f"\n{bullet_point} Aperte sair para fechar o game;"
                                f"\n{bullet_point} Aparecerá uma janela com as posições dos objetos; "
                                f"\n{bullet_point} Relacione as posições com os objetos iguais;"
                                f"\n{bullet_point} Tenha um bom jogo!",
                     justify="left", font=Font(family="Arial", size=10, weight="normal"))
    label.grid(row=1, column=0, padx=0, pady=2)
    botao = Button(intro, text="sair", command=encerrar, font=Font(family="Arial", size=10, weight="bold"))
    botao.grid(row=2, column=0, sticky='e', pady=5)
    botao = Button(intro, text="jogar", command=iniciar, font=Font(family="Arial", size=10, weight="bold"))
    botao.grid(row=2, column=0, sticky='w', padx=15, pady=5)
    intro.mainloop()
def iniciar():
    game = Toplevel()
    game.protocol("WM_DELETE_WINDOW", lambda: voltar(game))
    intro.withdraw()
    game.iconbitmap('memory.ico')
    game.title("Memory Game")
    largura_janela = 320
    altura_janela = 170
    largura_tela = game.winfo_screenwidth()
    altura_tela = game.winfo_screenheight()
    posicaoX = (largura_tela - largura_janela) // 2
    posicaoY = (altura_tela - largura_janela) // 2
    game.wm_minsize(largura_janela, altura_janela)
    game.wm_maxsize(largura_janela, altura_janela)
    game.geometry(f"{largura_janela}x{altura_janela}+{posicaoX}+{posicaoY}")
    label = Label(game, text="Observe as posições abaixo:", anchor="center", font=Font(family="Arial", size=12, weight="bold"))
    label.grid(row=0, columnspan=1, sticky='ew', pady=2, padx=0)
    linha = Canvas(game, width=320, height=170)
    linha.grid()
    index = 1
    for i in range(20,160,40):
        linha.create_line(0,i,320,i)
        for j in range(80, 321, 80):
            linha.create_line(j, 20, j, 200)
            centro_x = j - 40
            centro_y = i + 20
            linha.create_text(centro_x, centro_y, text=f"{index}", font="Arial")
            index += 1
    game.update()
    game.after(5000, lambda: atualizar_janela(game))

def atualizar_janela(game):
    for widget in game.winfo_children():
        widget.destroy()
    label = Label(game, text="Tente lembrar onde estão as figuras:", anchor="center",
                  font=Font(family="Arial", size=10, weight="bold"))
    label.grid(row=0, columnspan=1, sticky='ew', pady=4, padx=0)
    linha = Canvas(game, width=320, height=170)
    linha.grid()
    index = 0
    for i in range(20, 160, 40):
        linha.create_line(0, i, 320, i)
        for j in range(80, 321, 80):
            linha.create_line(j, 20, j, 200)
            centro_x = j - 40
            centro_y = i + 20
            linha.create_text(centro_x, centro_y, text=f"{emojis[index]}", font="Arial")
            index += 1 if index < 11 else 0
    game.update()
    game.after(2000, lambda: buscar_iguais(game))
def buscar_iguais(game):
    index = 0
    for i in range(50, 160, 40):
        for j in range(80, 321, 80):
            canto_x = j - 80
            canto_y = i
            botao = Button(game, text="?")
            botao['command'] = lambda b=botao, i=index, g=game: clicar_botao(b,i,g)
            botao.place(x=canto_x, y=canto_y, width=80, height=40)
            coordenadas['x'].append(canto_x)
            coordenadas['y'].append(canto_y)
            index += 1 if index < 11 else 0
    game.update()

def clicar_botao(botao:Button, index:int, game:Tk):
    global tentativas
    global acertos
    tentativas += 1
    global indices
    indices.append(index)
    global first_btn
    global second_btn
    if tentativas == 1:
        first_btn = botao
        first_btn.place_forget()
    if tentativas == 2:
        tentativas = 0
        second_btn = botao
        second_btn.place_forget()
        game.update()
        corresp = verifica_corresp()
        if corresp: acertos += 1
        else:
            time.sleep(1)
            first_btn.place(x=coordenadas['x'][indices[0]], y=coordenadas['y'][indices[0]], width=80, height=40)
            second_btn.place(x=coordenadas['x'][indices[1]], y=coordenadas['y'][indices[1]], width=80, height=40)
        indices = list()
    if acertos == 6:
        game.destroy()
        acertos = 0
        messagebox.showinfo(title="🏆", message="Parabéns, você achou todas as figuras e as suas correspondências!")
        intro.deiconify()
def verifica_corresp():
    return emojis[indices[0]] == emojis[indices[1]]

def voltar(game):
    game.destroy()
    intro.deiconify()
def encerrar():
    intro.quit()

if (__name__ == "__main__"):
    play()