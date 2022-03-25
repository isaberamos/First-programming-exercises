def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except(ValueError, TypeError):
            print("\033[31mERRO com os dados digitados!\033[m")
            continue
        except(KeyboardInterrupt):
            print("\n\033[31Usuário preferiu não infomar o número\033[m")
        else:
            return n


def leiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except(ValueError, TypeError):
            print("\033[31mERRO com os dados digitados!\033[m")
            continue
        else:
            return n


# Programa principal
n = leiaInt("Digite um número inteiro: ")
print(f"Você acabou de digitar o inteiro {n}")
n0 = leiaFloat("Digite um número real: ")
print(f"Você acabou de digitar o real {n0}")