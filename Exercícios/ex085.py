lista = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('-=-'*15)
lista[0].sort()
print(f'Os valores pares digitados foram {lista[0]}.')
lista[1].sort()
print(f'Os valores ímpares digitados foram {lista[1]}.')
