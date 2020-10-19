from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha uma das a seguir:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Escolha a sua opção: '))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô!!!')
print('-=-'*12)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}.'.format(itens[jogador]))
print('-=-'*12)
if computador == 0:
    if jogador == 0:
        print('JOGADA EMPATADA.')
    elif jogador == 1:
        print('JOGADOR VENCEU.')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU.')
    elif jogador == 1:
        print('JOGADA EMPATADA.')
    elif jogador == 2:
        print('JOGADOR VENCEU.')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU.')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('JOGADA EMPATADA.')
    else:
        print('JOGADA INVÁLIDA!')
