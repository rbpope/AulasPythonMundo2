from time import sleep


def contador(i, f, p):
    print('-*' * 20)
    print(f'Contagem de {i} a {f} de {p} em {p}.')
    sleep(1)
    if i < f:
        c = i
        while c <= f:
            print(f'{c} ', end=' ')
            sleep(0.5)
            c += p
        print('FIM')
    else:
        c = i
        while c >= f:
            print(f'{c} ', end=' ')
            sleep(0.5)
            c -= p
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('=*=' * 15)
print('Agora digite a sua contagem:')
ini = int(input('Início: '))
fim = int(input('Fim:   '))
passo = int(input('Passo:   '))
contador(ini, fim, passo)
