palavras = ('maca', 'biscoito', 'farofa', 'predio', 'chao', 'giz', 'chuva', 'caminhao')

vogais = 0
c = 0

for c in range(len(palavras)):
    print(f'Na palavra {palavras[vogais].upper()} temos as vogais ', end='')
    for c in palavras[vogais]:
        if c in 'aeiou':
            print(c.upper(), end=' ')
    print('')
    vogais += 1
