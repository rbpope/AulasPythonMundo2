from random import randint
print('-=-'*10)
print('PAR OU IMPAR')
print('-=-'*10)
cont = 0
while True:
    cp = randint (0, 5)
    jg = int(input('escolha um número: '))
    total = cp + jg
    esc = ' '
    while esc not in 'PI':
        esc = str(input('PAR OU IMPAR: ')).strip().upper()[0]
    print('-' * 15)
    if esc in 'P' and total % 2 == 0:
        print(f'Eu esgolhi {cp} e você escolheu {jg} o resultado {total} foi par')
        print('Jogador venceu:')
    elif esc in 'P' and total != 0:
        break
    elif esc in 'I' and total % 2 != 0:
        print(f'Eu esgolhi {cp} e você escolheu {jg} o resultado {total} foi impar')
        print('Jogador venceu:')
    elif esc in 'I' and total % 2 == 0:
        break
    cont += 1
    print('-' * 15)
print(f'Eu esgolhi {cp} e você escolheu {jg} o resultado {total}')
print('COMPUTADOR VENCEU!')
if cont == 0:
    print('Você nunca me venceu!')
else:
    print(f'Você venceu {cont} vezes consecutivas.')

