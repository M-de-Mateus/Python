primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo} - ', end='')
        termo += razao
        c += 1
    print('Pausa')
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f'Progressão finalizada com {total} termos exibidos!')
