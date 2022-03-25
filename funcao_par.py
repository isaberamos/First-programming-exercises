def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

while True:
    num = int(input("Digite um valor: "))
    print(par(num))
    r = str(input("Quer continuar? [S/N] "))
    if r in "Nn":
        print("   ATÉ MAIS!")
        break
