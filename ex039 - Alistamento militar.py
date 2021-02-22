import datetime

data = datetime.date.today()
ano = int(data.year)

nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano - nascimento

if idade < 18:
    alistamento = 18 - idade
    print('Você ainda não atingiu a idade de alistamento faltam {} ano(s)!'.format(alistamento))
elif idade == 18:
    print('Está na hora de se alistar, compareça a junta militar de sua cidade!')
else:
    alistamento = idade - 18
    print('Você está atrasado! Já passou {} ano(s) da data do alistamento, vá até a junta militar de sua cidade!'.format(alistamento))





