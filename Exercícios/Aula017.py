lanche = ['Hamburguer', 'Suco','Pizza', 'Pudim']
print(lanche)
lanche.append('Cookie')
print(lanche)
lanche.insert(1, 'Batata Frita')
print(lanche)
del lanche[1]
print(lanche)
lanche.pop()
print(lanche)
lanche.remove('Pizza')
print(lanche)
if 'Pizza' in lanche:
    lanche.remove('Pizza')
print(lanche)
if 'Suco' in lanche:
    lanche.remove('Suco')
print(lanche)