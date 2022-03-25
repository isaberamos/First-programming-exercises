from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    ano = int(input("Digite o {}º ano de nascimento: ".format(c)))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("No total são {} pessoas maiores de idade".format(totmaior))
print("E {} pessoas menores de idade".format(totmenor))
