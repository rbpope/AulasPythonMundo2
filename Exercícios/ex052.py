num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[7;31m{}\033[m '.format(c), end=' ')
        tot += 1
    else:
        print('{}'.format(c), end=' ')
print('\nO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso ele é um número primo.')
else:
    print('E por isso ele não é um número primo.')
