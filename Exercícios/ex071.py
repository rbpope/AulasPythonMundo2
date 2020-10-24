print('='*30)
print('{:^30} Banco Pope')
print('='*30)
valor = int(input('Digite o valor desejado R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de cédulas de R${ced}.')


