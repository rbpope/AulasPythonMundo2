a = float(input('Qual a altura da parede? '))
larg = float(input('Qual a largura da parede? '))
s = a * larg
t = s / 2
print('A área da parede é {:.2f} m² e são necessários {:.2f} litros de tinta para pintá-la.'.format(s, t))
