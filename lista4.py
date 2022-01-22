valores = list()
while True:
        n = int(input("Digite um valor: "))
        if n not in valores:
            valores.append(n)
            print("Valor adicionado!")
        else:
            print("Valor duplicado! Não será adicionado à lista")
        r = str(input("Quer continuar? [S/N] "))
        if r in "Nn":
                break
print("=" * 40)
valores.sort()
print(f"A lista é composta dos elementos {valores}")
