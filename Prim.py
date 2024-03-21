import math

def main():
    matriz = [
        [0, 5, 0, 0, 0, 8, 0, 0, 0, 2],
        [5, 0, -1, 0, 0, 3, 0, 0, 0, 3],
        [0, -1, 0, -1, 0, 3, 3, 2, 3, 3],
        [0, 0, -1, 0, 8, 1, 7, 4, 1, 6],
        [0, 0, 0, 8, 0, 0, 9, 0, 4, 0],
        [8, 3, 3, 1, 0, 0, 4, -1, 0, 0],
        [0, 0, 3, 7, 9, 4, 0, -4, 6, 0],
        [0, 0, 2, 4, 0, -1, -4, 0, 0, 0],
        [0, 0, 3, 1, 4, 0, 0, 0, 0, 7],
        [2, 3, 3, 6, 0, 0, 0, 0, 7, 0]
    ]

    print(MSTPrim(matriz, 0))

# Arvore geradora minima algoritmo de prim.
# G é um grafo representado por matriz de adjacencias.
# w e uma matriz que representa o peso das arestas.
def MSTPrim(G, r):
    chave = []
    p = []
    visitado = []
    Q = []

    for u in range(len(G)):
        chave.append(math.inf)
        visitado.append(False)
        p.append(None)
        Q.append(u)
        
    chave[r] = 0

    while len(Q) > 0:
        # retornar o indice do vertice de menor chave em Q
        menor = 0
        for i in range(1, len(Q)):
            if chave[Q[i]] < chave[Q[menor]]:
                menor = i
        
        u = Q.pop(menor)

        visitado[u] = True # o atributo visitado serve para não precisar percorrer Q para verificar se v ∈ Q.

        for v in G[u]:
            if visitado[v] == False and G[u][v] < chave[v]:
                p[v] = u
                chave[v] = G[u][v]

    return p

if __name__ == "__main__":
    main()