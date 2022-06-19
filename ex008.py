'''Criar um algoritmo que imprima todos os números de 1 até 10, 
e a média geral todos eles (intervalo fechado). '''

media = 0

for n in range(1, 11):
    media = media + n
print(media / 10)
