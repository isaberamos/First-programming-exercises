'''Faça um programa que receba o ano de nascimento de uma pessoa, calcule e mostre:
Se ele já tem idade para votar (16 anos ou mais);
E para conseguir carteira de habilitação (18 anos ou mais);
'''

ano = 2022
nascimento = int(input("Digite o ano de nascimento: "))
idade = ano - nascimento

if idade >= 16 and idade < 18:
    print("Você já pode votar!")
elif idade >= 18:
    print("Você já DEVE votar e também pode tirar CNH!")
else:
    print("Logo a idade chegará...")
