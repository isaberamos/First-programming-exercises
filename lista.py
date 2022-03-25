lista = []
for cont in range(1,6):
    lista.append(int(input(f"Digite o {cont}º valor: ")))
print(f"O maior valor é {max(lista)} e está na posição {lista.index(max(lista))}")
print(f"O menor valor é {min(lista)} e está na posição {lista.index(min(lista))}")



'''Ou há um jeito mais sofisticado de resolver, porém mais longo:

listanum = []
mai = 0
men = 0
for c in range(0,5):
    listanum.append(int(input("Digite um valor para a posição {c}: )))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if:
            if listanum[c] < men:
            men = listanum[c]
print(f"Você digitou os valores {listanum}")
print(f"O maior valor digitado foi {mai} e o menor foi {men} nas posições ")
for i, v in enumerate(listanum):
    if v == mai:
        print(f"{i}..., end="")
for i, v in enumerate(listanum):
    if v == men:
        print(f"{i}..., end="")
    '''
