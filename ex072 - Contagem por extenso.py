numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte')
valor = int(input('Digite um valor entre 0 e 20: '))
while True:
    if valor < 0 or valor > 20:
        valor = int(input('Tente novamente. Digite um valor entre 0 e 20: '))
    else:
        print(f'Você digitou o número {numeros[valor]}!')
        break

