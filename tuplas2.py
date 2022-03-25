n = (int(input("Digite o primeiro valor: ")),
     int(input("Digite o segundo valor: ")),
     int(input("Digite o terceiro valor: ")),
     int(input("Digite o quarto valor: ")))
print("Você digitou {}".format(n))
print("O número 9 aparece {}x ".format(n.count(9)))
if 3 in n:
    print("O número 3 aparece na {}ª posição".format(n.index(3)))
else:
    print("O número 3 não apareceu nenhuma vez")
print("Os números pares digitados foram ", end=" ")
for c in n:
    if c % 2 == 0:
        print(n, end=" ")

