p = float(input('Qual o peso em Kg: '))
a = float(input('Qual a altura em m: '))
imc = p /(a)**2
print('O IMC do indivíduo é {:.1f}Kg/m2 e'.format(imc), end=' ')
if imc <= 18.5:
    print('o indivíduo está abaixo do peso.')
elif 18.5 < imc <= 25:
    print('o indivíduo está na faixa de peso ideal.')
elif 25 < imc <= 30:
    print('o indivíduo está com sobrepeso')
elif 30 < imc <= 40:
    print('o indivíduo está obeso.')
elif imc > 40:
    print('o indivíduo está com obesidade mórbida.')
