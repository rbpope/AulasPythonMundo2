cores = {'inv':'\033[7m',
        'limpa':'\033[m',
        'verm':'\033[1;31m'}
print('==='*8)
print('{}ANALISADOR DE TRIANGULO{}'.format(cores['inv'], cores['limpa']))
print('==='*8)
x = float(input('Digite o primeiro lado do triangulo: '))
y = float(input('Digite o segundo lado do triangulo: '))
z = float(input('Digite o terceiro lado do triangulo: '))
if x >= y + z or y >= z + x or z >= x + y:
    print('Essas medidas {}não{} formam um triangulo!'.format(cores('verm'), cores('limpa')))
else:
    print('As medidas dadas formam um triangulo.')
if x == y and x == z:
    print('É um triangulo equilatero.')
elif x != z and x != y and z != y:
    print('É um triangulo escaleno.')
elif x == y or x == z or y == z:
    print('É um triangulo isosceles.')