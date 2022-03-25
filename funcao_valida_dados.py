def leiaInt(txt):
    ok = False
    valor = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido: \033[m")
        if ok:
            break
    return valor


#Programa principal
n = leiaInt("Digite um número inteiro: ")
print(f"Você digitou {n}")
