'''O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos, calcule e mostre:
O valor correspondente ao lucro do distribuidor;
O valor correspondente aos impostos;
O preço final do veículo;
'''

preco_fabrica = float(input("Preço de fábrica: R$"))
percentual_lucro = float(input("Percentual de lucro: "))
percentual_imposto = float(input("Percentual de imposto: "))

lucro_distribuidor = (percentual_lucro / 100) * preco_fabrica
valor_imposto = (percentual_imposto / 100) * preco_fabrica
preco_final = preco_fabrica + lucro_distribuidor + valor_imposto

print("O valor final do carro será R${:.2f}".format(preco_final))
