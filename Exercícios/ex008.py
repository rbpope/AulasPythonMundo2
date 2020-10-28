medida = float(input('Qual a medida em metros? '))
cm = float(medida * (pow(10,2)))
mm: float = (medida * 10**3)
plural = float(1.0)
if medida <= plural:
    print('A medida de {:.1f} metro equivale a {:.1f} centimetros e a {:.1f} milimetros.'.format(medida, cm, mm))
if medida > plural:
    print('A medida de {:.1f} metros equivalem a {:.1f} centimetros e a {:.1f} milimetros.'.format(medida, cm, mm))
