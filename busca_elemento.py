def busca(lista, elemento):
	for i in range(len(lista)):
		if lista[i] == elemento:
			return i
	return False

o = busca([0,7,8,5,10], 10)
print(o)