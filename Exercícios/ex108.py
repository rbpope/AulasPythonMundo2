import moeda
valor = float(input('Digite um valor: R$'))
taxa = float(input('Taxa:'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O Dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}.')
print(f'Tirando {taxa}% de {moeda.moeda(valor)} temos {moeda.moeda(moeda.diminuir(valor, taxa))}.')
print(f'Adicionando {taxa}% ao preço de {moeda.moeda(valor)}'
      f' temos {moeda.moeda(moeda.aumentar(valor, taxa))}')
