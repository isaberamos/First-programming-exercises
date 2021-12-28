print("\033[35m-=-" * 10)
print("     CÁLCULO DE IMC")
print("\033[35m-=-" * 10)
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Abaixo do peso. IMC \33[34m{:.2f}".format(imc))
elif imc >= 18.5 and imc < 25:
    print("Peso ideal. IMC \33[34m{:.2f}".format(imc))
elif imc >= 25 and imc < 30:
    print("Sobrepeso. IMC \33[34m{:.2f}".format(imc))
elif imc >= 30 and imc < 40:
    print("Obesidade. IMC \33[34m{:.2f}".format(imc))
elif imc > 40:
    print("Obesidade mórbida. IMC {:.2f}".format(imc))
