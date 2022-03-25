n = int(input("Digite um número inteiro >1: "))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade += 1
        n = n // fator
    if multiplicidade > 0:
        print("O fator ", fator, "multiplicidade = é ", multiplicidade)
    fator = fator + 1
    multiplicidade = 0