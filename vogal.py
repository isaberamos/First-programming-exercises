def vogal(letra):
    if letra in 'a' or letra in 'e' or letra in 'i' or letra in 'o' or letra in 'u' or letra in 'A' or letra in 'E' or letra in'I' or letra in 'O' or letra in 'U':
        return True
    else:
        return False

print(vogal('a'))
print(vogal('b'))