#Criando a primeira classe (POO)

class Conta:
    
    #pass #(passa bloco de código)

    def __init__(self, numero, titular, saldo, limite): #Pode-se já declarar valores aos parâmetros (limite = 1000.0)
        
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): #método privado
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar 

    def saca(self, valor):
        if self.__pode_sacar(valor) :
            self.__saldo -= valor
        else :
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.__deposita(valor)

    @property
    def saldo(self): #getter
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular.title()
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite): #setter
        self.__limite = limite

    @staticmethod #métodos estáticos ou de classe
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
    
    