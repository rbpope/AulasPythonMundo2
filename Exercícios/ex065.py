d = 'Y'
soma = media = c = maior = menor = 0
while d == 'Y':
    n = int(input('Digite um número: '))
    soma += n
    c += 1
    d = str(input('Deseja continuar: [Y/N]: ')).strip().upper()[0]
    media = soma / c
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números e  média dos valores digitados foi {}.'.format(c, media))
print('O maior valor digitado foi {} e o menor foi {}.'.format(maior, menor))
