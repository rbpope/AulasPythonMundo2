d = 'S'
cont = soma = media = maior = menor = 0
while True:
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    d = str(input('Deseja adicionar mais um número: [S/N] ')).strip().upper()[0]
    if d == 'N':
        break
    media = soma / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            num = menor
print(f'Você digitou {cont} números, a média entre eles foi {media:.2f}, o maior número digitado foi {maior} e o menor foi {menor}.')

