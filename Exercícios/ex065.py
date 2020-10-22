d = 'Y'
soma = media = c = 0
while d == 'Y':
    n = int(input('Digite um número: '))
    soma += n
    c += 1
    d = str(input('Deseja continuar: [Y/N]: ')).strip().upper()[0]
    media = soma / c
    if c == 1:
        maior = menor = n
    if n > maior:
        maior = n

print('Você digitou {} números e  média dos valores digitados foi {}.'.format(c, media))
