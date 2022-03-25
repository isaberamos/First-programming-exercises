valores = []
for cont in range(0,5):
    valores.append(int(input("Digite o valor: ")))

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o índice {v}")
print("Finish list!")



a = [2,1,3]
b = a[:]
b[2] = 4
print(f'Lista A: {a}')
print(f'Lista B: {b}')