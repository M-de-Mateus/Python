dias = int(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Quantos kilometros o carro rodou? '))
total = (dias * 60) + (km * 0.15)
print('Total a pagar é de R${:.2f}!'.format(total))

