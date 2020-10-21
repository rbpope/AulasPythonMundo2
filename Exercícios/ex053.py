frase = str(input('Digite uma frase: ')).strip()
f = frase.upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A Frase: {}, é um palíndromo.'.format(frase))
else:
    print('A frase: {}, \033[7;31mnão\033[m é um palíndromo'.format(frase))
