print("=" * 20)
print(" LOJINHA FACADINHA")
print("=" * 20)

produto = float(input("Valor do produto que você está namorando: R$ "))
print("""OPÇÕES DE PAGAMENTO
[1] Dinheiro ou cheque
[2] À vista no cartão
[3] Parcelado em 2x
[4] Parcelado 3x ou mais""")

condicao = int(input("Selecione a forma de pagamento que deseja: "))

if condicao == 1:
    condicao = produto - (produto * 10 / 100)
    print("Nessa forma de pagamento o produto custará {:.2f}, ou seja, \33[34m10%\33[34m de desconto".format(condicao))
elif condicao == 2:
    condicao = produto - (produto * 5 / 100)
    print("Nessa forma de pagamento o produto custará {:.2f}, ou seja, \33[34m5%\33[34m de desconto".format(condicao))
elif condicao == 3:
    condicao = produto
    print("Nessa forma de pagamento o preço do produto não acumula juros, continua \33[34m{:.2f}".format(condicao))
elif condicao == 4:
    condicao = produto + (produto * 20 / 100)
    totalparc = int(input("Quantas parcelas? "))
    parcela = condicao / totalparc
    print("Parcelando em {}x, as parcelas serão de {:.2f}, acumulando 20% de juros, e o valor final do produto é \33[34m{:.2f}.".format(totalparc, parcela, condicao))
