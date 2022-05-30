a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = int(input("Digite o quarto valor: "))
e = int(input("Digite o quinto valor: "))


if a > b and a > c and a > d and a > e:
    print("O maior valor é A")
elif b > a and b > c and b > d and b > e:
    print("O maior valor é B")
elif c > a and c > b and c > d and c > e:
    print("O maior valor é C")
elif d > a and d < b and d > c and d > e:
    print("O maior valor é D")
else:
    print("O maior valor é E")
