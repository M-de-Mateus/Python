print('=' * 45)
print('Programa para aprovar crédito imobiliário')
print('=' * 45)
casa = float(input('Qual o valor da casa que deseja comprar? '))
salario = float(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos deseja pagar? '))

prestacao = casa / (anos * 12)

if prestacao > (salario * 30) / 100:
    print('Infelizmente seu emprestimo foi negado!')
else:
    print('O emprestimo de R${:.2f} foi aprovado!'.format(casa))
    print('Será pago em {} ano(s) com a prestação mensal no valor de R${:.2f}!'.format(anos, prestacao))
