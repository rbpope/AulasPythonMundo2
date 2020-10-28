nome = str(input('Qual é o seu nome completo? ')).strip()
print(f'O nome em minúsculas é {nome.lower()}\nO nome em maiusculas é {nome.upper()}.')
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
