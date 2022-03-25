from time import sleep
print("Analisador de triângulos")
sleep(2)
r1 = float(input("Digite a reta 1: "))
r2 = float(input("Digite a reta 2: "))
r3 = float(input("Digite a reta 3: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos dados PODEM formar triângulos!")
else:
    print("Os segmentos dados NÃO PODEM formar triângulos!")
