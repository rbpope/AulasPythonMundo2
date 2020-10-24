ch = cm = cmj = 0
while True:
    id = int(input('Idade '))
    opcao = gen = ' '
    while gen not in 'MF':
        gen = str(input('[M/F] ')).strip().upper()[0]
    if gen == 'M':
        ch += 1
    if id >= 18:
        cm += 1
    if gen == 'F' and id < 20:
        cmj += 1
    while opcao not in 'SN':
        opcao = str(input('Deseja cadastrar mais uma opção: [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break
print('Cadastros encerrados,', end=' ')
print(f'foram um total de {ch} homens, {cm} de maiores de 18 anos e {cmj} mulheres com menos de 20 anos.')
