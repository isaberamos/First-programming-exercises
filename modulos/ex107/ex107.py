import moeda

p = float(input("Digite o preço: R$ "))
print(f"A metade do preço é R${moeda.metade(p)}")
print(f"O dobro do preço é R${moeda.dobro(p)}")
print(f"Aumentando 10% sobre o preço temos R${moeda.aumento(p, 10)}")
print(f"Reduzindo 13% sobre o preço temos R${moeda.desconto(p, 13)}")
