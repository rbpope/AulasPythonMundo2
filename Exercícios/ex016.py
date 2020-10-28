from math import trunc

nr = float(input('Digite um número aleatório: '))
print('A porção inteira de {} é {}.'.format(nr, trunc(nr)))
print('A porção inteira de {} é {:.0f}.'.format(nr, int(nr)))
