'''
pares = []
impares = []
principal = []
for c in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

principal.append(sorted(pares[:]))
principal.append(sorted(impares[:]))
pares.clear()
impares.clear()
print(principal)
'''

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')