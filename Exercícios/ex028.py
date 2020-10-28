from random import randint
from time import sleep
cores = {'limpa':'\033[m',
         'roxo':'\033[1;35m',
         'titulo':'\033[7;30m',
         'verm':'\033[1;31m'}
nc = randint(0,5) #Variável que o computador escolhe
print('-=-'*20)
print('{}Vou escolher um número entre 0 e 5, tente adivinhar!!!{}'.format(cores['titulo'], cores['limpa']))
print('-=-'*20)
n = int(input('Digite um número de 0 a 5: ')) #Escolha do jogador
print('{}(o){}'.format(cores['verm'], cores['limpa']))
sleep(2)
if nc == n :
    print('Parabéns, você acertou!') 
else:
    print('O escolhido foi {}! Eu ganhei!'.format(nc))
