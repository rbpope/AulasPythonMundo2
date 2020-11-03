jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
for c in range (0, tot):
    partidas.append(int(input(f'Quantos gols o {jogador["nome"]} fez na {c+1}ª partida: ')))
jogador['gols'] = partidas[:]
jogador['total gols'] = sum(partidas)
print('-=-'*20)
print(jogador)
print('-=-'*20)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=-'*20)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas.')
for i, v in enumerate(jogador['gols']):
    if v == 0:
        print(f'   => Na {i + 1}ª partida não fez gol.')
    elif v == 1:
        print(f'   => Na {i + 1}ª partida fez {v} gol.')
    else:
        print(f'   => Na {i +1}ª partida fez {v} gols')
if jogador['total gols'] == 0:
    print(f'O {jogador["nome"]} nunca fez gol!')
elif jogador['total gols'] == 1:
    print(f'O jogador {jogador["nome"]} fez {jogador["total gols"]} gol')
else:
    print(f'Totalizando {jogador["total gols"]} gols')
