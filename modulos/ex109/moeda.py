def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def aumento(preco=0, taxa=0, format=False):
    res = preco + (preco * taxa/100)
    return res if format is False else moeda(res)


def desconto(preco=0, taxa=0, format=False):
    res = preco - (preco * taxa/100)
    return res if format is False else moeda(res)


def moeda(preco=0, moeda="R$ "):
    return f"{moeda}{preco:.2f}".replace(".", ",")

