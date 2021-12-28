# Desenvolver um programa que pergunta a distância de uma viagem em Km. Calcular o preço da passagem,
# cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais distantes.

distancia = float(input("Qual é a distância da sua viagem? "))
print("Você começará uma viagem de {} Kms".format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print("O preço de sua passagem será R${:.2f}".format(preço))
