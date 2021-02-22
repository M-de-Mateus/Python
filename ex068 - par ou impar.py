from random import randint
jogador = computador = vitorias = 0

while True:
    jogador = int(input('Digite um valor entre 0 e 100: '))
    jogador_escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    computador = randint(1, 100)
    soma = jogador + computador
    while jogador_escolha not in 'PI':
        jogador_escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    if soma % 2 == 0:
        if jogador_escolha in 'Pp':
            print(f'Você jogou {jogador} e o computador jogou {computador}. ' 
                  f'A soma desses dois números tem o valor de {soma} e é par!'
                  f' Você venceu! Vamos jogar novamente? ')
            vitorias += 1
        else:
            print(f'Você jogou {jogador} e o computador jogou {computador}. ' 
                  f'A soma desses dois números tem o valor de {soma} e é par!'
                  f' Você perdeu! ')
            break
    elif soma % 2 != 0:
        if jogador_escolha in 'Ii':
            print(f'Você jogou {jogador} e o computador jogou {computador}. '
                  f'A soma desses dois números tem o valor de {soma} e é impar!'
                  f' Você venceu! Vamos jogar novamente? ')
            vitorias += 1
        else:
            print(f'Você jogou {jogador} e o computador jogou {computador}. ' 
                  f'A soma desses dois números tem o valor de {soma} e é impar!'
                  f' Você perdeu! ')
            break

print(f'Fim de jogo! Você venceu {vitorias} vez(es)!')

