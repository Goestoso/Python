import heapq

def dijkstra(grafo, ponto_inicial):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[ponto_inicial] = 0
    fila = [(0, ponto_inicial)]
    
    while fila:
        distancia_atual, vertice_atual = heapq.heappop(fila)
        
        if distancia_atual > distancias[vertice_atual]:
            continue
        
        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso
            
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila, (distancia, vizinho))
    
    return distancias

grafo = {
    '1': {'2': 6, '4': 3, '5': 5},
    '2': {'2': 6, '3': 7, '4': 4, '8': 4},
    '3': {'2': 7, '8': 3, '9': 3, '10': 5},
    '4': {'1': 3, '2': 4, '5': 2, '8': 5},
    '5': {'1': 5, '4': 2, '6': 6, '8': 4},
    '6': {'5': 6, '7': 1, '8': 3, '10': 3},
    '7': {'6': 1, '10': 5},
    '8': {'2': 4, '3': 3, '4': 5, '5': 4, '6': 3, '10': 7},
    '9': {'3': 3, '10': 2},
    '10': {'3': 5, '6': 3, '7': 5, '8': 7, '9': 2}
}

ponto_inicial = '1'

distancias = dijkstra(grafo, ponto_inicial)

distancia_ate_g = distancias['10']
distancia_ate_h = distancias['9']

print(f'Distância de 1 até 10: {distancia_ate_g}')
print(f'Distância de 1 até 9: {distancia_ate_h}')
