from random import randint
from time import sleep

numeros = list()


def sorteia(lista):
    print('Sorteando os números: ', end=' ', flush=True)
    sleep(0.3)
    for cont in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end=' ', flush=True)
        sleep(0.3)
    print('FIM')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista} temos {soma}.')


sorteia(numeros)
somaPar(numeros)
