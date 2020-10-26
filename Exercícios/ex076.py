itens = ('Lápis', 2.00,
         'Borracha', 1.75,
         'Caneta', 2.50,
         'Caderno', 15.00,
         'Livro', 55.00,
         'Fichário', 25.00,
         'Papel c/ 100', 30.00,
         'Ramo Almaço', 5.00,
         'Mochila', 120.00
         )
print('-'*40)
print(f'{"Lista de Preços":^40}')
print('-'*40)
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}', end=" ")
    if pos % 2 == 1:
        print(f'R${itens[pos]:>5.2f}')
print('-'*40)
