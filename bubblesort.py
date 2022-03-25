class Ordenador:
    def selecao_direta(self, lista):

        fim = len(lista)

        for i in range(fim - 1):
            # Inicialmente o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

        # Coloca o menor elemento encontrado no início da sub-lista
        # Para isso, trocar de lugar os elementos nas posições i e posição_do_minimo
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

    def bolha(self, lista):
        fim = len(lista)
        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    def bubble(self, lista):
        n = len(lista)
        for j in range(n-1):
            for i in range(n-1):
                if lista[i] > lista[i+1]:
                    # troca de elementos nas posições i e i+1
                    lista[i], lista[i+1] = lista[i+1], lista[i]

lista = [5,2,1,3,4]
o = Ordenador()
o.bolha(lista)
print(lista)