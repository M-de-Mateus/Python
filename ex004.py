x = input('Digite algo: ')
print('O tipo primitivo desse valor é {} \n'
      'Só tem espaço? {} \n'
      'É um número? {} \n'
      'É alfabético? {} \n'
      'É alfanumérico? {} \n'
      'Está em maiúsculo? {} \n'
      'Está em minúsculas? {} \n'
      'Está capitalizada? {} \n'
      .format(type(x), x.isspace(), x.isnumeric(), x.isalpha(), x.isalnum(), x.isupper(), x.islower(), x.istitle()))

