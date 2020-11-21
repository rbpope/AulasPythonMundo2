def aumentar(v=0, t=0, formato=False):
    """Função que adiciona uma porcetagem (t) em cima de um valor (v)
    e retorna o valor formatado em número corrente."""

    p = v + (v * t / 100)
    return p if formato is False else moeda(p)


def diminuir(v=0, t=0, formato=False):
    """Função que retira uma porcetagem (t) em cima de um valor (v)
        e retorna o valor formatado em número corrente."""
    p = v - (v * t / 100)
    return p if formato is False else moeda(p)


def dobro(v=0, formato=False):
    p = v * 2
    return p if formato is False else moeda(p)


def metade(v=0, format=False):
    p = v / 2
    return p if format is False else moeda(p)


def moeda(v=0, moeda='R$'):
    """Função que formato em número corrente em R$."""
    return f'{moeda}{v:.2f}'.replace('.', ',')


def resumo(v=0, a=0, d=0):
    print('-'*30)
    print('Resumo do Preço'.center(30))
    print('-'*30)
    print(f'Preço analizado: \t{moeda(v)}')
    print(f'Dobro do preço: \t{dobro(v, True)}')
    print(f'Metade do preço: \t{metade(v, True)}')
    print(f'{a}% de aumento: \t{aumentar(v, a, True)}')
    print(f'{d}% de desconto: \t{diminuir(v, d, True)}')
    print('-'*30)

