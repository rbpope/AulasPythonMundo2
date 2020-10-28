real = float(input('informe quantos R$: '))
dolar = float(input('Informe o valor do Dólar: '))
conv = real / dolar
print('Você tem R${:.2f}, que equivale a US${:.2f}.'.format(real, conv))
