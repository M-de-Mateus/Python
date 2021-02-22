lista1 = []
lista2 = []
igualdade = 0
for x in range(0, 5):
    v1 = int(input('Digite um valor para a primeira lista: '))
    lista1.append(v1)
for y in range(0, 5):
    v2 = int(input('Digite um valor para a segunda lista: '))
    lista2.append(v2)

for x, z in zip(lista1, lista2):
    if x == z:
        print(x)
        igualdade += 1
if igualdade == 0:
    print('Não tem!')
