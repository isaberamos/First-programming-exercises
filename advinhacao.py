from random import randint
from time import sleep
computador = randint(0,5)
print("Pensarei em um número entre 0 e 5...")
print('-=-' * 16)
jogador = int(input("Em que número pensei? "))
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print("Parabéns! Você ganhou :)")
else:
    print("GANHEI!!!! Pensei no número {} e não no {}".format(computador, jogador))
