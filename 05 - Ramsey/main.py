# Imports para gerar grafos aleatórios
import time
import random

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.arestas = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, v1, v2):
        if v2 not in self.arestas[v1]:
            self.arestas[v1].append(v2)
            self.arestas[v2].append(v1)

def coloracao_gulosa(grafo):
    cores = [-1] * grafo.num_vertices
    cores_disponiveis = [False] * grafo.num_vertices

    cores[0] = 0

    for v in range(1, grafo.num_vertices):
        for i in grafo.arestas[v]:
            if cores[i] != -1:
                cores_disponiveis[cores[i]] = True

        cor = 0
        while cor < grafo.num_vertices:
            if not cores_disponiveis[cor]:
                break
            cor += 1

        cores[v] = cor

        for i in grafo.arestas[v]:
            if cores[i] != -1:
                cores_disponiveis[cores[i]] = False

    return cores

def verificar_coloracao(grafo, cores):
    for v in range(grafo.num_vertices):
        for adjacente in grafo.arestas[v]:
            if cores[v] == cores[adjacente]:
                return False
    return True

def gerar_grafo_aleatorio(num_vertices, probabilidade_aresta):
    grafo = Grafo(num_vertices)
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if random.random() < probabilidade_aresta:
                grafo.adicionar_aresta(i, j)
    return grafo

def executar_e_medir(grafo, nome):
    inicio = time.time()
    cores = coloracao_gulosa(grafo)
    fim = time.time()
    tempo_execucao = fim - inicio

    print(f"\nResultados para {nome}:")
    print(f"Número de vértices: {grafo.num_vertices}")
    print(f"Número de arestas: {sum(len(adj) for adj in grafo.arestas) // 2}")
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")

    if verificar_coloracao(grafo, cores):
        print("Coloração válida encontrada!")
    else:
        print("A coloração não é válida.")

    num_cores = len(set(cores))
    print(f"Número total de cores usadas: {num_cores}")

grafo1 = gerar_grafo_aleatorio(100, 0.1)
executar_e_medir(grafo1, "Grafo 1")

grafo2 = gerar_grafo_aleatorio(500, 0.05)
executar_e_medir(grafo2, "Grafo 2")