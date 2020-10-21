from random import randint
from time import sleep
cores = {'limpa':'\033[m',
         'roxo':'\033[1;35m',
         'titulo':'\033[7;30m',
         'verm':'\033[1;31m'}
nc = randint(0,10) #Variável que o computador escolhe
cont = 0
print('-=-'*20)
print('{}Vou escolher um número entre 0 e 10, tente adivinhar!!!{}'.format(cores['titulo'], cores['limpa']))
print('-=-'*20)
n = int(input('Digite um número de 0 a 10: ')) #Escolha do jogador
print('{}(o){}'.format(cores['verm'], cores['limpa']))
sleep(2)
while n != nc:
    n = int(input('Não é esse número, tente novamente: '))
    cont +=1
print('Parabéns, você acertou e precisou de {} tentativas!'.format(cont))
'''else:
    print('O escolhido foi {}! Eu ganhei!'.format(nc))'''