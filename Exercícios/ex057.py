gen = str(input('Qual o seu gênero? [M/F] ').strip().upper()[0])
while gen not in 'MF':
    gen = str(input('Opção inválida, tente novamente: ').strip().upper()[0])
if gen == 'M':
    print('Você informou o genero masculino.')
if gen == 'F':
    print('Você informou o genero feminino.')
