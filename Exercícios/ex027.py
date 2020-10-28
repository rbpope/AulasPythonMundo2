n = str(input('Qual é o seu nome completo? ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!\nSeu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))
