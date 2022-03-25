palavras = ("Amarelo", "Verde", "Rosa",
            "Turquesa", "Marrom", "Preto",
            "Vermelho", "Branco", "Cinza")
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos ", end="")
    for letra in p:
        if letra.lower() in "aeiouAEIOU":
            print(letra, end=" ")
