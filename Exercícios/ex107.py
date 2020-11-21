import moeda
valor = float(input('Digite um valor: R$'))
taxa = float(input('Desconto:'))
print(f'A metade de R${valor:.2f} é R${moeda.metade(valor):.2f}')
print(f'O Dobro de R${valor:.2f} é R${moeda.dobro(valor):.2f}.')
print(f'Tirando {taxa}% de R${valor:.2f} temos R${moeda.diminuir(valor, taxa):.2f}.')
