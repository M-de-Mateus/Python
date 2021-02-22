sexo = idade = maior18 = homens = menor20 = continuar = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: '))

    if idade > 18:
        maior18 += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff':
        if idade < 20:
            menor20 += 1
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
print(f'''Foram cadastradas {maior18} pessoa(s) maior(es) de 18!
Foram cadastrados {homens} homem(ns)!
Foram cadastradas {menor20} mulheres menores de 20!''')
