valores = []
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('O valor está duplicado, não irei adicionar!')
    else:
        valores.append(num)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        print(f'Esses foram os números digitados: {sorted(valores)}')
        break
