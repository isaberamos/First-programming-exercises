n = list()
for i in range(0, 5):
    valor = int(input(f"Digite o {i} valor: "))
    if i == 0 or valor > n[-1]:
        n.append(valor)
        print("Adicionado ao final da lista")
    else:
        pos = 0
        while pos < len(n):
            if valor <= n[pos]:
                n.insert(pos, valor)
                print(f"Adicionado na posição {pos}")
                break
            pos += 1
print(f"Os valores digitados em ordem foram {n}")
