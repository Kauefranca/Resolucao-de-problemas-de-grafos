# Imports para gerar grafos aleatórios
import random
import time

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.arestas = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, u, v):
        if v not in self.arestas[u]:
            self.arestas[u].append(v)
            self.arestas[v].append(u)

def gerar_grafo_aleatorio(num_vertices, probabilidade_aresta):
    grafo = Grafo(num_vertices)
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if random.random() < probabilidade_aresta:
                grafo.adicionar_aresta(i, j)
    return grafo

def verificar_planitude(grafo):
    def encontrar_k5(grafo):
        for v in range(grafo.num_vertices):
            if len(grafo.arestas[v]) >= 4:
                vizinhos = set(grafo.arestas[v])
                for u in vizinhos:
                    if len(set(grafo.arestas[u]) & vizinhos) >= 3:
                        return True
        return False

    def encontrar_k33(grafo):
        for v in range(grafo.num_vertices):
            if len(grafo.arestas[v]) >= 3:
                vizinhos = set(grafo.arestas[v])
                for u in vizinhos:
                    comuns = set(grafo.arestas[u]) & vizinhos
                    if len(comuns) >= 2:
                        for w in comuns:
                            if len(set(grafo.arestas[w]) & comuns) >= 1:
                                return True
        return False

    return not (encontrar_k5(grafo) or encontrar_k33(grafo))

def caixeiro_viajante_aproximado(grafo):
    visitados = set()
    caminho = []
    vertice_atual = 0
    
    while len(visitados) < grafo.num_vertices:
        visitados.add(vertice_atual)
        caminho.append(vertice_atual)
        
        proximo_vertice = None
        menor_distancia = float('inf')
        
        for vizinho in grafo.arestas[vertice_atual]:
            if vizinho not in visitados and vizinho < menor_distancia:
                proximo_vertice = vizinho
                menor_distancia = vizinho
        
        if proximo_vertice is None:
            break
        
        vertice_atual = proximo_vertice
    
    caminho.append(caminho[0])
    return caminho

def medir_tempo_execucao(grafo, funcao, nome_funcao):
    inicio = time.time()
    resultado = funcao(grafo)
    fim = time.time()
    tempo_execucao = fim - inicio
    print(f"Tempo de execução de {nome_funcao}: {tempo_execucao:.6f} segundos")
    return resultado


grafo1 = gerar_grafo_aleatorio(100, 0.1)
grafo2 = gerar_grafo_aleatorio(500, 0.05)

print("Grafo 1:")
planar = medir_tempo_execucao(grafo1, verificar_planitude, "verificar_planitude")
print("O grafo é planar." if planar else "O grafo não é planar.")
caminho = medir_tempo_execucao(grafo1, caixeiro_viajante_aproximado, "caixeiro_viajante_aproximado")
print("Comprimento do caminho:", len(caminho))

print("\nGrafo 2:")
planar = medir_tempo_execucao(grafo2, verificar_planitude, "verificar_planitude")
print("O grafo é planar." if planar else "O grafo não é planar.")
caminho = medir_tempo_execucao(grafo2, caixeiro_viajante_aproximado, "caixeiro_viajante_aproximado")
print("Comprimento do caminho:", len(caminho))