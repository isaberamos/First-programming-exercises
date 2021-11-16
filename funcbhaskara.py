import math
from math import sqrt

def delta(a,b,c):
    return b ** 2 - 4 * a * c

def main():
    a = float(input("Digite o valor do coeficiente a: "))
    b = float(input("Digite o valor do coeficiente b: "))
    c = float(input("Digite o valor do coeficiente c: "))
    raizes_funcao(a,b,c)

def raizes_funcao(a,b,c):
    d = delta(a,b,c)
    if d == 0:
         raiz1 = (-b + math.sqrt(d)) / (2 * a)
         print("A única raiz quadrada é", raiz1)
    else:
        if d < 0:
            print("Esta equação não possui raízes reais")
        else:
            raiz = sqrt(d)
            r1 = (b * - 1 + raiz) / (2 * a)
            r2 = (b * - 1 - raiz) / (2 * a)
            print("As raízes da equação são", r1, "e", r2)

main()