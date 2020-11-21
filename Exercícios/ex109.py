import moeda
valor = float(input('Digite um valor: R$'))
taxa = float(input('Taxa:'))
print(f'A metade de {moeda.moeda(valor)} é {(moeda.metade(valor, True))}')
print(f'O Dobro de {moeda.moeda(valor)} é {(moeda.dobro(valor, True))}.')
print(f'Tirando {taxa}% de {moeda.moeda(valor)} temos {moeda.diminuir(valor, taxa, True)}.')
print(f'Adicionando {taxa}% ao preço de {moeda.moeda(valor)}'
      f' temos {moeda.aumentar(valor, taxa, True)}')


