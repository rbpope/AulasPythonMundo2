print('-=-' * 9)
print('A Sequencia de Fibonacci:')
print('-=-' * 9)
n = int(input('Quantos números mais da sequencia de Fibonacci você deseja ver? '))
print('_'*30)
t1 = 0
t2 = 1
t3 = t2 + t1
print('{}, {}, '.format(t1, t2), end=' ')
c = 3
while c <= n:
    t3 = t2 + t1
    print('{}, '.format(t3), end=' ')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
# Fibonacci 0, 1, 1, 2, 3, 5, 8, 13
