seq = []
n = 1

while n:
    n = int(input(print("Digite um número: ")))
    if n != 0:
        seq.append(n)
    print(seq)
    print(seq[:-1])
