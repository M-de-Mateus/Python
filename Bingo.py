from random import randint
from time import sleep
numero = []
continuar = ''
while True:
    print('Sorteando', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.')
    sleep(1)

    sorteio = randint(1, 100)
    if sorteio in numero:
        print('Número já sorteado!')
    else:
        numero.append(sorteio)
        print('\033[0;32m-=\033[m' * 15)
        print(f'O número sorteado foi: \033[1;31m{sorteio}\033[m!')
        print('\033[0;32m-=\033[m' * 15)
        print('\033[0;33m*\033[m-' * 50)
        print(f'Esses são os números já sorteados: ', end='')
        for n in numero:
            print(f'\033[1;36m{n}\033[m - ', end='')
        print()
        print('\033[0;33m*\033[m-' * 50)
        continuar = str(input('Deseja continuar? \033[1;31m[S/N]\033[m ')).upper().strip()[0]
        if continuar in 'N':
            print('\033[1;36mBINGO!\033[m')
            break
