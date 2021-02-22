valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
for c in valores:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'Os valores digitados foram: {valores}')
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')
