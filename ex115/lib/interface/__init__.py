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


def linha(tam=41):
    return "-" * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(41))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for i in lista:
        print(f"\033[33m{c}\033[33m - \033[34m{i}\033[m")
        c += 1
    print(linha())
    opc = leiaInt("Sua opção: ")
    return opc

def alteracao(lista):
    cabecalho("ALTERAÇÃO DE DADOS")
    c = 1
    for i in lista:
        print(f"\033[35m{i}\033[m")
        c += 1
    print(linha())
    opc = leiaInt("Sua opção: ")
    return opc
