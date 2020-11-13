from time import sleep
c = ('\033[m',                      #0 - sem cor
     '\033[0;30;41m',               #1 - Vermelho
     '\033[0;30;42m',               #2 - Verde
    '\033[0;30;43m',                #3 - Amarelo
     '\033[0;30;44m',               #4 - Azul
     '\033[0;30;45m',               #5 - lilas
     '\033[0;30;46m',               #6 - Ciano
     '\033[0;30;47m',               #7 - Cinza
     '\033[7;30m'                   #8 - Branco
     )


def titulo(msg, cor=0) -> object:
    tam = len(msg) + 4
    print(c[cor], end='')
    print('˜' * tam)
    print(f'  {msg}')
    print('˜' * tam)
    print(c[0], end='')
    sleep(1)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


comando = ''
while True:
    titulo('Sistema de Ajuda', 2)
    print(c[8], end='')
    comando = str(input('Função ou Biblioteca -> '))
    print(c[0], end='')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)
