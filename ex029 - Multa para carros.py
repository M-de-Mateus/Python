vel = int(input('Escreva a velocidade do carro: '))

if vel > 80:
    print('Você foi multado!')
    multa = float((vel - 80) * 7)
    print('O valor da multa é de R$ {:.2f}.'.format(multa))
else:
    print('Você está dentro da velocidade permitida!')

