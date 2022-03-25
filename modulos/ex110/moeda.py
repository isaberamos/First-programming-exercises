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

def resumo(preco=0, taxaa=10, taxa=5):
    print("-" * 30)
    print(f"RESUMO DO VALOR".center(30))
    print("_" * 30)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metade do preço: \t{metade(preco, True)}")
    print(f"{taxaa}% de aumento: \t{aumento(preco, taxaa, True)}")
    print(f"{taxa}% de desconto: \t{desconto(preco, taxa, True)}")
    print("_" * 30)
