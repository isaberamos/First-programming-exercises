lista = []
while True:
    lista.append(int(input("Adicione o valor: ")))
    r = str(input("Quer continuar? [S/N] "))
    if r in "Nn":
        break
print(f"Você digitou {len(lista)} elemento(s)")
lista.sort(reverse=True)
print(f"Em ordem decrescente se torna {(lista)}")
if 5 in lista:
    print("O número 5 está na lista")
else:
    print("Não achei o número 5...")
