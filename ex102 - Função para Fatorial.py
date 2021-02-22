def fatorial(n, show = False):
    '''

    :param n: Número qual será calculado o fatorial
    :param show: Mostra a conta feita para calcular o fatorial
    :return: retorna o valor do fatorial
    '''

    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=False))
