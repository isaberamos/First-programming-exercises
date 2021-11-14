from math import sqrt

# try:
a = float(input("Digite o valor do coeficiente a: "))
b = float(input("Digite o valor do coeficiente b: "))
c = float(input("Digite o valor do coeficiente c: "))

delta = b ** 2 - 4 * a * c

if delta >= 0:
    raiz = sqrt(delta)
    print("A raiz quadrada é", raiz)
    x1 = (b * - 1 + raiz) / (2 * a)
    x2 = (b * - 1 - raiz) / (2 * a)
    print("As raízes da equação são", x1, "e", x2)

else:
    print("Esta equação não possui raízes reais")
