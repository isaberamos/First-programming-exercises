terminou = False
count = 1
while (not terminou):
    n = int(input("Digite um número: "))
    if n == 0:
        terminou = True
    else:
        if n % 2 != 0:
            count += 1
            print(n, "é um número primo")
        else:
            n % 2 == 0
            print(n, "não é um número primo")