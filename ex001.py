idade = int(input("Idade: "))
sexo = str(input("Sexo: "))

if sexo == "F"  or sexo == "f" :
    if idade <=  12:
        print("Menina")
    elif idade > 12 and idade < 24:
        print("Moça")
    else:
        print("Mulher")
elif sexo == "M" or sexo == "m":
    if idade <= 12:
        print("Menino")
    elif idade > 12 and idade < 24:
        print("Moço")
    else:
        print("Homem") 
else:
    print("Digite uma opção válida")