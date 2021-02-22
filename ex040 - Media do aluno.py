print('=' * 25)
print('Calculo de média do aluno')
print('=' * 25)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = nota1 + nota2 / 2

if media < 5:
    print('O aluno foi REPROVADO!')
elif media >= 5 or media <= 6.9:
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('O aluno foi APROVADO!')
