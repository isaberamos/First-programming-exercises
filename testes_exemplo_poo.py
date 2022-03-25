'''class Carro:
    pass

meu_carro = Carro()
carro_do_ime = Carro()

meu_carro.ano = 1965
meu_carro.modelo = "Fusca"
meu_carro.cor = "Rosa"

print(meu_carro.ano)

carro_do_ime.ano = 1975
carro_do_ime.modelo = "Kombi"
carro_do_ime.cor = "Azul"

print(carro_do_ime.ano)

novo_fusca = carro_do_ime

novo_fusca.ano += 10

print(novo_fusca.ano)'''

'''class Pato:
  pass

pato = Pato()
patinho = Pato()
if pato == patinho:
  print("Estamos no mesmo endereço!")
else:
  print("Estamos em endereços diferentes!")'''

class Carro:
    def __init__(self, m, a, c):
        self.modelo = m
        self.ano = a
        self.cor = c

brasilia = Carro('Brasilia', 1968, 'amarela')
fusca = Carro('Fusca', 1981, 'preto')

fusca.ano += 10   # observe que podemos acessar atributos de fusca
print(fusca.ano)

class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano    = ano
        self.cor    = cor

meu_carro = Carro("Kombi", 1975, "Branca")

print(meu_carro.ano)

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome   = nome
        self.idade  = idade
        self.altura = altura

class Cachorro:
    def __init__(self, raça, idade, nome, cor):
        self.raça = raça
        self.idade = idade
        self.nome = nome
        self.cor = cor


rex = Cachorro('vira-lata', 2, 'Bobby', 'marrom')

