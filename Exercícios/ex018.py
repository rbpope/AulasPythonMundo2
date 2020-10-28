from math import sin, cos, tan, radians

an = float(input('Qual é o angulo? '))
a = radians(an)
seno = sin(a)
coseno = cos(a)
tangente = tan(a)
print('O seno de {} é {:.2f}\nO coseno de {} é {:.2f}\nA tangente de {} é {:.2f}'.format(an, seno, an, coseno, an, tangente))
