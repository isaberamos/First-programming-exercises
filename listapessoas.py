dado = []
pessoas = []
maior = 0
menor = 0
while True:
    dado.append(str(input("Digite o nome: ")))
    dado.append(float(input("Digite o peso: ")))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    r = str(input("Deseja continuar? [S]/N] "))
    if r in "Nn":
        break
print("-=" * 25)
print(f"No total, foram cadastradas {len(pessoas)} pessoas")
print(f"O maior peso foi {maior}Kg. Peso de ", end="")
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}]", end="")
print()
print(f"O menor peso foi {menor}Kg. Peso de ", end="")
for p in pessoas:
    if p[1] == menor:
       print(f"[{p[0]}]", end="")
print()
