def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores passados')
    for valor in num:
        print(f'{valor} ', end=' ')
        if cont == 0:
            maior = cont
        else:
            if maior < valor:
                maior = valor
        cont += 1
    print()
    print(f'Foram informados {cont} valores e o maior valor é {maior}.')


maior(2, 9, 6, 10)