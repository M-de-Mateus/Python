tabela = ('São Paulo', 'Atlético-MG', 'Flamengo', 'Internacional', 'Grêmio', 'Palmeiras', 'Chapecoense',
          'Santos', 'Corinthians', 'Ceará SC', 'Athletico-PR', 'Atlético-GO',
          'Bragantino', 'Fortaleza', 'Sport Recife', 'Bahia', 'Vasco da Gama',
          'Goias', 'Botafogo', 'Coritiba')
print(f'Os 5 primeiros colocados são {tabela[0:5]}')
print('-=' * 30)
print(f'Os 4 últimos colocados são {tabela[-4:]}')
print('-=' * 30)
print(f'Ordem alfabética {sorted(tabela)}')
print('-=' * 30)
print(f'O time da Chapecoense encontra-se na {tabela.index("Chapecoense") + 1}ª posição!')
