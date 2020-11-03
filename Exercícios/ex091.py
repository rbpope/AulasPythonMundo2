from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1' : randint(1, 6),
        'jogador2' : randint(1, 6),
        'jogador3' : randint(1, 6),
        'jogador4' : randint(1, 6)}
print('*'*30)
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} jogou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=-'*10)
for i, v in enumerate(ranking):
    print(f'O {i + 1}º lugar foi o {v[0]} jogando {v[1]} no dado.')
    sleep(1)
