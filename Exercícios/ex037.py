num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] para binário
[2] para octal
[3] para hexadecimal''')
o = int(input('sua opção é: '))
if o == 1:
    print('{} convertido para binário é: {}'.format(num, bin(num)[2:]))
elif o == 2:
    print('{} convertido para octal é: {}'.format(num, oct(num)[2:]))
elif o == 3:
    print('{} convertido para hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')
