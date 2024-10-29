from utils import gerar_grafo, truncate_obj, calcular_tempo

def alg_dijkstra(grafo, inicio):
    distancias = { no: float("Inf") for no in grafo }
    distancias[inicio] = 0
    nao_visitado = list(grafo.keys())
    
    while nao_visitado:
        atual = min(nao_visitado, key=lambda no: distancias[no])
        nao_visitado.remove(atual)
        
        for vizinho, peso in grafo[atual].items():
            distancia = distancias[atual] + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
    
    return distancias

def alg_bellman_ford(grafo, inicio):
    distancias = { no: float("Inf") for no in grafo }
    distancias[inicio] = 0
    
    for _ in range(len(grafo) - 1):
        for no in grafo:
            for vizinho, peso in grafo[no].items():
                if distancias[no] + peso < distancias[vizinho]:
                    distancias[vizinho] = distancias[no] + peso

    for no in grafo:
        for vizinho, peso in grafo[no].items():
            if distancias[no] + peso < distancias[vizinho]:
                print("O grafo contém um ciclo com pesos negativos")
                return
    
    return distancias

print("Grafo pequeno (10 vértices):")
grafo_P = gerar_grafo(10)

dijkstra, tempo_dijkstra = calcular_tempo(alg_dijkstra, grafo_P, 'A')
print(f"Dijkstra: {truncate_obj(dijkstra)}\nTempo: {tempo_dijkstra:.6f} segundos")

bellman_ford, tempo_bellman_ford = calcular_tempo(alg_bellman_ford, grafo_P, 'A')
print(f"Bellman-Ford: {truncate_obj(bellman_ford)}\nTempo: {tempo_bellman_ford:.6f} segundos")

print("\nGrafo grande (1000 vértices):")
grafo_G = gerar_grafo(1000)

dijkstra_result, dijkstra_time = calcular_tempo(alg_dijkstra, grafo_G, 'A')
print(f"Dijkstra: {truncate_obj(dijkstra_result)}...\nTempo: {dijkstra_time:.6f} segundos")

bellman_ford_result, bellman_ford_time = calcular_tempo(alg_bellman_ford, grafo_G, 'A')
print(f"Bellman-Ford: {truncate_obj(bellman_ford_result)}...\nTempo: {bellman_ford_time:.6f} segundos")