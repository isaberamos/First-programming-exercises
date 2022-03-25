princ = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        princ[0].append(valor)
    else:
        if valor % 2 != 0:
            princ[1].append(valor)
princ[0].sort()
princ[1].sort()
print(f"Os números pares são: {princ[0]}")
print(f"Os números ímpares são: {princ[1]}")
