distancia = int(input('Digite a distancia da viagem em km: '))

if distancia <= 200:
    valor = float(distancia * 0.50)
    print('Sua viagem custará R$ {:.2f}.'.format(valor))
else:
    valor = float(distancia * 0.45)
    print('Sua viagem custará R$ {:.2f}.'.format(valor))
