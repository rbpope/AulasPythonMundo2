from datetime import date

atual = date.today().year
nascimento = int(input('Qual o ano de nascimento do atleta? '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
# mirim idade <= 9
# infantil idade > 9 and idade <= 14
# junior idade > 14 and <= 19
# senior idade > 19 and <= 25
# master idade > 25
if idade <= 9:
    print('O atleta é da categoria MIRIM')
elif 9 < idade <= 14:
    print('O atleta é da categoria INFANTIL.')
elif 14 < idade <= 19:
    print('O atleta é da categoria JUNIOR')
elif 19 < idade <= 25:
    print('O atleta é da categoria SENIOR')
elif idade > 25:
    print('O atleta é da categoria MASTER.')
