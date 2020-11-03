jogador = dict()
partidas = list()
equipe = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range (0, tot):
        partidas.append(int(input(f'Quantos gols o {jogador["nome"]} fez na {c+1}ª partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total gols'] = sum(partidas)
    equipe.append(jogador.copy())
    while True:
        d = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if d in 'SN':
            break
        print('Erro, responda S ou N:')
    if d == 'N':
        break
print('-=-'*20)
for k,v in enumerate(equipe):
    print(f'{k + 1:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-=-'*20)
while True:
    busca = int(input(f'Mostrar dados de qual jogador? (0 para nenhum): '))
    indice = busca - 1
    if busca == 0:
        print('Até logo!')
        break
    if indice >= len(equipe):
        print(f'Erro! Não existe jogador com codigo {busca}.')
    else:
        print(f'Levantamento do jogador {equipe[indice]["nome"]}: ')
        for i, g in enumerate(equipe[indice]['gols']):
            print(f'    No {i + 1}° jogo fez {g} gols.')
    print('-'*50)
print('Obrigado por Utilizar')

'''for k, v in jogador.items():
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
    print(f'O jogador {jogador["nome"]} fez {jogador["total gols"]} go')
else:
    print(f'Totalizando {jogador["total gols"]} gols')'''
