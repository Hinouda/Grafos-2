import math

#Arvore geradora minima algoritmo de prim.
#G é um grafo representado por matriz de adjacencias.
#w e uma matriz que representa o peso das arestas.
def MSTPrim(G, w, r):
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
        #retornar o indice do vertice de menor chave em Q
        menor = 0
        for i in range(1, len(Q)):
            if chave[Q[i]] < chave[Q[menor]]:
                menor = i
        
        u = Q.pop(menor)

        visitado[u] = True #o atributo visitado serve para não precisar percorrer Q para verificar se v ∈ Q.

        for v in G[u]:
            if visitado[v] == False and w[u][v] < chave[v]:
                p[v] = u
                chave[v] = w[u][v]

    return p