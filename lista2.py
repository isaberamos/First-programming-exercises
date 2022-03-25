lista = []
par = []
impar = []
while True:
    valor = int(input("Adicione o valor: "))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    lista = [par] + [impar]
    r = str(input("Quer continuar? [S/N] "))
    if r in "Nn":
        break
print(f"A lista completa é {lista}")
print(f"A lista de pares é {par}")
print(f"A lista de ímpares é {impar}")


# Outra forma de fazer com que a lista apareça junta:
'''num = []
while True:
    num.append(int(input....

for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else v % 2 == 1:
        impar.append(v)
'''
