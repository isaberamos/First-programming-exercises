print ("Digite uma sequência de números terminada por zero.")

soma = 0
valor = 1

while valor != 0:
    valor = int(input("Digite o valor a ser somado: "))
    soma = soma + valor
print("A soma da sequência é ", soma)