soma = 0
cont = 0
for impar in range(1,501,2):
    if impar % 3 == 0:
        cont = cont + 1
        soma = soma + impar
print('\33[35mA soma de todos os {} valores solicitados é {}.'.format(cont,soma))