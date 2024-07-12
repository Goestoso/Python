import heapq

def prim(graph):
    start_vertex = '1'
    visited = set([start_vertex])
    minimum_spanning_tree = []
    edges = [
        (weight, start_vertex, next_vertex)
        for next_vertex, weight in graph[start_vertex]
    ]
    heapq.heapify(edges)
    total_weight = 0

    while edges:
        weight, current_vertex, next_vertex = heapq.heappop(edges)
        if next_vertex not in visited:
            visited.add(next_vertex)
            minimum_spanning_tree.append((current_vertex, next_vertex, weight))
            total_weight += weight

            for neighbor, neighbor_weight in graph[next_vertex]:
                if neighbor not in visited:
                    heapq.heappush(edges, (neighbor_weight, next_vertex, neighbor))

    return minimum_spanning_tree, total_weight

# Grafo representado como um dicionário de adjacências com os pesos das arestas
graph = {
    '1': [('2', 5), ('3', 1), ('4', 2)],
    '2': [('1', 5), ('3', 3), ('6', 3)],
    '3': [('1', 1), ('2', 3), ('4', 5), ('5', 5), ('6', 5), ('7', 5)],
    '4': [('1', 2), ('3', 5), ('5', 6)],
    '5': [('3', 5), ('4', 6), ('6', 4), ('7', 3)],
    '6': [('2', 3), ('3', 5), ('5', 4), ('7', 2), ('8', 2)],
    '7': [('3', 5), ('5', 3), ('6', 2), ('8', 3)],
    '8': [('6', 2), ('7', 3)],
}

minimum_spanning_tree, total_weight = prim(graph)

# Imprime as arestas da árvore geradora mínima
for edge in minimum_spanning_tree:
    print(f'{edge[0]} --- {edge[2]} : {edge[1]}')

print("Peso total da árvore geradora mínima:", total_weight)
