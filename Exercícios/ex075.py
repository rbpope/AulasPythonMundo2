
num = (int(input('Escolha um número: ')),
      int(input('Digite outro valor: ')),
      int(input('Digite o terceiro valor: ')),
      int(input('Digite o último valor: ')))

print(num)
print(f'Temos {num.count(9)} número 9.')
if 3 in num:
    print(f'A posição do primeiro número 3 é {num.index(3)+1}.')
else:
    print('O número 3 não foi digitado.')
print(f'Os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
