class Data:

    def __init__(self, dia, mes, ano):

        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.data = f"{dia:02d}/{mes:02d}/{ano}" #adiciona um zero a esquerda de números < 10

    def imprime_data(self):
        print(self.data)