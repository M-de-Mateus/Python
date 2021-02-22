lista = []

while True:
    valores = int(input('Digite um valor: '))
    lista.append(valores)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
print(f'Foram digitados {len(lista)} números!')
print(f'Lista ordenada de forma decrescente: {sorted(lista, reverse= True)}')
if 5 in lista:
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 não foi digitado!')
