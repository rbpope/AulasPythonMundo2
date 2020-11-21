def aumentar(v=0, t=0):
    p = v + (v * t / 100)
    return p


def diminuir(v=0, t=0):
    p = v - (v * t / 100)
    return p


def dobro(v=0):
    p = v * 2
    return p


def metade(v=0):
    p = v / 2
    return p


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')
