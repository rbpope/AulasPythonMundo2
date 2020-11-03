cadastro = dict()
lista = list()
soma = media = 0
while True:
    cadastro['nome'] = str(input('Nome: ')).strip().capitalize()
    cadastro['gen'] = str(input('Gênero: ')).strip().upper()[0]
    while cadastro['gen'] not in 'MF':
        print('Opção inválida.')
        cadastro['gen'] = str(input('Gênero: ')).strip().upper()[0]
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    lista.append(cadastro.copy())
    d = str(input('Deseja cadastrar outra pessoa? [S/N] ')).strip().upper()[0]
    while d not in 'SN':
        print('Opção inválida.')
        d = str(input('Deseja cadastrar outra pessoa? [S/N] ')).strip().upper()[0]
    if d == 'N':
        break
media = soma / len(lista)
print('-*-'*15)
print(lista)
if len(lista) == 1:
    print('Foi cadastrada apenas 1 pessoa.')
else:
    print(f'Foram cadastradas {len(lista)} pessoas')
print(f'A média das idades das pessoas é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in lista:
    if p['gen'] == 'F':
        print(f'{p["nome"]} ', end='')
print('.')
print('A lsta das pessoas com idade acima da média: ', end='')
for p in lista:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')
