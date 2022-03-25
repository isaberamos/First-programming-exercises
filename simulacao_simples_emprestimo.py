print("\033[35m-=-" * 10)
print("   SIMULADOR DE EMPRÉSTIMO")
print("\033[35m-=-" * 10)
valor_casa = float(input("Informe o valor da casa: R$ "))
valor_salario = float(input("Informe o valor do seu salário: R$ "))
prestacao_anos = float(input("Informe em quantos anos deseja pagar: R$ "))
valor_prestacao = valor_casa / (prestacao_anos * 12)
if valor_prestacao <= (valor_salario * 30 / 100):
    print("O valor de sua prestação será de R${:.2f} :)".format(valor_prestacao))
else:
    print("Ops. O valor da prestação excede no seu salário :(")
