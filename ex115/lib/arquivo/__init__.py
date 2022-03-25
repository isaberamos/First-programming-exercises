from ex115.lib.interface import *

def arqExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Ocorreu um ERRO na criação do arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("ERRO ao abrir o arquivo")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        print(f'{"No.":<0}{"NOME":<2}{"IDADE":>20}{"SEXO":>10}')
        contador = 0
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            dado[2] = dado[2].replace("\n", "")
            contador += 1
            print(f"{contador:<3}{dado[0]:<13}{dado[1]:>10}{dado[2]:>10}")
    finally:
        a.close()


def cadastrar(arq, nome="Desconhecido", idade=0, sexo="Prefere não informar"):
    try:
        a = open(arq, "at")
    except:
        print("Houve um ERRO na abertura do arquivo")
    else:
        try:
            a.write(f"{nome};{idade};{sexo};\n")
        except:
            print("Houve um ERRO ao digitar os dados!")
        else:
            print(f"Novo registro de {nome} adicionado com sucesso!")
            a.close()

def alteraDados(arq, nome="Desconhecido", idade=0, sexo="Prefere não informar"):
    try:
        a = open(arq, "w+")
    except:
        print("Houve um ERRO na abertura do arquivo")
    else:
        try:
            a.write(f"{nome};{idade};{sexo}")
        except:
            print("Erro ao digitar os dados!")
        else:
            print(f"Registro alterado com sucesso!")
            a.close()
