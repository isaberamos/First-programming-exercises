# Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

def remove_repetidos(lista):
    l1 = []
    for i in lista:
        if i not in l1:
            l1.append(i)
    l1.sort()
    return l1

lista = []

lista = remove_repetidos(lista)
print(lista)
