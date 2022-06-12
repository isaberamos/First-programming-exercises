a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a < b and b < c:
    print("Crescente")
    print(a, b, c)
elif b < c and c < a:
    print(b, c, a)
elif b < a and a < c:
    print(b, a, c)
elif a < c and c < b:
    print(a, c, b)
elif a < b and b < c:
    print(a, c, b)
elif c < b and b < a:
    print(c, b, a)
elif c < a and a < b:
    print(c, a, b)
elif a > b and b < a:
    print(b, a, c)
else:
    print("Opção inválida")
