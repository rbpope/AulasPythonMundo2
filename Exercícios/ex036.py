color = {'limpa': '\033[m',
         'invert':'\033[33;44]',
         'verm': '\033[1;31;40'}
v = float(input('Qual é o valor do imóvel? R$'))
s = float(input('Qual o valor do salário do comprador? R$'))
a = int(input('Em quantos anos o comprador deseja pagar? '))
p = v / (a *12)
pm = s *30 / 100
print('O valor da prestação de um imóvel de R${:.2f}, pago em {} anos será de R${:.2f},'.format(v, a, p), end = ' ')
print('para quem ganha um salário mensal de R${:.2f}:'.format(s), end = ' ')
if p <= pm:
    print('O empréstimo está aprovado')
else:
    print('O empréstimo NÃO pode ser aprovado.')
