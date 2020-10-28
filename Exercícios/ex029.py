cores = {'limpa':'\033[m',
         'alerta':'\033[1;31;40m'}
v = int(input('Qual a velocidade do carro? '))
if v > 80:
    ve = int(v - 80)
    multa = float(ve*7.0)
    print('{}Você está {}Km/h acima do limite de velocidade e foi multado em R${:.2f}!{}'.format(cores['alerta'], ve, multa, cores['limpa']))
else:
    print('Tenha um bom dia!!')
