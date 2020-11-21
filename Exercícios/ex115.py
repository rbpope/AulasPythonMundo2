from ex115.lib.interface import *
from ex115.lib.arquivo import*
from time import sleep
a = 'pope.txt'
if not arquivoexiste(a):
    criararquivo(a)
while True:
    resposta = menu(['Ver Cadastro', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Ver Cadastro')
        lerarquivo(a)
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Terminando o sistema.')
        break
    else:
        print('Favor digitar uma opção válida.')
    sleep(2)

