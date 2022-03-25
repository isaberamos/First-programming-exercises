num = int(input("Digite um número: "))
while num >= 0:
    fact = 1
    while num > 1:
        fact = fact * num
        num = num - 1
    print(fact)
    num = int(input("Digite um número: "))
