largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

count = largura
while altura > 0:
    altura = altura - 1

    largura = count

    while largura > 0:
        largura = largura - 1
        print('#', end = '')
    print('', end="\n")
