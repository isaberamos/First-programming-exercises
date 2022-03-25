from datetime import date
print("\033[35m-=-" * 10)
print("     ALISTAMENTO MILITAR") # Pode usar o texto.center(núm de linha)
print("\033[35m-=-" * 10)
atual = date.today().year
nascimento = int(input("Digite o ano de seu nascimento: "))
idade = atual - nascimento
if idade < 18:
    saldo = 18 - idade
    print("Hmmmm... sua hora vai chegar. Ainda faltam {} anos".format(saldo))
elif idade == 18:
    print("Já está na hora de se alistar!")
elif idade > 18:
    saldo = idade - 18
    print("Vish! Você já deveria ter se alistado há {} anos".format(saldo))
