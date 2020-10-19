p = float(input('Informe o preço do item: R$'))
cond = int(input('''Escolha a modalidade de pagamento:
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2X no cartão
[4] 3x ou mais no cartão
Qual é a sua opção: '''))
if cond == 1:
    pf = p - (p*10/100)
    print('O preço à vista em dinheiro ou cheque tem 10% de desconto e fica em R${:.2f}.'.format(pf))
elif cond == 2:
    pf = p-(p*5/100)
    print('O valor à vista no cartão tem 5% de desconto e fica em R${:.2f}.'.format(pf))
elif cond == 3:
    parcelas = p / 2
    print('O preço final será de R${:.2f} em até 2x de R${:.2f}.'.format(p, parcelas))
elif cond == 4:
    pf = p + (p*20/100)
    parcelas = pf/3
    print('O preço final será de R${:.2f} em, no mínimo, 3X de R${:.2f}, com 20% de juros.'.format(pf, parcelas))
else:
    print('Essa opção não é válida.')
