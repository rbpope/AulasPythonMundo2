cores = {'inv':'\033[7m',
        'limpa':'\033[m'}
print('==='*8)
print('{}ANALISADOR DE TRIANGULO{}'.format(cores['inv'], cores['limpa']))
print('==='*8)
x = float(input('Digite o primeiro lado do triangulo: '))
y = float(input('Digite o segundo lado do triangulo: '))
z = float(input('Digite o terceiro lado do triangulo: '))
if x >= y + z or y >= z + x or z >= x + y:
    print('Essas medidas \033[1;31mnão\033[m formam um triangulo!')
else:
    print('As medidas dadas formam um triangulo.')
if x == y and x == z:
    print('É um triangulo equilatero.')
if x == y or x == z or y == z:
    print('É um triangulo isosceles.')
    