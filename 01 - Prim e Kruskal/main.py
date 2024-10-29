from random import random, randint, choice
import heapq
from time import time

class Grafo:
    def __init__(self, V):
        self.V = V
        self.arestas = [] 
        self.adj = [[] for _ in range(V)]  
    
    # Prim
    def add_aresta(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
        self.arestas.append((u, v, w))
    
    def agm_prim(self):
        fp = [] # Fila de prioridade
        src = 0

        key = [float('inf')] * self.V
        parent = [-1] * self.V
        visitado = [False] * self.V

        heapq.heappush(fp, (0, src))
        key[src] = 0

        while fp:
            u = heapq.heappop(fp)[1]

            if visitado[u]:
                continue

            visitado[u] = True

            for v, peso in self.adj[u]:
                if not visitado[v] and key[v] > peso:
                    key[v] = peso
                    heapq.heappush(fp, (key[v], v))
                    parent[v] = u

        custo = sum([key[i] for i in range(1, self.V)])
        print(f"Custo Prim: {custo}")

    # Kraskal
    def find_set(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find_set(parent, parent[i])
        return parent[i]

    def union_sets(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
    
    def agm_kruskal(self):
        result = []
        parent = [node for node in range(self.V)]
        rank = [0] * self.V

        self.arestas = sorted(self.arestas, key=lambda item: item[2])

        a = 0
        i = 0

        while a < self.V - 1:
            u, v, w = self.arestas[i]
            i += 1
            x = self.find_set(parent, u)
            y = self.find_set(parent, v)

            if x != y:
                a += 1
                result.append((u, v, w))
                self.union_sets(parent, rank, x, y)

        custo = sum([w for _, _, w in result])
        print(f"Custo Kruskal: {custo}")


if __name__ == "__main__":
    V = 500000

    # Mais rapido para o Kraskal
    # qtd_arestas = 500000

    # Mais rapido para o Prim
    qtd_arestas = 5

    arestas = []
    lst_vertices = [i for i in range(V)]

    for i in range(V - 1):
        arestas.append((i, i + 1, randint(1, 100)))

    for i in range(qtd_arestas):
        arestas.append((choice(lst_vertices), choice(lst_vertices), randint(1, 100)))


    g = Grafo(V)
    for u, v, w in arestas:
        g.add_aresta(u, v, w)

    inicio = time()
    g.agm_prim()
    fim = time()
    print(f"Tempo de execução - Prim: {fim - inicio:.8f} segundos")

    inicio = time()
    g.agm_kruskal()
    fim = time()
    print(f"Tempo de execução - Kruskal {fim - inicio:.8f} segundos")