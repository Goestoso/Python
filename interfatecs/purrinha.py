def main():
    qtd_jogadores = int(input())
    jogadores = {}
    for _ in range(qtd_jogadores):
        key = input()
        jogadores[key] = 0
    qtd_rodadas = int(input())
    for _ in range(qtd_rodadas):
        guardados = input()
        guardados = [int(guardado) for guardado in guardados.split()]
        chutes = input()
        chutes = [int(chute) for chute in chutes.split()]
        total_guardados = 0
        for guardado in guardados:
            total_guardados += guardado
        if validaChutes(chutes):
            for index, jogador in enumerate(jogadores.keys()):
                if (chutes[index] == total_guardados):
                    jogadores[jogador] += 1
    
    print(vencedor(jogadores))
        
def vencedor(jogadores):
    jogadores = dict(jogadores)
    maximo = max(jogadores.values())
    empate = 0
    ganhador = ""
    for jogador, pontos in jogadores.items():
        if maximo == pontos: 
            ganhador = jogador
            empate += 1
        
    if empate > 1: return "EMPATE"
    
    return f"{ganhador} GANHOU"
            
def validaChutes(chutes):
    for i in range(len(chutes)-1):
        j = i + 1
        while j < len(chutes):
            if chutes[i] == chutes[j]:
                return False
            j += 1
    return True         
    
if __name__ == "__main__": 
    main()

    
        
            

       