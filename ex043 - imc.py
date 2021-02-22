print('*' * 20)
print('Calculo de IMC')
print('*' * 20)

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30 <= imc < 40:
    print('Obesidade!')
else:
    print('Obesidade morbida!')
print('Seu imc é de {:.1f}!'.format(imc))