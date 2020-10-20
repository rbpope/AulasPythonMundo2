cont = 0

a = int(input('Primeiro termo da PA: '))
b = int(input('Razão da PA: '))
decimo = a + (10-1) * b
for c in range(a, decimo + b, b):
    print(c, end=' ')
print('ACABOU')