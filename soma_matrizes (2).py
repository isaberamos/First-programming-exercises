'''import matriz

def soma_matrizes(A, B): # Recebe duas matrizes como parâmetro
    num_linhas = len(A) # Comprimento de linhas
    num_colunas = len(A[0]) # Comprimento da linha 0 de A
    C = matriz.cria_matriz(num_linhas, num_colunas, 0)

    for linha in range(num_linhas): #percorre as linhas da matriz
        for coluna in range(num_colunas): #percorre as colunas da matriz
            C[linha][coluna] = A[linha][coluna] + B[linha][coluna]
    return C

print(soma_matrizes(A, B))'''

def calcula_dimensoes(matriz):
    height = len(matriz)
    width = 1
    for item in matriz:
        width = len(item)
        break
    return height, width

def soma_matrizes(m1, m2):
    h, w = calcula_dimensoes(m1)
    if calcula_dimensoes(m1) != calcula_dimensoes(m2):
        return False
    else:
        m3 = m1
        for i in range(0, h):
            for j in range(0, w):
                m3[i][j] = m1[i][j] + m2[i][j]
    return m3
