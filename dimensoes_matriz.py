def calcula_dimensoes(matriz):
    altura = len(matriz)
    largura = 1
    for item in matriz:
        largura = len(item)
        break
    return "{}".format(altura) + "X" + "{}".format(largura)

def dimensoes(matrix):
    print(calcula_dimensoes(matrix))

minha_matriz = [[1], [2], [3]]
dimensoes(minha_matriz)
