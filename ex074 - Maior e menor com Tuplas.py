from random import randint
n = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
maior = n[0]
menor = n[0]
for c in n:
    if c > maior:
        maior = c
    elif c < menor:
        menor = c
print(f'Os valores sorteados foram {n}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
