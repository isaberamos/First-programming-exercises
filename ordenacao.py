string = "não está em ordem crescente"
posicoes = ["primeiro", "segundo", "terceiro"]
valores = []

for i in range(0, 3):
    nota = float(input('Digite o %s numero: ' % posicoes[i]))
    valores.append(nota)

if sorted(valores) == valores:
    string = "crescente"

print(string)