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
    matriz = transformarManejo(matriz)
    result = FloydWarshall(matriz)
    printMatriz(result)

def transformarManejo(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if((matriz[i][j] == 0) and (i != j)):
                matriz[i][j] = float('inf')
    return matriz

def FloydWarshall(pesos):
    for k in range(len(pesos)):
        for i in range(len(pesos)):
            if i != k:
                for j in range(len(pesos)):
                    if(pesos[i][j] > (pesos[i][k] + pesos[k][j]) and (j != k)):
                        pesos[i][j] = pesos[i][k] + pesos[k][j]
    return pesos

def inicializarMatriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = [0] * colunas
        matriz.append(linha)
    return matriz

def printMatriz(matriz):
    for linha in range(len(matriz)):
        print(matriz[linha])

if __name__ == "_main":
    main()