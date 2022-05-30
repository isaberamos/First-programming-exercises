'''Implemente a função encontra_impares(lista), que recebe como parâmetro uma lista de
números inteiros e devolve uma outra lista apenas com os números ímpares da lista dada.'''

def encontra_impares(lista):
    impar = []
    if len(lista) > 0:
        if lista[0] % 2 != 0:
            impar.append(lista[0])
        impar.extend(encontra_impares(lista[1:]))
    return impar
