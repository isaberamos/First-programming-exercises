from math import sqrt

a = int(input("Digite o primero número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
d = int(input("Digite o quarto número: "))

p1 = a and b
p2 = c and d

distancia = sqrt((a - b) ** 2 + (c - d) ** 2)

if distancia < 10:
    p1 = sqrt(distancia)
    p2 = sqrt(distancia)
    print("Perto")
else:
    if distancia > 10:
      p1 = sqrt(distancia)
      p2 = sqrt(distancia)
      print("Longe")
