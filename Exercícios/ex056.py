somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomehomemvelho = ''
totmulher20 = 0
for p in range(1, 6):
    print('------{}ª pessoa------'.format(p))
    nome = str(input('Qual o primeiro nome da pessoa? ')).strip().capitalize()
    idade = int(input('Qual a idade da pessoa? '))
    gen = str(input('Qual o genero [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and gen in 'Mm':
        nomehomemvelho = nome
        maioridadehomem = idade
    if gen in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomemvelho = nome
    if gen in 'Ff' and idade < 21:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é {}.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomehomemvelho))
print('Temos um total de {} mulheres com menos de 20 anos'.format(totmulher20))
