from random import randint
computador = randint(0,10)
print('Acabei de pensar em um número entre 0 e 10, tente advinhar.')
acertou = bool(False)
tentativas = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    tentativas +=1
    if jogador == computador:
        acertou = bool(True)
    else:
        if jogador < computador:
                    print('O número é maior que isso.')
        elif jogador > computador:
                    print('O número é menor do que isso')
print('Parabéns, você acertou em {} tentativas.'.format(tentativas))
