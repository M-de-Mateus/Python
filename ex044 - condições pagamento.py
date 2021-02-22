c = -1
while c < 10.000:
    print(f'{" Pagamento e condições ":=^40}')
    preco = float(input('Digite o preço do produto: '))
    condicao = int(input('Escolha a condição de pagamento: \n'
                         '1 - À vista dinheiro ou cheque (10% de desconto) \n'
                         '2 - À vista no cartão (5% de desconto) \n'
                         '3 - Em até 2x no cartão (preço normal) \n'
                         '4 - 3x ou mais no cartão (20% de juros) \n'
                         ' '))
    print('=' * 60)

    if condicao == 1:
        preco = preco - ((preco * 10) / 100)
        print('O preço do produto passa a ser R${:.2f} com o pagamento à vista!'.format(preco))
        c += 1
    elif condicao == 2:
        preco = preco - ((preco * 5) / 100)
        print('O preço do produto passar a ser R${:.2f} com o pagamento à vista no cartão!'.format(preco))
        c += 1
    elif condicao == 3:
        preco = preco / 2
        print('Você pagará 2 parcelas de R${:.2f} sem juros!'.format(preco))
        c += 1
    elif condicao == 4:
        parcelas = int(input('Digite o núemro de parcelas: '))
        if parcelas == 2:
            preco = preco / 2
            print('Você pagará 2 parcelas de R${:.2f} sem juros!'.format(preco))
            c += 1
        else:
            preco = preco + ((preco * 20) / 100)
            total = preco / parcelas
            print('Você pagará {} parcelas de R${:.2f}!'.format(parcelas, total))
            c += 1
    else:
        print('Opção inválida!')
        c += 1
