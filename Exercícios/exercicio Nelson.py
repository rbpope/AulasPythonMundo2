s = []
i = 1
soma = 0
while i <= 10000000:
    termo = 1/i
    soma += termo
    s.append(termo)
    i += 1
print(f'A soma dos números é {soma}')
print(f'A soma é {sum(s):.2f}')
print(f'Os últimos números são {s[-4:-1]}')