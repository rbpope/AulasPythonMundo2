classificacao = ('Internacional', 'Flamengo', 'Atlético - MG', 'Fluminense',
                 'São Paulo', 'Santos', 'Palmeiras', 'Fortaleza', 'Grêmio',
                 'Ceará', 'Atlético - GO', 'Sport', 'Corinthians', 'Bahia',
                 'RB Bragantino', 'Botafogo', 'Vasco', 'Athletico', 'Coritiba', 'Goias')
print('-------'*20)
print(f'Os times do Brasileirão 2020 são {sorted(classificacao)}', end= ' ')
print('-------'*20)
print(f'Os cinco primeiros colocados no Brasileirão 2020 são {(classificacao[:5])}')
print('-------'*20)
print(f'Os times em ordem alfabética são {classificacao[-4:]}')
print('-------'*20)
print(f'A posição do Coritiba é o {classificacao.index("Coritiba")+1}º lugar.')
print('-------'*20)
