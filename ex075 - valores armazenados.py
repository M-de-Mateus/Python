valores = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
par = 0
print(f'Você digitou os valores {valores}!')
try:
    print(f'O valor 9 apareceu {valores.count(9)} vez(es)!')
except:
    print('O valor 9 apareceu 0 vez(es)!')
try:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição!')
except:
    print('O valor 3 não apareceu!')
finally:
    for c in valores:
        if c % 2 == 0:
            par += 1
    print(f'Os valores pares digitados foram {par}!')