# Algoritmo de busca binária em forma recursiva

def busca_binaria(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista) - 1

    if max < min:
        return False
    else:
        meio = min + (max - min) // 2

    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio - 1)

    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio + 1, max)

    else:
        return meio


def teste_busca_binaria(lista, valor, esperado):
    assert busca_binaria(lista, valor, esperado) == esperado


a = [0,1,2,3,4,5,6,7]
print(teste_busca_binaria(a, 8, False))

