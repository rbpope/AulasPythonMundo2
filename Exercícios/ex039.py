from datetime import date
atual = date.today().year
ano_nasc = int(input('Qual o ano do seu nascimento: '))
idade = atual-ano_nasc
print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {atual}')   #format(ano_nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE.')
elif idade < 18:
    saldo = 18 - idade
    alistamento = atual + saldo
    print(f'Ainda faltam {saldo} anos para o seu alistamento')
    print(f'O seu alistamento será em {alistamento}.')
elif idade > 18:
    saldo = int(idade - 18)
    alistamento = int(atual - saldo)
    print(f'Você deveria ter se alistados há {saldo} anos.')
    print(f'Seu alistamento foi em {alistamento}.')
