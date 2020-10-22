n = cont = soma = 0
n = int(input('Digite um valor [digite 999 para parar]: '))
while n != 999:
    soma = soma + n
    cont += 1
    n = int(input('Digite um valor [digite 999 para parar]: '))
print('Você digitou {} números e a soma deles foi {}.'.format((cont), (soma)))
