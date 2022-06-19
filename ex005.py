x = int(input("Informe um número que deseja ver a tabuada: "))
mult = 0

for num in range(1, 11):
    mult = x * num
    print(f"{x} * {num} = {mult}")
    