def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res


def aumento(preco, taxa):
    res = preco + (preco * taxa/100)
    return res


def desconto(preco, taxa):
    res = preco - (preco * taxa/100)
    return res

