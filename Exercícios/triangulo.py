x = int(input('Digite o primeiro lado do triangulo: '))
y = int(input('Digite o segundo lado do triangulo: '))
z = int(input('Digite o terceiro lado do triangulo: '))
if x >= y + z or y >= z + x or z >= x + y:
    print('Não é um triangulo!')
else:
    print('É um triangulo.')
if x == y and x == z:
    print('É um triangulo equilatero.')
if x == y or x == z or y == z:
    print('É um triangulo isosceles.')
