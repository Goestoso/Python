class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self): #método genérico
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa): #Herança
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano) #criando objeto genérico com nome e ano
        self.duracao = duracao

    def __str__(self): #sobrescrevendo o método da super classe usando um dunder method
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def imprime(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} min - {self._likes} Likes'

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    
    print(programa) #imprime o conteúdo textual da classe usando o dunder method __str__ delas
    #programa.imprime() #polimorfismo para uniformizar os objetos de subclasses diferentes mas que herdam da mesma super classe