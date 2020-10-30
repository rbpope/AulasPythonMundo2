cadastro = []
maior = men = 0
while True:
    temp = []
    temp.append(str(input('Digite o nome: ').strip().capitalize()))
    temp.append(float(input('Digite o peso: ')))
    if len(cadastro) == 0:
        maior = men = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < men:
            men = temp[1]
    cadastro.append(temp[:])

    d = str(input('Deseja adicionar mais um: [S/N]:')).strip().upper()[0]
    if d not in 'SN':
        d = str(input('Deseja adicionar mais um: [S/N]:')).strip().upper()[0]
    if d == 'N':
        break
print('-=-'*15)
if len(cadastro) == 1:
    print('Foi cadastrada 1 pessoa.')
else:
    print(f'Foram cadastradas {len(cadastro)} pessoas.')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in cadastro:
    if p[1] == maior:
        print(f'{p[0]}, ', end='')
print()
print(f'O menor peso foi {men}Kg. Peso de ', end='')
for p in cadastro:
    if p[1] == men:
        print(f'{p[0]}, ', end='')
