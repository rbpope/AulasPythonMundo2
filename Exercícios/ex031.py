d = int(input('Qual a distância da sua viagem? '))
if d <= 200:
    v = float(0.5)
if d > 200:
    v = float(0.45)
p = v * d
print('O valor da sua viagem será de R${:.2f}.'.format(p))
