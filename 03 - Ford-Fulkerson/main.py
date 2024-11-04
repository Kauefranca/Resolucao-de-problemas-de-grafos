from time import time
from utils import gerar_grafo

class Grafo:
    def __init__(self, grafo):
        self.grafo = grafo
        self.ROW = len(grafo)

    def bfs(self, origem, sumidouro, anterior):
        visitados = [False] * self.ROW
        fila = []
        fila.append(origem)
        visitados[origem] = True

        while fila:
            u = fila.pop(0)
            for i, val in enumerate(self.grafo[u]):
                if visitados[i] == False and val > 0:
                    fila.append(i)
                    visitados[i] = True
                    anterior[i] = u
                    if i == sumidouro:
                        return True
        return False

    def ford_fulkerson(self, origem, sumidouro):
        anterior = [-1] * self.ROW
        flx_max = 0

        while self.bfs(origem, sumidouro, anterior):
            caminho = float("Inf")
            s = sumidouro
            while(s != origem):
                caminho = min(caminho, self.grafo[anterior[s]][s])
                s = anterior[s]

            flx_max += caminho

            v = sumidouro
            while(v != origem):
                u = anterior[v]
                self.grafo[u][v] -= caminho
                self.grafo[v][u] += caminho
                v = anterior[v]

        return flx_max

g = Grafo(gerar_grafo(500))
origem = 99
sumidouro = 444

i = time()
print("O fluxo máximo da rede de distribuição de água é:", g.ford_fulkerson(origem, sumidouro))
print(f'Tempo: {(time() - i):.4f} segundos')

g = Grafo(gerar_grafo(1000))
origem = 55
sumidouro = 639

i = time()
print("O fluxo máximo da rede de transporte é:", g.ford_fulkerson(origem, sumidouro))
print(f'Tempo: {(time() - i):.4f} segundos')