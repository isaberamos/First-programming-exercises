from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = "curso.txt"

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver cadastrados", "Cadastrar nova pessoa", "Sair do sistema"])
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo do sistema...")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida\033[m")
    sleep(1)

