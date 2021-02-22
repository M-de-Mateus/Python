'''def maior (x, y, z):
    max = x

    if y > max:
        max = y
    if z > max:
        max = z

    return max

def menor (x, y, z):
    min = x

    if y < min:
        min = y
    if z < min:
        min = z
    return min

def menu():
    x = int(input('Digite o primeiro número: '))
    y = int(input('Digite o segundo número: '))
    z = int(input('Digite o terceiro número: '))
    print()
    print('=' * 30)
    print('=' * 30)
    print('O maior número é {}'.format(maior(x, y, z)))
    print('O menor número é {}'.format(menor(x, y, z)))
    print('=' * 30)
    print('=' * 30)
    print()
while True:
    menu()'''

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}!'.format(menor))
print('O maior valor digitado foi {}!'.format(maior))
