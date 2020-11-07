def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados foram {f1}, {f2} e {f3}')
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}.')
