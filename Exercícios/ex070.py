print('-=-'*4)
print('Lojas Pope')
print('-=-'*4)
total = acima = barato = cont = 0
pmb = ' '
while True:
    produto = str(input('Qual o produto: ')).strip()
    preco = float(input('Digite o valor do produto: R$'))
    total += preco
    opcao = ' '
    cont += 1
    if preco > 1000:
        acima += 1
    if cont == 1 or preco < barato:
        barato = preco
        pmb = produto
    while opcao not in 'SN':
        opcao = str(input('Deseja adicionar mais um iten: [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-'*20)
print('Compra encerrada')
print(f'O total foi de R${total:.2f}.')
print(f'O item mais barato foi {pmb} e custou R${barato:.2f}.')
print(f'{acima} itens custaram mais que R$1000.00.')
