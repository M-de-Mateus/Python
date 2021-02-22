import random

lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)
jogador = str(input('Escolha entre pedra, papel ou tesoura: ')).lower()


if jogador == computador:
    print('O jogador escolheu {} e o computador escolheu {} por isso deu empate!'.format(jogador, computador))
elif jogador == 'pedra' and computador == 'tesoura':
    print('O jogador escolheu {} e o computador escolheu {} por isso o jogador ganhou!'.format(jogador, computador))
elif jogador == 'tesoura' and computador == 'papel':
    print('O jogador escolheu {} e o computador escolheu {} por isso o jogador ganhou!'.format(jogador, computador))
elif jogador == 'papel' and computador == 'pedra':
    print('O jogador escolheu {} e o computador escolheu {} por isso o jogador ganhou!'.format(jogador, computador))
elif jogador == computador:
    print('O jogador escolheu {} e o computador escolheu {} por isso deu empate!'.format(jogador, computador))
elif jogador != lista:
    print('Jogada inválida!')
else:
    print('O jogador escolheu {} e o computador escolheu {} por isso o jogador perdeu!'.format(jogador, computador))
