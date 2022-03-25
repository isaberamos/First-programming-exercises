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

        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    def bubbleshort(self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                return

'''lista = [52, 2, -7, 4]
o = Ordenador()
o.selecao_direta(lista)
print(lista)'''