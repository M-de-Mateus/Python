n = cont = soma = 0
while True:
    n = int(input('Digite um número inteiro [Digite 999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} números e o valor da soma entre eles é de {soma}!')
