import heapq

def a_estrella(grafo, inicio, fin, heuristica):
    abierta = []
    cerrada = set()
    heapq.heappush(abierta, (0 + heuristica(inicio), 0, inicio, []))

    while abierta:
        _, costo, actual, camino = heapq.heappop(abierta)
        if actual in cerrada:
            continue
        camino = camino + [actual]
        if actual == fin:
            return camino
        cerrada.add(actual)
        for vecino, peso in grafo.get(actual, []):
            heapq.heappush(abierta, (costo + peso + heuristica(vecino), costo + peso, vecino, camino))
    
    return None

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

def heuristica(nodo):
    distancias = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
    return distancias.get(nodo, 0)

camino = a_estrella(grafo, 'A', 'D', heuristica)
print(f"Camino más corto es: {camino}")