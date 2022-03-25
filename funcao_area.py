def area(l, c):
    a = l * c
    print(f"A área de um terreno {l}x{c} é de {a}m²")

print("CONTROLE DE TERRENOS")
print("-=" * 10)
larg = int(input("LARGURA (m): "))
comp = int(input("COMPRIMENTO (m): "))
area(larg, comp)