import math

co = float(input('Qual é o cateto oposto? '))
ca = float(input('Qual é o cateto adjacente? '))
hipotenusa = ((co ** 2 + ca ** 2)**(1/2))
hi = math.hypot(co, ca)
print('A hipotenusa vale {:.2f}'.format(hipotenusa))
print('A hipotenusa vale {:.2f}'.format(hi))

