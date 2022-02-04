lista1 = [1,2,3,4,5]
lista2 = []

for i in lista1:
    lista2.append(i+1)

print(lista2)

print(list(map(lambda x: x+1, lista1)))