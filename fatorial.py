from math import factorial as fact

def binomial(n, k):
    return fact(n) // fact(k) // fact(n - k)

print(binomial(5,3))