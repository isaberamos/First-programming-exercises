largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
a = altura
l = largura
while altura > 0:
    x = 0
    while x < largura:
        if altura == (a) or x == (l - 1) or altura == 1 or x == 0:
            print("#" , end = '')
        else:
            print(" " , end = '')
        x+=1
    altura = altura - 1
    print()