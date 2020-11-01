matriz = [[0, 0 ,0], [0, 0, 0], [0, 0, 0]]
somapar = soma = maior = 0
for l in range (0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))
        if matriz[1][c] > maior:
            maior = matriz[1][c]
'''soma = (matriz[0][2] + matriz[1][2] + matriz[2][2])''' # uma altenativa também deu certo, poré usar for in é mais elegante
print('*'*35)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
for l in range(0,3):
    soma += matriz[l][2]
print('*'*35)
print(f'A soma de todos os valores pares digitados foi {somapar}.')
print(f'A soma dos valores da terceira coluna foi {soma}.')
print(f'O maior valor digitado da segunda linha foi {maior}.')