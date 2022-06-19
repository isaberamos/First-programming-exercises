num = int(input("Fatorial: "))
fat = 1

for n in range(1, num):
    fat = fat * num
    num = num - 1
print(fat)
