cont = 0

termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
decimo = termo + (10-1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end=' ')
print('ACABOU')