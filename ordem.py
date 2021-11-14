n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if int(n1 < n2 and n2 < n3):
    print("Crescente")
else:
    if int(n1 > n2 and n2 > n3):
        print("Decrescente")