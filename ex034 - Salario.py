salario = float(input('Digite o salario: '))

if salario >= 1250:
    aumento = (salario * 10)/100 + salario
    print('Quem ganhava R$ {:.2f} agora ganha R$ {:.2f}.'.format(salario, aumento))
else:
    aumento = (salario * 15)/100 + salario
    print('Quem ganhava R$ {:.2f} agora ganha R$ {:.2f}.'.format(salario, aumento))
