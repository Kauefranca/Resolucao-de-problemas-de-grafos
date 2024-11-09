# Imports para gerar grafos aleatórios
from time import time
from random import random
from string import ascii_uppercase

def edmonds_karp(grafo, fonte, sumidouro):
    def busca_em_largura(pai):
        visitados = [False] * len(grafo)
        fila = [fonte]
        visitados[fonte] = True
        
        while fila:
            u = fila.pop(0)
            for v, capacidade in enumerate(grafo[u]):
                if not visitados[v] and capacidade > 0:
                    visitados[v] = True
                    pai[v] = u
                    if v == sumidouro:
                        return True
                    fila.append(v)
        return False

    fluxo_maximo = 0
    pai = [-1] * len(grafo)
    while busca_em_largura(pai):
        fluxo_caminho = float('inf')
        s = sumidouro
        while s != fonte:
            fluxo_caminho = min(fluxo_caminho, grafo[pai[s]][s])
            s = pai[s]
        fluxo_maximo += fluxo_caminho
        v = sumidouro
        while v != fonte:
            u = pai[v]
            grafo[u][v] -= fluxo_caminho
            grafo[v][u] += fluxo_caminho
            v = pai[v]
    return fluxo_maximo

def criar_grafo_bipartido(esquerda, direita, arestas):
    n = len(esquerda) + len(direita) + 2
    grafo = [[0] * n for _ in range(n)]
    fonte, sumidouro = 0, n - 1
    
    for i, u in enumerate(esquerda, 1):
        grafo[fonte][i] = 1
    
    for i, v in enumerate(direita, len(esquerda) + 1):
        grafo[i][sumidouro] = 1
    
    for u, v in arestas:
        i, j = esquerda.index(u) + 1, direita.index(v) + len(esquerda) + 1
        grafo[i][j] = 1
    
    return grafo, fonte, sumidouro

def verificar_emparelhamento(esquerda, direita, arestas, emparelhamento):
    usados_esquerda = set()
    usados_direita = set()
    for u, v in emparelhamento:
        if u in usados_esquerda or v in usados_direita:
            return False
        if (u, v) not in arestas:
            return False
        usados_esquerda.add(u)
        usados_direita.add(v)
    return len(emparelhamento) == min(len(esquerda), len(direita)) or all(u in usados_esquerda for u in esquerda) or all(v in usados_direita for v in direita)


def gerar_grafo_bipartido(tamanho_esquerda, tamanho_direita, probabilidade_aresta=0.5):
    esquerda = [f'Y{i+1}' for i in range(tamanho_direita)]
    direita = [f'X{i+1}' for i in range(tamanho_direita)]
    arestas = []

    for no_esquerda in esquerda:
        for no_direita in direita:
            if random() < probabilidade_aresta:
                arestas.append((no_esquerda, no_direita))
    
    return esquerda, direita, arestas


tamanho_esquerda = 100
tamanho_direita = 100
probabilidade_aresta = 0.5

esquerda, direita, arestas = gerar_grafo_bipartido(tamanho_esquerda, tamanho_direita, probabilidade_aresta)

print(f"Vértices esquerda: {tamanho_esquerda}")
print(f"Vértices direita: {tamanho_direita}")
print(f"Total Arestas: {len(arestas)}")

grafo, fonte, sumidouro = criar_grafo_bipartido(esquerda, direita, arestas)

i = time()
emparelhamento_maximo = edmonds_karp(grafo, fonte, sumidouro)
print(f"Tempo de execução: {time() - i:.2f}s")

print(f"\nTamanho do emparelhamento máximo: {emparelhamento_maximo}")

emparelhamento = []
for i, u in enumerate(esquerda, 1):
    for j, v in enumerate(direita, len(esquerda) + 1):
        if grafo[j][i] == 1:  # Fluxo reverso indica uma aresta no emparelhamento
            emparelhamento.append((u, v))

print("Emparelhamento máximo (primeiros 20 pares):")
for aresta in emparelhamento[:20]:
    print(f"{aresta[0]} - {aresta[1]}")

eh_valido = verificar_emparelhamento(esquerda, direita, arestas, emparelhamento)
print(f"O emparelhamento é válido e máximo? {'Sim!' if eh_valido else 'Não!'}")