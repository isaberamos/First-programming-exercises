'''João recebeu seu salário e precisa pagar duas contas atrasadas. Em razão do atraso, ele deverá pagar multa de 2% sobre cada conta. Faça um programa que lê o valor do salário, das duas contas e calcule e mostre quanto restará do salário de João.
'''

salario = float(input("Informe o salário: R$"))
fatura1 = float(input("Informe o valor da primeira fatura: R$"))
fatura2 = float(input("Informe o valor da segunda fatura: R$"))

restante_salario = salario - ((fatura1 + fatura2) / 100 * 2)

print("Restante do salário: R${}".format(restante_salario))
