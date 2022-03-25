print("-" * 30)
print("    SEQUÊNCIA DE FIBONACCI")
print("-" * 30)
t = int(input("Digite quantos termos deseja mostrar: "))
t1 = 0
t2 = 1
print("{} > {}".format(t1, t2), end="")
cont = 3
while cont <= t:
    t3 = t1 + t2
    print(" > {}".format(t3), end="")
    cont+= 1
    t1 = t2
    t2 = t3
print(" > FIM")