total = mil = menor = c = barato = 0
while True:
    produto = str(input('Nome do produo: '))
    preco = float(input('Preço: R$'))
    c += 1
    total += preco
    if preco > 1000:
        mil += 1
    if c == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break
    print(f'O total da compra foi de R${total:.2f}')
    print(f'{mil} Um produto custou mais de R$ 1.000,00')
    print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
