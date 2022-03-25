print("-" * 50)
print("             LISTAGEM DE PREÇOS")
print("-" * 50)
itens = ("Massa italiana", 15.50,
         "Vinho tinto seco gringo", 65.75,
         "Cogumelos selvagens", 11.50,
         "Cebola roxa", 3.77)

for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f"{itens[pos]:.<35}",end="")
    else:
        print(f"R${itens[pos]:.>10.2f}")
print("-" * 50)
