'''Pedro comprou um saco de ração, com peso em quilos. Ele possui dois gatos, para os quais fornece a quantidade de ração em gramas. A quantidade diária de ração fornecida para cada gato é sempre a mesma. Faça um programa que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato, calcule e mostre quanto restará de ração no saco após 5 dias de consumo.
'''

peso_racao = float(input("Peso do saco de ração: "))
quant_racao = float(input("Quantidade de ração dada: "))

quantidade = peso_racao - quant_racao * 2 * 5 / 1000

print("Em 5 dias, restará {}kg de ração".format(quantidade))