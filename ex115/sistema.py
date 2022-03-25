from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = "curso.txt"
lista = []

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver cadastrados", "Cadastrar nova pessoa", "Alterar dados", "Sair do sistema"])
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        sexo = str(input("Sexo [F/M/ÑB/Ñ INFORMAR]: "))
        cadastrar(arq, nome.title(), idade, sexo.upper())
    elif resposta == 3:
        lerArquivo(arq)
        print("-" * 41)
        lista.append(arq)
        opcao = int(input("Nº de cadastro: "))
        if opcao <= len(lista) - 1:  # SELECIONAR O USUÁRIO PARA ACESSAR SUAS INFORMAÇÕES
            print(f"Você escolheu {lista[opcao][0]}")
        alteracao(["Selecione o que deseja alterar: ", "[1] Nome", "[2] Idade", "[3] Sexo"])
    elif resposta == 4:
        cabecalho("Saindo do sistema...")
        sleep(0.5)
        break
    else:
        print("\033[31mERRO! Digite uma opção válida\033[m")
    sleep(1)

