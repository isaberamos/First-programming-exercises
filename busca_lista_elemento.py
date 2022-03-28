def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) - 1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo)// 2
        if lista[meio] == elemento:
            return meio
        elif elemento > lista[meio]:
            primeiro = meio + 1
        elif elemento < lista[meio]:
            ultimo = meio - 1
        else:
            return False
    return -1