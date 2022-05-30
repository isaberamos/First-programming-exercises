x = int(input("Valor de x: "))
y = int(input("Valor de y: "))

aux = x
maior = 0
valor = int(x + y) / 100 * 30

if valor >= 500:
    x = y
    y = aux
    print(f"O valor de x é {x} e o valor de y é {y}")
else:
    if x < y:
        print(f"O menor valor é x, e portanto, {x}")
    else:
        print(f"O menor valor é x, e portanto, {y}")
