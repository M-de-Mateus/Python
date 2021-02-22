metros = float(input("Digite a quantidade de metros quadrados a serem pintados: "))
litros = metros / 3

if metros % 54 == 0:
    latas = metros / 54
else:
   if metros / 54 + 1 > 4.5:
    latas = round(float(metros / 54)) + 1
   else:
      latas = int(metros / 54) + 1

preco_latas = latas * 80
print('Total de lata(s): {}. Valor R${:.2f}'.format(latas, preco_latas))

if metros % 10.8 == 0:
   galoes = metros / 10.8
else:
   if metros / 10.8 + 1 >= 18.5:
      galoes = round(float(metros / 10.8)) + 2
   elif metros / 10.8 > 1 < 18.5:
      galoes = round(float(metros / 10.8)) + 1
   else:
      galoes = int(metros / 10.8) + 1

preco_galoes = galoes * 25

print('Total de galão(ões): {}. Valor R${:.2f}'.format(galoes, preco_galoes))


if metros >= 200:
   latas = int(((metros * 10 / 100) + metros) / 54)
   galoes = round((((metros * 10 / 100) + metros) % 54) / 10.8) + 1

elif metros % 54 == metros:
   galoes = round((metros / 54) + 1)
   latas = 0

else:
   latas = metros // 54
   galoes = round(float((metros % 54) / 10.8) + 1)



preco_comb_latas = latas * 80
preco_comb_galoes = galoes * 25

precofinal = preco_comb_latas + preco_comb_galoes

print('{} lata(s) e {} galão(ões) custam R${:.2f}'.format(int(latas), galoes, precofinal))
