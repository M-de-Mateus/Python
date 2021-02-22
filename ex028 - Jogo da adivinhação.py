from random import randint
n = randint(0, 5)
print('Jogo para adivinhar qual número o computador está pensando!')
resp = int(input('Em qual número entre 0 e 5 o computador está pensando agora? '))

if resp == n:
    print('Parabéns! Você acertou!')
else:
    print('Você perdeu!')
