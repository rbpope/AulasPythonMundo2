teste = list()
teste.append('Renato')
teste.append(45)
print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'leonora'
teste[1] = 45
galera.append(teste[:])
print(galera)