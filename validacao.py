sexo = str(input("Digite o sexo [F/M/Outro]: ")).strip().upper()[0]
while sexo not in "MmFfOutro":
    sexo = str(input("Dados inválidos. Digite novamente: ")).strip().upper()[0]
print("Sexo {} registrado com sucesso!".format(sexo))