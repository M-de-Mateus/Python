def notas(*n, sit=False):
    '''
    -> Função para calcular a média de um aluno e sua situação
    :param n: Notas do aluno
    :param sit: Mostra a situação de acordo com a média
    :return: Retorna um dicionário com varias informações do aluno
    '''
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.4, 3.1, 4, 7, sit=True)
print(resp)