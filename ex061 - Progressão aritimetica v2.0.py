primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
c = 1
while c <= 10:
    print(f'{termo} - ', end='')
    termo += razao
    c += 1
print('Fim')

