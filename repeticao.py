meuCartao = int(input("Digite o número do cartão de crédito: "))

cartaolido = 1
encontreiMeuCartaoNaLista = False

while cartaolido != 0 and not encontreiMeuCartaoNaLista:
    cartaolido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaolido == meuCartao:
        encontreiMeuCartaoNaLista = True

if encontreiMeuCartaoNaLista:
    print("Encontrei!!!")
else:
    print("Não encontrei :(")