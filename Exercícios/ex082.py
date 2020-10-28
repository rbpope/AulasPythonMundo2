lista = []
listap = []
listai = []
while True:
    n = int(input('Digite um número : '))
    lista.append(n)
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)
    d = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if d not in 'SN':
        d = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if d == 'N':
        break
print('-*-'*20)
print(f'A lista construida foi: {lista}.')
print(f'Os números pares inseridos na lista foram: {listap}.')
print(f'Os números ímpares inseridos foram: {listai}.')
