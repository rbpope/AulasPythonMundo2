def area(larg, comp):
    a = l * h
    print('-='*25)
    print(f'A área do seu terreno de {l}m X {h}m é {a} m²')
    print('-=' * 25)


l = float(input('Qual a largura do terreno em m: '))
h = float(input('Qual a profundidade do seu terreno em m: '))
area(l, h)

