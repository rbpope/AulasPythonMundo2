primeiro = int(input('Qual é o primeiro termo? '))
razao = int(input('Qual é a razão da PA? '))
termo = primeiro
total = 0
mais = 10
cont = 1
while mais != 0:
    total += mais
    while cont <= total:
        print('{} '.format(termo), end=' ')  # preciso entender melhor essa construção.
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos números você quer mais? '))
print('FIM, Você visualizou {} termos.'.format(total))
