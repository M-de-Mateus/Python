n = int(input('Digite o número do qual deseja ver a tabuada: '))
print('Essa é a tabuada do número {}: '.format(n))
for c in range(0, 11):
    print('{} X {:2} = {}'.format(n, c, c * n))

