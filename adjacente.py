n_salvo = n = int(input("Digite uma sequência numérica: "))

anterior = n % 10
n = n // 10
adj_iguais = False
post = 0

while n > 0 and not adj_iguais:
   atual = n % 10
   if atual == anterior:
     adj_iguais = True
   else:
     post += 1
   anterior = atual
   n = n // 10

if adj_iguais:
    print(n_salvo, "tem os dígitos", atual, "que são adjacentes")
else:
    print(n_salvo, "não possui dígitos iguais adjacentes")
