d = int(input('Quantos dias o carro ficou com o cliente? '))
kmr = float(input('Quantos Km foram rodados? '))
vd = float(60.00)
vkmr = float(0.15)
vdt = d * vd
pkmr = kmr * vkmr
vt = vdt + pkmr
print('O valor total a ser pago é R${:.2f}'.format(vt))
print('Discriminando o valor temos que foram {} dias a R${:.2f}\nForam {}Km rodados a R${:.2f}.'.format(d,vd, kmr, vkmr))
print('Pagar R${:.2f} em diárias e R${:.2f} em Kilometragem'.format(vdt, pkmr))
