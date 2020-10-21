from time import sleep
print('----'*20)
print('Escolha dois números e depois selecione qual operação deseja fazer:')
print('----'*20)
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
opcao = 0
while opcao != 5:
    print('''Escolha a sua opção:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Escolher novos números
    [5] sair''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        s = n1 + n2
        print(f'A soma de {n1} com {n2} é {s}.')
    elif opcao == 2:
        m = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {m}.')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2}, {maior} é o maior número.')
    elif opcao == 4:
        print('----' * 20)
        print('Escolha dois números e depois selecione qual operação deseja fazer:')
        print('----' * 20)
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
    elif opcao ==5:
        print('Finalizando...')
    else:
        print('Opção inválida.')
    sleep(3)
print('Obrigado!')
