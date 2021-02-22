def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('ERRO! Digite um número inteiro válido!')
            continue
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar esse número!')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('ERRO! Digite um número inteiro válido!')
            continue
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar esse número!')
            return 0
        else:
            return n


num = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um numero real: ')
print(f'Você digitou o número inteiro {num} e o número real {num2}!')
