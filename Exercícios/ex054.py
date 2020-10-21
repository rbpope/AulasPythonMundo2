from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    nasc = int(input('Qual o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Neste grupo temos {} menores de idade e {} maiores de idade'.format(totalmenor, totalmaior))
