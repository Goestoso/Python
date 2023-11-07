import networkx as nx

# Construção do grafo
grafo = nx.DiGraph()

grafo.add_edge('A', 'B', capacity=7)
grafo.add_edge('A', 'C', capacity=6)
grafo.add_edge('A', 'D', capacity=5)
grafo.add_edge('B', 'E', capacity=5)
grafo.add_edge('C', 'E', capacity=3)
grafo.add_edge('C', 'F', capacity=5)
grafo.add_edge('D', 'F', capacity=6)
grafo.add_edge('D', 'G', capacity=3)
grafo.add_edge('E', 'G', capacity=7)
grafo.add_edge('F', 'G', capacity=5)

# Definição da fonte e sumidouro
fonte = 'A'
sumidouro = 'G'

# Cálculo do fluxo máximo
fluxo = nx.maximum_flow(grafo, fonte, sumidouro)
fluxo_maximo = fluxo[0]
fluxos_arestas = fluxo[1]

# Impressão do caminho percorrido
caminho_percurso = nx.shortest_path(grafo, fonte, sumidouro)
print("Caminho percorrido:", caminho_percurso)

# Impressão do resultado
print("Fluxo máximo da rede:", fluxo_maximo)

# Impressão dos fluxos nas arestas
for aresta, fluxo_aresta in fluxos_arestas.items():
    print(f"Fluxo na aresta {aresta}: {fluxo_aresta}")

