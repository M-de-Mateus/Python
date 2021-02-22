num = float(input('Digite a largura da parede: '))
num2 = float(input('Digite a altura da parede: '))
area = num*num2
tinta = area/2
print('A area da parede é de {}m² e serão necessarias {:.2f}l de tinta para pinta-la.'.format(area, tinta))
