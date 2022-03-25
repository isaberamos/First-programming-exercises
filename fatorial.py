'''from math import factorial as fact

def binomial(n, k):
    return fact(n) // fact(k) // fact(n - k)

print(binomial(5,3))'''

n = int(input("Digite o valor de n:"))
fat = 1
i = 2
while i <= n:
  fat = fat * i
  i = i + 1
print(fat)