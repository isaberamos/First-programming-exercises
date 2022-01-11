from time import sleep

opcao = 0
soma = 0
maior_valor = 0
mult = 0

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

while opcao != 5:
    print("""SELECIONE UMA OPÇÃO DO MENU:
    [1] Somar
    [2] Multiplicar
    [3] Maior valor
    [4] Novos números
    [5] Sair do programa""")
    opcao = int(input(">>>Digite a opção desejada: "))

    if opcao == 1:
        soma = valor1 + valor2
        print("A soma de {} + {} é {}".format(valor1, valor2, soma))
    elif opcao == 2:
        mult = valor1 * valor2
        print("A multiplicação de {} x {} é {}".format(valor1, valor2, mult))
    elif opcao == 3:
        if valor1 > valor2:
            maior_valor = valor1
        else:
            maior_valor = valor2
        print("O maior valor é {}".format(maior_valor))
    elif opcao == 4:
        print("Informe os números novamente: ")
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))
        print("Os novos valores são {} e {}".format(valor1, valor2))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção inválida")
    sleep(1)
    print("=" * 30)

print("Fim do program!")
