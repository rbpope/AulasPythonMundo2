listnum =[]
while True:
    n = int(input('Digite um valor: '))
    if n not in listnum:
        listnum.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Número já foi digitado, Não foi adicionado.')
    d = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if d not in 'SN':
        d = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if d in 'N':
        break
print('-=-'*10)
listnum.sort()
print(f'Você digitou {listnum}.')
