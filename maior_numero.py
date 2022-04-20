def maior(* lista):
    maior = 0
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior