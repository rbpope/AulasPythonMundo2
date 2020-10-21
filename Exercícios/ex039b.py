from datetime import date

atual = date.today().year
print('''Qual o seu gênero:
[1] Masculino
[2] Feminino
''')
gen = int(input('Qual a sua opção: '))
if gen == 2:
    print('Você não precisa se alistar.')
elif gen == 1:
    nasc = int(input('Qual o seu ano de nascimento? '))
    idade = atual - nasc
    if idade == 18:
        print('Você á tem 18 anos e precisa se alistar IMEDIATAMENTE.')
    elif idade < 18:
        saldo = 18 - idade
        alistamento = atual + saldo
        print('Você tem {} anos e ainda não precisa se alistar'.format(idade))
        print('Seu alistamento será no ano de {}'.format(alistamento))
    elif idade > 18:
        saldo = idade - 18
        alistamento = atual - saldo
        print('Voce tem {} anos, deveria ter se alistado há {} anos.'.format(idade, saldo))
        print('Seu alistamento foi em {}'.format(alistamento))
else:
    print('Essa merda de ideologia de gênero não existe para o exército.')
