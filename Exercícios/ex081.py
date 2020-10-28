lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    d = str(input('Deseja adicionar outro valor? [S/N] ')).strip().upper()[0]
    while d not in 'SN':
        d = str(input('Deseja adicionar outro valor? [S/N] ')).strip().upper()[0]
    if d == 'N':
        break

print('-=-'*20)
print(f'A lista digitada é {lista}.')
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista.')
