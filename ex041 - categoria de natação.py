from _datetime import datetime

data = datetime.today()
ano = data.year

idade = int(input('Digite o ano de nascimento do atleta: '))
idade = ano - idade

if idade <= 9:
    print('MIRIM!')
elif idade <= 14:
    print('INFANTIL!')
elif idade <= 19:
    print('JUNIOR!')
elif idade <= 20:
    print('SÊNIOR!')
else:
    print('MASTER!')
