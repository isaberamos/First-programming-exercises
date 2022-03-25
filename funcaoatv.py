from time import sleep

def maior(* num):
    print("\nAnalisando os valores passados...")
    sleep(1)
    cont = maior = 0
    for valor in num:
        print(f"{valor} ",end="", flush=True)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"foram informados. No total, são {cont} valores.")
    print(f"O maior valor informado foi {maior}.")


# Programa principal
maior(20, 35, 45, 98, 100)
maior(2, 5, 6, 10, 15, 8, 4)