matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacol = maior = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}][{coluna}]: "))
for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()
print("~" * 30)
print(f"A soma dos pares é {somapar}")
for l in range(0,3):
    somacol += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {somacol}")
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"O maior elemento da 2ª linha é {maior}")
