def cria_matriz(num_linhas, num_colunas):
    '''(int, int, valor) -> matriz(lista de valores)
        Cria e retorna uma matriz com num_linhas e num_colunas
        colunas em que cada elemento é digitado pelo usuário.
        '''

    '''Modificar o código de forma que ao invés de ele inicializar
        a matriz com um elemento pré definido em todas as posições,
        ele vá lendo do teclado interpretar os elementos da matriz.
            '''

    matriz = [] # lista vazia
    for i in range(num_linhas):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)

        # adiciona linha a matriz
        matriz.append(linha)
    return matriz


def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    return cria_matriz(lin, col)

print(le_matriz())