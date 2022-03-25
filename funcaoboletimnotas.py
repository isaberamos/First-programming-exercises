def boletim(*n, sit=False):
    """
    --> Função que analisa a situação de vários alunos.
    :param n: aceita uma ou mais notas
    :param sit: opcional; indicando se deve ou não adicionar a situação
    :return: dicionário com informações da situação do boletim
    """
    r = dict()
    r["total"] = len(n) # Quantidade de notas
    r["maior"] = max(n) # Nota máxima
    r["menor"] = min(n) # Nota mínima
    r["media"] = sum(n) / len(n)  # Soma das notas / quantidade de notas
    if sit:
        if r["media"] >= 7:
            r["situação"] = "BOA"
        elif r["media"] >= 5:
            r["situação"] = "RAZOÁVEL"
        else:
            r["situação"] = "RUIM"
    return r


# Programa principal
r = boletim(5.5, 6.5, 7.0, 8.5, sit=True)
help(boletim)