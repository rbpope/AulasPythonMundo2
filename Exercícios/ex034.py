s = float(input('Qual o valor do salário do funcionário? '))
cap = float(1250.00)
if s > cap:
    a = (s*10/100)
if s <= cap:
    a = (s*15/100)
print('O aumento do funcionário será de R${:.2f} e o novo salário do funcionário será de R${:.2f}.'.format(a, (s+a)))
