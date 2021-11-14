n = int(input("Digite uma sequência de números: "))

quantidadeNumero = len(n)
contador = 1
valor = 0

while contador <= quantidadeNumero:
    valor = n % 10 and n // 10
    valor = n + 1
    contador = contador + 1;
    # print("A soma dos números é: ", valor)
