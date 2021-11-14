n = int(input("Digite um número: "))

if (n % 3 == 0) and (n % 5 == 0):
    print("FizzBuzz")
else:
    if (n % 3 != 0) or (n % 5 != 0):
     print(n)