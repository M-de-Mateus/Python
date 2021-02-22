n = c = 0
while True:
    n = int(input('Digite o número do qual deseja ver a tabuada: '))
    if n < 0:
        print('O programa foi encerrado!')
        break
    else:
        while c < 11:
            print(f'{n} x {c:2} = {n * c}')
            c += 1
    c = 0
