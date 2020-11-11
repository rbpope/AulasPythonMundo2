def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >=7.0:
            r['situação'] = 'BOA'
        elif r['media'] >= 5.0:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'

    return r


resp = notas(5.5, 2.5, 9, 8, sit=True)
print(resp)
