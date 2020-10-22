print('-=-'*20)
print('Gerador de PA')
print('-=-'*20)
cont = 1
primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro
while cont <= 10:
    print('{} '.format(termo), end=' ')
    termo += razao
    cont +=1
print('FIM')

'''for c in range(termo, decimo + razao, razao):
    print(c, end=' ')'''
print('ACABOU')