from datetime import date
atual = date.today().year
ano_nasc = int(input('Qual o ano do seu nascimento: '))
idade = ano_nasc - atual
print('Quem nasceu em {} tem {} anos em {}'.format(ano_nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE.')
elif idade < 18:
    saldo = 18 - idade
    alistamento = atual + saldo
    print('Ainda faltam {} anos para o seu alistamento'.format(saldo))
    print('O seu alistamento será em {}.'.format(alistamento))
elif idade > 18:
    saldo = idade - 18
    alistamento = atual - saldo
    print('Você deveria ter se alistados há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}.'.format(alistamento))
