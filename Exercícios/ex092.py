from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().capitalize()
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteria de trabalho: [0 se não tem] '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - datetime.now().year
print('-=-'*10)
for k, v in dados.items():
    print(f'   - {k} tem o valor {v}')
