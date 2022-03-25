import moeda


p = float(input("Digite o preço: R$ "))
print(f"A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"Aumentando 10% sobre o preço temos {moeda.moeda(moeda.aumento(p, 10))}")
print(f"Reduzindo 13% sobre o preço temos {moeda.moeda(moeda.desconto(p, 13))}")