'''ano = int(input('Digite o ano: '))
ano1 = ano % 4

if ano1 == 0:
    ano %= 100
    if ano != 0:
        print('Esse ano é bissexto!')
    elif ano == 0:
        print('Esse ano é bissexto!')
elif ano1 != 0:
    ano %= 400
    if ano1 == 0:
        print('Esse ano é bissexto!')
    else:
        print('Esse ano não é bissexto')'''

from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: ' ))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é Bissexto!'.format(ano))







