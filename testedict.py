'''pessoas = {"Nome" : "Franco", "Idade" : 27}
pessoas["Nome"] = "Leandro"
for k, v in pessoas.items():
    print((f"{k} = {v}"))'''

'''brasil = []
estado = {"UF" : "Santa Catarina", "sigla" : "SC"}
brasil.append(estado)

print(estado)'''

'''estado = dict()
brasil = list()
for c in range(0,3):
    estado["UF"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")'''
#                 OU
'''for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print()'''