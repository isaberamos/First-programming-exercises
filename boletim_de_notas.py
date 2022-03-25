print('-=' * 20)
print('BOLETIM DE NOTAS'.center(20))
print('-=' * 20)
lista = []
while True:
    nome = str(input("Aluno: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    r = str(input("Adicionar novas informações? [S/N] "))
    if r in "Nn":
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MF":>8}')
print('-' * 30)
for i, a in enumerate(lista):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print('-' * 30)
    opcao = int(input("Selecione um aluno para ver as notas (999 interrompe): "))
    if opcao == 999:
        print("INTERROMPENDO PROGRAMA...")
        break
    if opcao <= len(lista) - 1:
        print(f'Notas de {lista[opcao][0]} são {lista[opcao][1]}')
print("-=" * 30)
