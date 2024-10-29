from random import randint, sample
from time import time

def gerar_grafo(n_vertices):
    vertices = [chr(65 + i) if i < 26 else chr(65 + (i // 26) - 1) + chr(65 + (i % 26)) for i in range(n_vertices)]
    grafo = {}

    for vertice in vertices:
        n_arestas = randint(5, min(20, n_vertices - 1))
        vizinhos = sample([v for v in vertices if v != vertice], n_arestas)
        grafo[vertice] = { vizinho: randint(3, 10) for vizinho in vizinhos }

    return grafo

def truncate_obj(obj):
    return str(obj)[:100]

def calcular_tempo(algoritimo, grafo, inicio):
    t_inicio = time()
    resultado = algoritimo(grafo, inicio)
    t_fim = time()
    return resultado, t_fim - t_inicio