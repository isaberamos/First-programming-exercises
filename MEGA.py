from random import randint
from time import sleep
lista = []
jogos = []
print("-" * 20)
print("   JOGO DA MEGA")
print("-" * 20)
qt = int(input("Quantos jogos para hoje? "))
tot = 1
while tot <= qt:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f" >>>>>SORTEANDO {qt} JOGOS<<<<<")
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")
    sleep(1)
print("    >>>>>>BOA SORTE<<<<<<")
