lanche = ('Hambúrger', 'Suco', 'Batata', 'Pudim')
'''for c in lanche:
    print(f'Vou comer {c}')'''
'''for cont in range(0, len(lanche)):
    print(f' Eu vou comer {lanche[cont]} na posição {cont}.')'''
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}.')

#print(sorted(lanche))
