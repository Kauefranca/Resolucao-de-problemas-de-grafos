from random import randint, random

def gerar_grafo(num_linhas):
    grafo = [[0 for _ in range(num_linhas)] for _ in range(num_linhas)]
    
    for i in range(num_linhas - 1):
        for j in range(i + 1, num_linhas):
            if random() < 0.4:
                grafo[i][j] = randint(1, 20)
    
    return grafo