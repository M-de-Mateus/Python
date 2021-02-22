'''valores = 0
lista = []
for v in range(0, 5):
    valores = int(input('Digite um valor: '))
    lista.append(valores)
maior = lista[0]
menor = lista[0]
for m in lista:
    if m > maior:
        maior = m
    elif m < menor:
        menor = m

print(f'O maior valor da lista foi {maior} na posição {lista.index(maior)}!')
print(f'O menor valor da lista foi {menor} na posição {lista.index(menor)}!')'''


lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print(f'Você digitou os seguintes valores: {lista}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O maior valor digitado foi {menor} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()