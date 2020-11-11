def ficha(jog='<desconhecido>', gols=0):
    print(f'O jogador {jog} fez {gols} gols no campeonato.')


j = str(input('Qual o nome do jogador? ')).capitalize()
g = str(input('Quantos gols ele fez no campeonato? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)
