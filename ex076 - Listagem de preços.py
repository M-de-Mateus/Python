listagem = ('Lápis', 1, 'Caderno', 15, 'Borracha', 0.50, 'Livro', 25, 'Caneta', 2.50, 'Estojo', 5, 'Lapiseira', 4)

a = 0
b = 1
print('-' * 50)
print(f'{"LISTAGEM DE PREÇO":^50}')
print('-' * 50)
for c in listagem:
    while b < len(listagem):
        print(f'{listagem[a]:.<40}{"R$"} {float(listagem[b]):5.2f}')
        a += 2
        b += 2
print('-' * 50)