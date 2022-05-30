'''Escreva um programa que pergunte a que velocidade do carro de um usuário. Caso o valor informado seja maior que 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Neste caso, exiba o valor da multa, cobrando R$ 5,00 por Km acima dos 80 km/h'''

velocidade = int(input("Digite a velocidade do carro: "))
 
if velocidade >= 80:
    print("Motorista multado!")
    multa = (velocidade - 80) * 5
    print("O valor da multa será: R$", multa)
    
else:
    print("Ufa! Dessa vez levou multa...")