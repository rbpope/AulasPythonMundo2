def  voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        return f'Com {idade} anos, ainda não pode votar.'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos, o voto é optativo.'
    else:
        return f'COm {idade} anos o voto é obrigatório.'

nasc = int(input('Ano de nascimento: '))
print(voto(nasc))