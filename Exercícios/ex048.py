soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        cont = cont + 1
print('A soma de todos os números divisíveis por 3 entre 1 e 500 é {}.'.format(soma))
print('Existem {} números divisíveis por 3 entre 1 e 500.'.format(cont))
