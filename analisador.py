soma_idade = 0
media_idade = 0
maior_homem = 0
nomeveio = " "
totmulher20 = 0
for c in range(1,5):
    print("\033[35m----- {}ª PESSOA -----".format(c))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    soma_idade += idade
    if c == 1 and sexo in "Mm":
        maior_homem = idade
        nomeveio = nome
    if sexo in "Mm" and idade > maior_homem:
        maior_homem = idade
        nomeveio = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1

media_idade = soma_idade / 4
print("A média de idade do grupo é {} anos".format(media_idade))
print("O homem mais velho se chama {} e tem {} anos".format(nomeveio, maior_homem))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))
