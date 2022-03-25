class Musica:
    def __init__(self, titulo, interprete, compositor, ano): # Construtor da classe
        # Lista de objetos do tipo música
        self.titulo = titulo
        self.interprete = interprete
        self.compositor = compositor
        self.ano = ano

class Buscador:
    def busca_por_titulo(self, playlist, titulo):
        for i in range(len(playlist)):
            if playlist[i].titulo == titulo:       # Comparando com o atributo
                return i
        return -1                               # Indica que não encontrou a música na playlist

    def vamos_buscar(self):
        playlist = [Musica("Ponta de areia", "Milton Nascimento", "Milton Nascimento", 1975),
                    Musica("Luz de tieta", "Caetano Veloso", "Caetano Veloso", 1984),
                    Musica("Baby", "Gal Costa", "Caetano Veloso", 1969)]

        onde_achou = self.busca_por_titulo(playlist, "Baby")

        if onde_achou == -1:
            print("Minha música preferida não está na playlist :(")
        else:
            preferida = playlist[onde_achou]
            print(preferida.titulo, preferida.interprete, preferida.compositor, preferida.ano,
                  sep = ", ")


b = Buscador()
b.vamos_buscar()
print(b)