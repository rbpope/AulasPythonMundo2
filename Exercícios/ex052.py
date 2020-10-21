num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[7;31m{c}\033[m ', end=' ')
        tot += 1
    else:
        print(f'{c}', end=' ')
print('\nO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso ele é um número primo.')
else:
    print('E por isso ele não é um número primo.')
