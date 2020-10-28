import random

n1 = 'Eduardo Pope'
n2 = 'Arthur Pope'
n3 = 'Giorgia Pope'
n4 = 'Leonora Pope'
n5 = 'Renato Pope'
n6 = 'Nahor Neto'
n7 = 'Nica Malandra Ladra de Sopa'
lista = [n1, n2, n3, n4, n5, n6, n7]
escolhido = random.choice(lista)
print('O impostor é {}'.format(escolhido))
