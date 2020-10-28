preco = float(input('Preço do produto: R$'))
desc = float(input('% de desconto: '))
np = preco - (preco * desc / 100)
print('O preço após o desconto é de R${:.2f}'.format(np))
